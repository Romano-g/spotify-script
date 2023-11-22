import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

tracks = []

artistas_file = open('artistas.txt', 'r')
artista = [x.strip('\n') for x in artistas_file.readlines()]

numero_artista = len(artista)

load_dotenv()

username = os.getenv('USER')
playlist_id = os.getenv('PLAYLIST_ID')

client_id_env = os.getenv('CLIENT_ID')
client_secret_env = os.getenv('CLIENT_SECRET')
client_redirect_uri = os.getenv('REDIRECT_URI')

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id= client_id_env,
                                               client_secret= client_secret_env,
                                               redirect_uri= client_redirect_uri,
                                               scope="user-library-read"))

for x in range(0, numero_artista):
    result = sp.search(artista[x], limit=3)

    for i, t in enumerate(result['tracks']['items']):
        tracks.append(str(t['id'].strip('u')))
        print('adicionando a track', t['id'], t['name'])

while tracks:
    try:
        result = sp.user_playlist_add_tracks(username, playlist_id, tracks[:1])
    except:
        print('error')

    tracks = tracks[1:]