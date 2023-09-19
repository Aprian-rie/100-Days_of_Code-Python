### Day 46 making a musical time machine project
Building a python Time Machine


### Description

It goes back in time to find the music that was in the top 100 shots that was being played all over the radio 
The platform that will be used is billboard

### Steps To complete the Project

1. Created an ``input()`` prompt asking the user which year you would like to travel to in YYYY-MM-DD:
```python
date = input("What year do you want to travel to? Type the date in this format YYYY-MM-DD")
```
2. Scraping the top 100 song titles on that date into a python list.
```python
import requests
from bs4 import BeautifulSoup
# Getting the data webpage
URL = f"https://www.billboard.com/charts/hot-100/{date}/"
response = requests.get(URL)
billboard_webpage = response.text

# print(billboard_webpage)

# Scraping the datato obtain the titles
soup = BeautifulSoup(billboard_webpage, "html.parser")

titles = soup.select('h3.a-no-trucate')
artist = soup.find(name="span", class_="a-no-trucate")
titles_list = []

# Storing the song titles in a list titles_list
for title in titles:
    titles_list.append(title.getText().strip())
```

    the song lists were obtained from billboards official site: https://www.billboard.com/charts/hot-100/{your_date}
3. In order to create a playlist in spotify you must have an acoount with Spotify after that we go to the developer dashboard
    
    https://developer.spotify.com/dashboard/ and create a Spotify app
4. After creating the Spotify app, copy the Client ID and the Client Secret into the python project
5. Authenticating with spotify is kinda challenging so I used spotipy using OAuth
    
    ### How to Authenticate the Python Project with Spotify Using the unique Client ID and Client Secret
```python
import spotipy
from spotipy.oauth2 import SpotifyOAuth

Client_ID = "1b0a33746f9f4786a5f0fe4818d5d6e6"
client_SECRET = "9c0f1ee9cdb44b0eb347c82551dab33e"
redirect_url = "http://localhost:8080/"

# Apryan_ID is the user ID in Spotify


# Defining the scope of our programme as it is allowed to create and modify a private 
# playlist. There are tons of other scopes we can put but this is for the purpose of the 
# project
scope = "playlist-modify-private"

sp_auth = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=Client_ID, client_secret=client_SECRET, redirect_uri=redirect_url, scope=scope))

# Getting the user_ID 
current_user = sp_auth.current_user()
# This returns a dictionary therefore we look for the value of the "id key
Apryan_ID = sp_auth.current_user()["id"]
# Saved it to Apryan_ID
```
6. After that we create a list of Spotify Song URIs of the list of songs found from scraping the song titles of the given year
```python
# Creating an empty list called song_uris
song_uris = []

# Splitting the date to the year only so as to refine our search
year = date.split("-")[0]

# Looping through the for loop
for song in titles_list:
    
    # The .search is for searching the songs according to the year 
    result = sp_auth.search(q=f"track: {song} year: {year}", type="track")
    # print(result)
    
    # the exception is used for handling songs that do not exist in Spotify
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped")
```
7. The last step is to create a new private playlist with the name "YYYY-MM-DD Billoard 100" and then adding the songs that I have searched to the playlist
```python
# Creates a new playlist using my User ID and the title
# and the last parameter is a boolean asking whether the playlist is public(true)
# or private (false)
my_playlist = sp_auth.user_playlist_create(Apryan_ID, f"{date} Billboard 100", False)
playlist_id = my_playlist["id"]

# This is for adding the songs to the playlist taking the parameters
#play;ist_id and the song_uris (song locations)
sp_auth.playlist_add_items(playlist_id=playlist_id, items=song_uris)
```

### The End !

By Aprian