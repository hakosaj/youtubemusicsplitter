import json

playlist_name="fucc"
with open(f"{playlist_name}_pl.json",'r') as jsonfile:
    playlist_json=json.load(jsonfile)['items']


video_data=dict()
for video in playlist_json:
    sn=first_video_data=video['snippet']

    thumbnail_url=sn['thumbnails']['default']['url']
    video_id=thumbnail_url.split("vi/")[-1].split("/")[0]

    first_video_tag=video.get('etag')
    first_video_data.pop('thumbnails')
    first_video_data.pop('position')
    first_video_data.pop('publishedAt')
    first_video_data.pop('playlistId')
    first_video_data.pop('resourceId')
    first_video_data.pop('channelTitle')

    video_data[first_video_data['title']]=first_video_data
    video_data[first_video_data['title']]['tag']=first_video_tag
    video_data[first_video_data['title']]['video_id']=video_id



playlist_core_data=json.dumps(video_data, indent=4)  # print the videos in the playlist
with open(f"cleaned_{playlist_name}_pl.json",'w') as jsonfile:
    jsonfile.write(playlist_core_data)

