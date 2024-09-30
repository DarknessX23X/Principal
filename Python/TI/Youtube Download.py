from pytube import Playlist, YouTube
from moviepy.editor import *
import os
import youtube_dl
import os

def convert_mp4_to_mp3(folder):
    for file in os.listdir(folder):
        if file.endswith(".mp4"):
            video_path = os.path.join(folder, file)
            mp3_path = os.path.join(folder, file[:-4] + ".mp3")
            try:
                video = VideoFileClip(video_path)
                video.audio.write_audiofile(mp3_path)
                video.close()
                os.remove(video_path)
                print(f"Conversão concluída e arquivo {file} removido com sucesso!")
            except Exception as e:
                print(f"Ocorreu um erro ao converter ou remover o arquivo {file}: {str(e)}")

def download_youtube_music_playlist(playlist_url, output_folder):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])
        print("Download da playlist concluído com sucesso!")

# Insira a URL da playlist do YouTube Music abaixo
playlist_url = 'https://music.youtube.com/playlist?list=PLDsZzVlR5iMPWVWvsQkBRFR1TnEJzBcnA'

output_folder = 'G:\\Download'

download_youtube_music_playlist(playlist_url, output_folder)

convert_mp4_to_mp3(output_folder)


