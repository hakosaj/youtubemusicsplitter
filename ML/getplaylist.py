import requests
import json

#Api key
with open("ytapi.pub","r") as apifile:
    api_key=apifile.read()
hyvia_playlist="PLouI7YeilwCv69IHhIIIUzZjfowPnMa4Y"
fucc_playlist="PLouI7YeilwCvy2PR9T5zuP8lwml-c1p29"




playlist_items_url = f'https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=50&playlistId={fucc_playlist}&key={api_key}'
playlist_items_data = requests.get(playlist_items_url).json()
playlist_data=json.dumps(playlist_items_data, indent=4)  # print the videos in the playlist

with open("fucc_pl.json","w") as jsonfile:
    jsonfile.write(playlist_data)

def get_playlist_from_url(url:str):
    return
    with open("ytapi.pub","r") as apifile:
        api_key=apifile.read()
    
