import os
import subprocess
from screeninfo import get_monitors
import pyautogui
import psutil
import time
from pynput import mouse
import keyboard
from PIL import Image


nome_atalho = "Virtual Age - Remoto 2.lnk"
monitor_desejado = 1  # Índice do monitor desejado (começando em 0)

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


def fechar_processo(nome_processo):
    for processo in psutil.process_iter(['name']):
        if processo.info['name'] == nome_processo:
            processo.kill()


def verificar_processo(nome_processo):
    for processo in psutil.process_iter(['name']):
        if processo.info['name'] == nome_processo:
            return True
    return False
           

def abrir_atalho(caminho_atalho, monitor):
    try:
        caminho_area_trabalho = os.path.expandvars('%USERPROFILE%\\Desktop')
        caminho_completo = os.path.join(caminho_area_trabalho, caminho_atalho)
        print(caminho_completo)
        os.startfile(caminho_completo)
        print("Atalho aberto com sucesso!")

        monitores = get_monitors()
        if monitor < len(monitores):
            monitor_desejado = monitores[monitor]
            pyautogui.moveTo(monitor_desejado.x, monitor_desejado.y)

    except Exception as e:
        print("Erro ao abrir o atalho:", str(e))

nome_processo = "ua-client.exe"
if verificar_processo(nome_processo):
      fechar_processo(nome_processo)       

abrir_atalho(nome_atalho, monitor_desejado)

while True:
        imagem_tela = ".\\screenshot\\screenshot.png"
        pyautogui.screenshot(imagem_tela)
        cor_procurada = (78, 63, 44)
        posicao_cor = procurar_cor_na_imagem(imagem_tela, cor_procurada)
        if posicao_cor is None:
            continue
        else:     
            break
pyautogui.typewrite("automacao")
pyautogui.press('tab')
pyautogui.typewrite("k8X4G3i6") 
pyautogui.press('enter')
time.sleep(1)
while True:
        imagem_tela = ".\\screenshot\\screenshot2.png"
        pyautogui.screenshot(imagem_tela)
        cor_procurada = (255, 0, 0)
        posicao_cor = procurar_cor_na_imagem(imagem_tela, cor_procurada)
        if posicao_cor is None:
            continue
        else:     
            break
pyautogui.hotkey('alt', 'O')
pyautogui.press('C')
pyautogui.write("INTFP053",interval=0.1)
pyautogui.press('F12')
while True:
        imagem_tela = ".\\screenshot\\screenshot3.png"
        pyautogui.screenshot(imagem_tela)
        cor_procurada = (192, 255, 255)
        posicao_cor = procurar_cor_na_imagem(imagem_tela, cor_procurada)
        if posicao_cor is None:
            continue
        else:     
            break
pyautogui.hotkey('alt', 't')

nome_processo = "ua-client.exe"
if verificar_processo(nome_processo):
    fechar_processo(nome_processo)