"""
Service for interacting with Spotify API
"""
import urllib.parse
from typing import Dict, Any
import requests
from fastapi import HTTPException

from config.settings import settings


class SpotifyService:
    """Handles all Spotify API interactions"""
    
    @staticmethod
    def get_authorization_url() -> str:
        """
        Generate Spotify OAuth authorization URL
        
        Returns:
            str: Authorization URL for user to visit
        """
        params = {
            "client_id": settings.SPOTIFY_CLIENT_ID,
            "response_type": "code",
            "scope": settings.SPOTIFY_SCOPES,
            "redirect_uri": settings.SPOTIFY_REDIRECT_URI,
            "show_dialog": "true"
        }
        
        return f"{settings.SPOTIFY_AUTH_URL}?{urllib.parse.urlencode(params)}"
    
    @staticmethod
    def exchange_code_for_token(code: str) -> Dict[str, Any]:
        """
        Exchange authorization code for access token
        
        Args:
            code: Authorization code from Spotify
            
        Returns:
            dict: Token information
            
        Raises:
            HTTPException: If token exchange fails
        """
        params = {
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": settings.SPOTIFY_REDIRECT_URI,
            "client_id": settings.SPOTIFY_CLIENT_ID,
            "client_secret": settings.SPOTIFY_CLIENT_SECRET
        }
        
        response = requests.post(url=settings.SPOTIFY_TOKEN_URL, data=params)
        
        if response.status_code != 200:
            raise HTTPException(
                status_code=400,
                detail="Failed to exchange authorization code for access token"
            )
        
        return response.json()
    
    @staticmethod
    def get_user_profile(access_token: str) -> Dict[str, Any]:
        """
        Fetch user profile from Spotify
        
        Args:
            access_token: Spotify access token
            
        Returns:
            dict: User profile data
            
        Raises:
            HTTPException: If request fails
        """
        url = f"{settings.SPOTIFY_API_BASE_URL}me"
        headers = {"Authorization": f"Bearer {access_token}"}
        
        response = requests.get(url=url, headers=headers)
        
        if response.status_code != 200:
            raise HTTPException(
                status_code=400,
                detail="Failed to fetch user profile"
            )
        
        return response.json()
    
    @staticmethod
    def get_user_top_tracks(access_token: str, limit: int = 10) -> Dict[str, Any]:
        """
        Fetch user's top tracks from Spotify
        
        Args:
            access_token: Spotify access token
            limit: Number of tracks to fetch (default: 10)
            
        Returns:
            dict: Top tracks data
            
        Raises:
            HTTPException: If request fails
        """
        url = f"{settings.SPOTIFY_API_BASE_URL}me/top/tracks"
        headers = {"Authorization": f"Bearer {access_token}"}
        params = {"limit": limit}
        
        response = requests.get(url, headers=headers, params=params)
        
        if response.status_code != 200:
            raise HTTPException(
                status_code=400,
                detail="Failed to fetch top tracks"
            )
        
        return response.json()
    
    @staticmethod
    def get_user_top_artists(access_token: str, limit: int = 10) -> Dict[str, Any]:
        """
        Fetch user's top artists from Spotify
        
        Args:
            access_token: Spotify access token
            limit: Number of artists to fetch (default: 10)
            
        Returns:
            dict: Top artists data
            
        Raises:
            HTTPException: If request fails
        """
        url = f"{settings.SPOTIFY_API_BASE_URL}me/top/artists"
        headers = {"Authorization": f"Bearer {access_token}"}
        params = {"limit": limit}
        
        response = requests.get(url, headers=headers, params=params)
        
        if response.status_code != 200:
            raise HTTPException(
                status_code=400,
                detail="Failed to fetch top artists"
            )
        
        return response.json()
