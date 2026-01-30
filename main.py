"""
Main FastAPI application for Spotify Roast
"""
from fastapi import FastAPI, HTTPException, Query, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Annotated, Optional

from config.settings import settings
from models.spotify_models import UserData, Track, Artist
from services.spotify_service import SpotifyService
from services.roast_service import RoastService


# Initialize FastAPI app
app = FastAPI(
    title="Spotify Roast",
    description="Get your music taste roasted based on your Spotify data",
    version="1.0.0"
)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Setup Jinja2 templates
templates = Jinja2Templates(directory="templates")

# Initialize services
spotify_service = SpotifyService()
roast_service = RoastService()


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    """
    Render the home page
    
    Args:
        request: FastAPI request object
        
    Returns:
        HTMLResponse: Rendered home page
    """
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/login", response_class=RedirectResponse)
async def login():
    """
    Redirect user to Spotify authorization page
    
    Returns:
        RedirectResponse: Redirect to Spotify OAuth
    """
    auth_url = spotify_service.get_authorization_url()
    return RedirectResponse(auth_url)


@app.get("/callback", response_class=HTMLResponse)
async def callback(
    request: Request,
    code: Annotated[Optional[str], Query()] = None,
    error: Annotated[Optional[str], Query()] = None
):
    """
    Handle OAuth callback from Spotify
    
    Args:
        request: FastAPI request object
        code: Authorization code from Spotify
        error: Error message if authorization failed
        
    Returns:
        HTMLResponse: Rendered roast page
        
    Raises:
        HTTPException: If authorization fails
    """
    # Check for errors
    if error is not None:
        raise HTTPException(
            status_code=400,
            detail=f"Spotify authorization failed: {error}"
        )
    
    if code is None:
        raise HTTPException(
            status_code=400,
            detail="No authorization code received"
        )
    
    # Exchange code for token
    token_info = spotify_service.exchange_code_for_token(code)
    access_token = token_info["access_token"]
    
    # Fetch user data
    user_profile = spotify_service.get_user_profile(access_token)
    top_tracks_data = spotify_service.get_user_top_tracks(access_token)
    top_artists_data = spotify_service.get_user_top_artists(access_token)
    
    # Format data
    top_tracks = [
        Track(
            track=t["name"],
            artists=[artist["name"] for artist in t["artists"]]
        )
        for t in top_tracks_data["items"]
    ]
    
    top_artists = [
        Artist(
            artist=a["name"],
            genres=a["genres"]
        )
        for a in top_artists_data["items"]
    ]
    
    # Create user data model
    user_data = UserData(
        user_name=user_profile.get("display_name", "Music Lover"),
        top_tracks=top_tracks,
        top_artists=top_artists
    )
    
    # Generate roast
    roast = roast_service.generate_roast(user_data)
    
    # Render roast page
    return templates.TemplateResponse(
        "roast.html",
        {
            "request": request,
            "user_name": user_data.user_name,
            "roast": roast
        }
    )


@app.get("/health")
async def health_check():
    """
    Health check endpoint
    
    Returns:
        dict: Health status
    """
    return {
        "status": "healthy",
        "service": "Spotify Roast API",
        "version": "1.0.0"
    }


if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(
        "main:app",
        host=settings.APP_HOST,
        port=settings.APP_PORT,
        reload=settings.DEBUG
    )
