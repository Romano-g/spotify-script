import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

load_dotenv()

client_id_env = os.getenv('CLIENT_ID')
client_secret_env = os.getenv('CLIENT_SECRET')
client_redirect_uri = os.getenv('REDIRECT_URI')

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id= client_id_env,
                                               client_secret= client_id_env,
                                               redirect_uri= client_redirect_uri,
                                               scope="user-library-read"))

results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])