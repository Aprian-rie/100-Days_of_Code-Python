import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

Client_ID = "1b0a33746f9f4786a5f0fe4818d5d6e6"
client_SECRET = "9c0f1ee9cdb44b0eb347c82551dab33e"
redirect_url = "http://localhost:8080/"
Apryan_ID = '31ebbaxfip72gufwftzob53x3moa'

date = input("What year would you like to travel to YYY-MM-DD: ")

# Getting the data webpage
URL = f"https://www.billboard.com/charts/hot-100/{date}/"
response = requests.get(URL)
billboard_webpage = response.text

# print(billboard_webpage)

soup = BeautifulSoup(billboard_webpage, "html.parser")

titles = soup.select('h3.a-no-trucate')
artist = soup.find(name="span", class_="a-no-trucate")
titles_list = []

for title in titles:
    titles_list.append(title.getText().strip())

# print(titles_list)

# print(title.getText().strip())
# print(artist.getText().strip())

scope = "playlist-modify-private"
# scope = "user-read-recently-played"

sp_auth = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=Client_ID, client_secret=client_SECRET, redirect_uri=redirect_url, scope=scope))

current_user = sp_auth.current_user()
# print(current_user)
# results = sp_auth.playlist('7HNDoSF4dLMVKNaCf0GMRj')

song_uris = []

year = date.split("-")[0]
for song in titles_list:
    result = sp_auth.search(q=f"track: {song} year: {year}", type="track")
    # print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped")

my_playlist = sp_auth.user_playlist_create(Apryan_ID, f"{date} Billboard 100", False)
playlist_id = my_playlist["id"]

sp_auth.playlist_add_items(playlist_id=playlist_id, items=song_uris)