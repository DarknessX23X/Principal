import time
import pyautogui
from PIL import Image
import os
import shutil

diretorio_origem = 'C:\\config\\XML'
diretorio_destino = 'X:\\Fiscal\\98 - Fiscal\\XML2'

def procurar_cor_na_imagem(imagem, cor):
    # Abrir a imagem
    img = Image.open(imagem)

    # Converter a imagem para o modo RGB
    img_rgb = img.convert("RGB")

    # Obter as dimensões da imagem
    largura, altura = img_rgb.size

    # Percorrer todos os pixels da imagem
    for x in range(largura):
        for y in range(altura):
            # Obter a cor do pixel na posição (x, y)
            pixel = img_rgb.getpixel((x, y))

            # Verificar se a cor do pixel corresponde à cor procurada
            if pixel == cor:
                return (x, y)  # Retornar a posição do pixel

    return None  # Retornar None se a cor não for encontrada


pyautogui.click(162,142,2)
with open('NOTAS1.txt', 'r') as arquivo:   
        total_linhas = len(arquivo.readlines())
        contador = total_linhas
        arquivo.seek(0)
        for linha in arquivo:      
            print(f'{contador}: {linha}', end='')      
            time.sleep(3)
            pyautogui.press('tab',presses=11)                                           
            pyautogui.write(linha)
            pyautogui.press("F4")
            pyautogui.press("left")
            pyautogui.press("space")
            pyautogui.hotkey('Alt', 'x')
            time.sleep(3)
            pyautogui.press("down",presses=20)
            time.sleep(3)
            pyautogui.click(914,623,2)
            pyautogui.press("down",presses=5)
            pyautogui.click(913,530,2)
            pyautogui.press("down",presses=7)
            pyautogui.press("enter")
            time.sleep(3)
            pyautogui.press("enter")
            pyautogui.press("F2")           
            contador -= 1
            arquivos = os.listdir(diretorio_origem)
            for arquivo in arquivos:
                if arquivo.endswith('.xml'):
                    try:
                        shutil.move(os.path.join(diretorio_origem, arquivo), diretorio_destino)
                    except Exception as e:
                        print(f"Ocorreu um erro ao mover os arquivos: {e}")




