from email.mime import audio
import pafy
import vlc
import json
import re, requests, subprocess, urllib.parse, urllib.request
from bs4 import BeautifulSoup
from pytube import YouTube


def get_file():
    playlist_name="fucc"
    with open(f"cleaned_{playlist_name}_pl.json",'r') as jsonfile:
        playlist_json=json.load(jsonfile)

    k1=list(playlist_json.keys())[0]
    first_data=playlist_json[k1]
    vid_url=f'https://www.youtube.com/watch?v={first_data["video_id"]}'
    selected_video = YouTube(vid_url)
    #print(dir(selected_video))

    audio_stream=selected_video.streams.filter(only_audio=True,file_extension="mp4").first()
    audio_stream.download()
    print('Download Completed!')

    print(audio_stream.title)

def convert_file(title="Do I Wanna Know.mp4"):


    command = "ffmpeg -i video_downloads/doiwannaknow.mp4 -ab 160k -ac 2 -ar 44100 -vn wav_files/doiwannaknow.wav"

    subprocess.call(command, shell=True)




if __name__=="__main__":
    convert_file()