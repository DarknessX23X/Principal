from pytube import YouTube

def get_video_metadata(video_url):
    video = YouTube(video_url)
    
    metadata = {
        'título': video.title,
        'autor': video.author,
        'visualizações': video.views,
        'duração': video.length,
        'avaliação': video.rating,
        'descrição': video.description,
        'palavras-chave': video.keywords,
        'data de publicação': video.publish_date,
        'thumbnail': video.thumbnail_url,
    }
    
    return metadata

# Insira a URL do vídeo do YouTube abaixo
video_url = 'https://www.youtube.com/watch?v=yYOSwXSnESU'

metadata = get_video_metadata(video_url)
for key, value in metadata.items():
    print(f'{key}: {value}')