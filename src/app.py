from __init__ import app

from flask import request, url_for, session, redirect

from Utils import oauth2, get_current_user

import spotipy

TOKEN_INFO = 'token_info'


@app.route('/')
def home():
    return redirect(url_for('login', _external=True))


@app.route('/login')
def login():
    sp_oauth = oauth2()
    auth_url = sp_oauth.get_authorize_url()

    # print(auth_url)
    # print(url_for('redirectPage', _external=True),)

    return redirect(auth_url)


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login', _external=True))


@app.route('/redirect')
def redirectPage():
    sp_oauth = oauth2()
    session.clear()
    code = request.args.get('code')
    token_info = sp_oauth.get_access_token(code)
    session[TOKEN_INFO] = token_info

    return redirect(url_for('index', _external=True))


@app.route('/index')
def index():
    return 'Here is the index page'


@app.route('/getTracks')
def getTracks():
    current_user = get_current_user()

    list_of_tracks = current_user.current_user_saved_tracks()

    list_of_names = [list_of_tracks['items'][i]['track']['name']
                     for i in range(len(list_of_tracks['items']))]

    return list_of_names


@app.route('/getUserInfo')
def getUserInfo():
    current_user = get_current_user()

    user_info = current_user.current_user()

    return user_info


@app.route('/getPlaylists')
def getPlayingTrack():
    current_user = get_current_user()

    playlist_list = current_user.current_user_playlists(limit=50)

    print(type(playlist_list))

    playlist_collection = {}
    for i, playlist in enumerate(playlist_list['items'], start=1):
        key = i
        playlist_collection[key] = {
            'id': playlist['id'],
            'name': playlist['name'],
            'description': playlist['description'] if playlist['description'] else 'No Description Available',
            'url': playlist['external_urls']['spotify'],
            'total_tracks': playlist['tracks']['total'],
            'cover_image': playlist['images'][0]['url'] if len(playlist['images']) > 0 else 'No Image Available',
            'owner': playlist['owner']['display_name'] if playlist['owner']['display_name'] else 'No Owner Available'
        }
    return sorted(playlist_collection.items())
    # Filter the playlist by the number of tracks
    # return sorted(playlist_collection.items(), key=lambda x: x[1]['total_tracks'], reverse=True)


if __name__ == '__main__':
    app.run()
