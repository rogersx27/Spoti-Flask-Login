import os
from dotenv import load_dotenv

load_dotenv()

from spotipy.oauth2 import SpotifyOAuth
from flask import url_for

def create_spotify_oauth2():
    """
    Creates and returns a SpotifyOAuth object with the specified parameters.

    Returns:
        SpotifyOAuth: The created SpotifyOAuth object.
    """
    return SpotifyOAuth(
        client_id=os.getenv('CLIENT_ID'),
        client_secret=os.getenv('CLIENT_SECRET'),
        redirect_uri= url_for('redirectPage', _external=True),
        scope="user-library-read"
    )