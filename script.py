import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="9b853100cca243a7a9ebd317a74e59d5",
                                               client_secret="7333cfabeacb428da40c3b6470b79916",
                                               redirect_uri="http://localhost:8080/callback",
                                               scope="user-library-read"))

results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])