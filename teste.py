import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy import SpotifyException
from dotenv import load_dotenv
import os

load_dotenv()

artists_file = open('artists.txt', 'r')
artists = [x.strip('\n') for x in artists_file.readlines()]
artists_number = len(artists)

username = os.getenv('USER')
playlist_id = os.getenv('PLAYLIST_ID')

client_id_env = os.getenv('CLIENT_ID')
client_secret_env = os.getenv('CLIENT_SECRET')
client_redirect_uri = os.getenv('REDIRECT_URI')

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id= client_id_env,
                                               client_secret= client_secret_env,
                                               redirect_uri= client_redirect_uri,
                                               scope="playlist-modify-public"))

artista = sp.artist('6mdiAmATAx73kdxrNrnlao')
print(artista)
