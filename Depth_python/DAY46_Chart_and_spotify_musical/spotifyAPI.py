from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth
import os
import spotipy

load_dotenv(r'Depth_python\DAY46_Chart_and_spotify_musical\.env')
CLIENT_ID = os.getenv('spotify_id')
CLIENT_SECRET = os.getenv('spotify_secret_key')


def creating_playlist(date, song_names_list):
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        scope='playlist-modify-private',
        redirect_uri="http://example.com/callback/",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path=r'Depth_python\DAY46_Chart_and_spotify_musical\token.txt'
    )
    )

    user_id = sp.current_user()["id"]

    song_uris = []
    year = date.year

    for song in song_names_list:
        result = sp.search(
            q=f"track:{song} year:{year}", type="track", limit=1, market='US')
        try:
            uri = result["tracks"]["items"][0]["uri"]
        except IndexError:
            print(f"{song} doesn't exist in Spotify. Skipped.")
        else:
            song_uris.append(uri)

    playlists = sp.user_playlist_create(
        user=user_id, name=f"{date} Billboard 100.", public=False)

    sp.playlist_add_items(playlist_id=playlists["id"], items=song_uris)
    print(sp)
