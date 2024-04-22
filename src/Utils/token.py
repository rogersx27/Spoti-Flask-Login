import time
import spotipy

from flask import session, redirect, url_for
from .auth import create_spotify_oauth2


def get_access_token():
    """
    Retrieves the access token from the session or refreshes it if expired.

    Returns:
        dict: The token information containing the access token and other details.
    
    Raises:
        Exception: If no token is found in the session.
    """
    token_info = session.get('token_info', None)

    if not token_info:
        raise Exception('No token found')

    now_time = int(time.time())
    is_expired = token_info['expires_at'] - now_time < 60

    if is_expired:
        sp_oauth = create_spotify_oauth2()
        token_info = sp_oauth.refresh_access_token(token_info['refresh_token'])

    return token_info


def get_current_user():
    """
    Retrieves the current user's Spotify access token and returns a Spotify object.

    If no token is found, it redirects the user to the login page.

    Returns:
        sp (spotipy.Spotify): Spotify object authenticated with the user's access token.
    """
    try:
        token_info = get_access_token()
    except:
        print('No token found')
        return redirect(url_for('login', _external=False))

    sp = spotipy.Spotify(auth=token_info['access_token'])

    return sp
