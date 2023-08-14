import requests
import json
def get_playlist_from_url(url:str):
    with open("ytapi.pub","r") as apifile:
        api_key=apifile.read()
    playlist_id=url.split("playlist?list=")[1]
    playlist_items_url = f'https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=5&playlistId={playlist_id}&key={api_key}'
    playlist_items_data = requests.get(playlist_items_url).json()
    playlist_data=json.dumps(playlist_items_data, indent=4)  # print the videos in the playlist

    playlist_general_metadata_url=f'https://www.googleapis.com/youtube/v3/playlists?key={api_key}&id={playlist_id}&part=id,snippet&fields=items(id,snippet(title,channelId,channelTitle))'
    playlist_general_metadata=requests.get(playlist_general_metadata_url).json()
    playlist_general_metadata=json.dumps(playlist_general_metadata,indent=4)

    playlist_metadata=json.loads(playlist_general_metadata)
    playlist_name=playlist_metadata["items"][0]["snippet"]["title"]
    playlist_channel=playlist_metadata["items"][0]["snippet"]["channelTitle"] 

    
    return playlist_data,playlist_name,playlist_channel
