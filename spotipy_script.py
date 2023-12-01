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

resultado = sp.playlist_items(playlist_id)
resultados_id = []

for id in range(len(resultado['items'])):
    resultados_id.append(resultado['items'][id]['track']['id'])

ids = []
music_ids = []

for x in range(0, artists_number):
    result = sp.search(artists[x], limit=1)
    name_path = result['tracks']['items'][0]['artists'][0]['name']
    id_path = result['tracks']['items'][0]['artists'][0]['id']

    ids.append(id_path)
    
    for id in ids:
        artista = sp.artist_top_tracks(id)
        print(artista)



    # for id in ids:
    #     artista = sp.artist_top_tracks(id)
    #     print(artista)
        #  for x in range(0, 5):
        #       music_id = artista['tracks'][x]['id']
        #       music_ids.append(music_id)

# try:
#     sp.user_playlist_add_tracks(username, playlist_id, music_ids)
# except SpotifyException:
#     os.system('cls')
#     print('Não há novas músicas para adicionar')