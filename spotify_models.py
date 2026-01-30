"""
Data models for the application
"""
from typing import List
from pydantic import BaseModel


class Track(BaseModel):
    """Represents a Spotify track"""
    track: str
    artists: List[str]


class Artist(BaseModel):
    """Represents a Spotify artist"""
    artist: str
    genres: List[str]


class UserData(BaseModel):
    """Represents user's Spotify data"""
    user_name: str
    top_tracks: List[Track]
    top_artists: List[Artist]


class TokenResponse(BaseModel):
    """Represents Spotify token response"""
    access_token: str
    token_type: str
    scope: str
    expires_in: int
    refresh_token: str
