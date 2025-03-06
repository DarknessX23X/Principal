import requests
import os
import subprocess



config = "C:\\Config"
download = "C:\\Config\\Download"

def download_file(url, folder_path):
    response = requests.get(url)
    file_name = url.split('/')[-1]
    file_path = os.path.join(folder_path, file_name)
    with open(file_path, 'wb') as file:
        file.write(response.content)
    print(f'{file_name} baixado com sucesso!')

if not os.path.exists(config):
     os.makedirs(config)
if not os.path.exists(download):
     os.makedirs(download)

with open('.\\TI\\URL.txt', 'r') as file:
    # Lê e exibe o conteúdo do arquivo linha por linha
    for line in file:
        url = line.strip()
        download_file(url, download)
