# type: ignore
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy import SpotifyException
from dotenv import load_dotenv
import os

load_dotenv()

playlist_id_env = os.getenv('PLAYLIST_ID')
client_id_env = os.getenv('CLIENT_ID')
client_secret_env = os.getenv('CLIENT_SECRET')
client_redirect_uri_env = os.getenv('REDIRECT_URI')
username_env = os.getenv('USER')

artists_file = open('artists.txt', 'r')
artists = [x.strip('\n') for x in artists_file.readlines()]
artists_number = len(artists)

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=client_id_env,
    client_secret=client_secret_env,
    redirect_uri=client_redirect_uri_env,
    scope="user-library-read"
))

results_ids = []


def checker(offset: int):
    result_playlist_musics = sp.playlist_items(playlist_id_env, offset=offset)
    for id in range(len(result_playlist_musics['items'])):
        results_ids.append(result_playlist_musics['items'][id]['track']['id'])
    return


checker(0)
checker(100)
checker(200)
checker(300)
checker(400)

ids = []

for x in range(0, artists_number):
    result = sp.search(artists[x], limit=1)
    name_path = result['tracks']['items'][0]['artists'][0]['name']
    id_path = result['tracks']['items'][0]['artists'][0]['id']

    ids.append(id_path)

music_ids = []

for id in ids:
    artista = sp.artist_top_tracks(id)

    try:
        for x in range(5):
            music_id = artista['tracks'][x]['id']

            if music_id in results_ids:
                continue
            else:
                music_ids.append(music_id)
                print('Adicionando a música: ', artista['tracks'][x]['name'])
                continue
    except IndexError:
        continue

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=client_id_env,
    client_secret=client_secret_env,
    redirect_uri=client_redirect_uri_env,
    scope="playlist-modify-public"))


def add_track(start: int, end: int):
    sp.user_playlist_add_tracks(
        username_env, playlist_id_env, music_ids[start:end])


try:
    add_track(0, 100)
    add_track(100, 200)
    add_track(200, 300)
except SpotifyException:
    os.system('cls')
    print('Não há novas músicas para adicionar!')

print(f'Foram adicionadas todas as {len(music_ids)} músicas')
