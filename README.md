![Spotify logo](https://github.com/Romano-g/spotify-script/assets/143983377/6bb3085f-6f38-4033-966e-607a5fda3f4e)



# Criando playlists com Python

Este script foi elaborado com o uso da biblioteca **Spotipy**.

>"Uma biblioteca Python leve para a API da Web Spotify."

## Objetivos deste script:

1. Buscar os artistas que estão no arquivo .txt;
2. Adicionar suas top 3 musicas na playlist selecionada.

Você pode conferir o funcionamento do script em vídeo [clicando aqui!](https://youtu.be/vC1mIFwHJg4)

## Documentação e script:

A documentação oficial da biblioteca se encontra [aqui](https://spotipy.readthedocs.io/en/2.22.1/#getting-started), e também o github do criador da mesma com informações valiosas pode ser encontrado [aqui](https://github.com/spotipy-dev/spotipy).

O código final do script que utilizei no vídeo foi:

~~~python
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
~~~

## .env

Para manter os dados em segurança, utilizei um arquivo .env, você pode conferir a estrutura de dados que utilizei no arquivo .env_example ou copiando-o aqui embaixo:

~~~
CLIENT_ID=''
CLIENT_SECRET=''
REDIRECT_URI=''
USER=''
PLAYLIST_ID=''
~~~
