from googletrans import Translator
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from lyricsgenius import Genius


def get_lyrics(artist, song):
    translator = Translator()
    genius = Genius(lyric_token)
    genius.verbose = False
    # genius.remove_section_headers = True
    song_info = genius.search_song(song, artist)
    if song_info is not None:
        s = str(song_info.lyrics).splitlines()
        fix_first = s[0]
        fix_last = s[len(s)-1]
        fix_last = fix_last[:fix_last.rfind("Embed")-1]
        fix_first = fix_first[fix_first.rfind("Lyrics") + 6:]
        s[len(s)-1] = fix_last
        s[0] = fix_first
        for line in s:
            print(line + "               " + translator.translate(text=line, dest="en").text)
    else:
        print(f"Lyrics for {song} are unavailable...")


lyric_token = "3kOSGpjJUrFl3IJTWIpGqbbbmIO96C8zUq234ve4F_iJvsJdjgZTX-ChI0Mm3z_X"
ID = "b5b1c80530944fe1b480d22d176a80ee"
secret = "b8501a850d3048fcb83d4ca86d64a1a7"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=ID,
                                               client_secret=secret,
                                               redirect_uri="http://localhost:8888/callback",
                                               scope="user-read-currently-playing"))

song = sp.current_user_playing_track()['item']['name']
artist = sp.current_user_playing_track()['item']['artists'][0]['name']

print(f"Song: {song} by {artist}")
print()
get_lyrics(artist, song)