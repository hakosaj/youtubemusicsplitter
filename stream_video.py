from email.mime import audio
import pafy
import vlc
import json
import re, requests, subprocess, urllib.parse, urllib.request
from bs4 import BeautifulSoup
from pytube import YouTube
import pytube 

def remove_bracket_contents(ttl: str)-> str:
    if '(' in ttl:
        b1=ttl.find('(')
        b2=ttl.find(')')
        if b1<b2:
            ttl=ttl[:b1]+ttl[b2+1:]
    if '[' in ttl:
        b1=ttl.find('[')
        b2=ttl.find(']')
        if b1<b2:
            ttl=ttl[:b1]+ttl[b2+1:]
    return ttl

def get_file():
    playlist_name="fucc"
    with open(f"cleaned_{playlist_name}_pl.json",'r') as jsonfile:
        playlist_json=json.load(jsonfile)

    for item in list(playlist_json.keys()):
        print(item)
        first_data=playlist_json[item]
        vid_url=f'https://www.youtube.com/watch?v={first_data["video_id"]}'
        selected_video = YouTube(vid_url)
        #print(dir(selected_video))
        try: 
            audio_stream=selected_video.streams.filter(only_audio=True,file_extension="mp4").first()

            ttl=audio_stream.title.strip().replace(' ','').lower()+".mp4"
            ttl=ttl.replace("'",'').replace(',','')
            ttl=remove_bracket_contents(ttl)

            audio_stream.download(output_path="video_downloads/",filename=ttl)
            print('Download Completed!')

            convert_file_and_strip(ttl)
        except pytube.exceptions.VideoUnavailable:
            print("video not found, skipping!")

def convert_file_and_strip(title:str):


    command = f"ffmpeg -i video_downloads/{title} -ab 160k -ac 2 -ar 44100 -vn wav_files/{title.replace('.mp4','.wav')}"
    print(command)
    subprocess.call(command, shell=True)




if __name__=="__main__":
    #convert_file()
    get_file()