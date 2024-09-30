from pytube import YouTube,Playlist
from moviepy.editor import *
import os

def download_and_convert_videos(playlist_url, output_folder):
    # Criar pasta de saída se não existir
    os.makedirs(output_folder, exist_ok=True)
    
    playlist = Playlist(playlist_url)
    for video_url in playlist.video_urls:
        try:
            video = YouTube(video_url)
            file_path = video.streams.get_highest_resolution().download(output_folder)
            
            # Converter o vídeo para MP3
            mp3_path = os.path.join(output_folder, f"{video.title}.mp3")
            video_file = VideoFileClip(file_path)
            audio_file = video_file.audio
            audio_file.write_audiofile(mp3_path)
            audio_file.close()
            video_file.close()
            
            # Remover o arquivo de vídeo original
            os.remove(file_path)
            
            print(f"Download e conversão do vídeo {video.title} concluídos com sucesso!")
        except Exception as e:
            print(f"Ocorreu um erro no download ou na conversão do vídeo: {str(e)}")

# Insira a URL da playlist do YouTube abaixo
playlist_url = "https://music.youtube.com/playlist?list=PLDsZzVlR5iMPWVWvsQkBRFR1TnEJzBcnA"

# Insira o caminho para a pasta de saída
output_folder = "G:\\Download"

download_and_convert_videos(playlist_url, output_folder)