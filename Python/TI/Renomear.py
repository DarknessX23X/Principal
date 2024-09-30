import os
from mutagen.easyid3 import EasyID3

def identificar_musicas(pasta):
    for raiz, diretorios, arquivos in os.walk(pasta):
        for arquivo in arquivos:
            if arquivo.endswith(".mp3"):
                caminho = os.path.join(raiz, arquivo)
                try:
                    tags = EasyID3(caminho)
                    cantor = tags["artist"][0]
                    musica = tags["title"][0]
                    print(f"Cantor: {cantor} | Música: {musica}")
                except:
                    print(f"Não foi possível identificar as informações da música: {caminho}")

identificar_musicas("G:\\Billie")                    