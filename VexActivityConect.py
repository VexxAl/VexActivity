import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Configura las credenciales de la aplicación de Spotify
SPOTIPY_CLIENT_ID = '0d8851a56e7d40309937384984ca46d3'
SPOTIPY_CLIENT_SECRET = '8137e44a77204128b2b5d2f79e61c5f4'
SPOTIPY_REDIRECT_URI = 'http://localhost:8000/callback'

# Inicializa el objeto de autorización
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope='user-read-playback-state'))