CLIENT_ID = "9f5a622b9180437c806b8d078703f498"
CLIENT_SECRET = "8f6da2dca015445f97ac462d2131c744"


from bs4 import BeautifulSoup
import requests

import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "playlist-modify-private"
redirect = "http://example.com/"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, scope=scope,redirect_uri=redirect,show_dialog=True,cache_path="token.txt"))
user_id = sp.current_user()["id"]
# sp = spotipy.oauth2.SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET,scope= scope,redirect_uri="http://example.com")
#
# sp

# year = input("What year would you like to go to?(in YYYY-MM-DD format)")
# response = requests.get("https://www.billboard.com/charts/hot-100/" + year)
# songs_page = response.text
# soup = BeautifulSoup(songs_page,"html.parser")
# songs_list = []
# songs= soup.find_all(name="h3", class_="a-no-trucate", id="title-of-a-story")
# for song in songs:
#     text = song.get_text().strip()
#     songs_list.append(text)
#
# print(songs_list)
