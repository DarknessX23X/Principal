import requests

def extract_text_from_image(image_path):
    api_key = 'K86412841088957'
    url = 'https://api.ocr.space/parse/image'
    payload = {
        'apikey': api_key,
        'language': 'por',
        'isOverlayRequired': False
    }
    with open(image_path, 'rb') as image_file:
        response = requests.post(url, files={'image': image_file}, data=payload)
        result = response.json()
        if result['IsErroredOnProcessing']:
            print('Erro ao processar a imagem')
        else:
            text = result['ParsedResults'][0]['ParsedText']
            save_text_to_file(text)

def save_text_to_file(text):
    with open('output.txt', 'w', encoding='utf-8') as file:
        file.write(text)


# Exemplo de uso
extract_text_from_image('c:\\config\\print.png')