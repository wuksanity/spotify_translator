from googletrans import Translator
import spotipy
from spotipy.oauth2 import SpotifyOAuth

ID = "b5b1c80530944fe1b480d22d176a80ee"
secret = "b8501a850d3048fcb83d4ca86d64a1a7"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=ID,
                                               client_secret=secret,
                                               redirect_uri="http://localhost:8888/callback",
                                               scope="user-read-currently-playing"))

print(sp.currently_playing())