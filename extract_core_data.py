import json

playlist_name="fucc"
with open(f"{playlist_name}_pl.json",'r') as jsonfile:
    playlist_json=json.load(jsonfile)['items']

first_video_data=playlist_json[0]['snippet']
first_video_data.pop('thumbnails')
first_video_data.pop('position')
first_video_data.pop('publishedAt')
first_video_data.pop('channelTitle')
first_video_data.pop('playlistId')
first_video_data.pop('resourceId')
print(first_video_data)