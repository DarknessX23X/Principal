from tkinter import *
import psutil
import os
import tkinter.messagebox as messagebox
import time
import pyautogui
from PIL import Image
import clipboard

nome_atalho = "VirtualAge.lnk"

def abrir_atalho(caminho_atalho):
    try:
        caminho_area_trabalho = os.path.expandvars('%USERPROFILE%\\Desktop')
        caminho_completo = os.path.join(caminho_area_trabalho, caminho_atalho)
        print(caminho_completo)
        os.startfile(caminho_completo)
        print("Atalho aberto com sucesso!")
    except Exception as e:
        print("Erro ao abrir o atalho:", str(e))  

def verificar_processo(nome_processo):
    for processo in psutil.process_iter(['name']):
        if processo.info['name'] == nome_processo:
            return True
    return False

def fechar_processo(nome_processo):
    for processo in psutil.process_iter(['name']):
        if processo.info['name'] == nome_processo:
            processo.kill()

nome_processo = "ua-client.exe"
if verificar_processo(nome_processo):
        fechar_processo(nome_processo)


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

maximo = int(input("Por favor, insira um número máximo: "))
contador = 0
abrir_atalho(nome_atalho) 

while True:
        imagem_tela = "screenshot.png"
        pyautogui.screenshot(imagem_tela)
        cor_procurada = (78, 63, 44)
        posicao_cor = procurar_cor_na_imagem(imagem_tela, cor_procurada)
        if posicao_cor is None:
            continue
        else:     
            break


pyautogui.typewrite("giovane")
pyautogui.press('tab')
pyautogui.typewrite("Darkness") 
pyautogui.press('enter')
time.sleep(0.75)
pyautogui.press('1',presses=2)
pyautogui.press('enter',presses=2,interval=1.5)


while True:
        imagem_tela = "screenshot1.png"
        pyautogui.screenshot(imagem_tela)
        cor_procurada = (255, 159, 111)
        posicao_cor = procurar_cor_na_imagem(imagem_tela, cor_procurada)
        if posicao_cor is None:
            continue
        else:     
            break
   
pyautogui.hotkey('alt', 'O')
pyautogui.press('C')
    
while True:
        imagem_tela = "screenshot2.png"
        pyautogui.screenshot(imagem_tela)
        cor_procurada = (192, 255, 255)
        posicao_cor = procurar_cor_na_imagem(imagem_tela, cor_procurada)
        if posicao_cor is None:
            continue
        else:     
            break
    
pyautogui.write('INTFP053',interval=0.1)
pyautogui.press('F12')
time.sleep(2)


while contador < maximo :
    pyautogui.press('tab',presses=4)
    pyautogui.press('delete')
    pyautogui.write('02',interval=0.1)   
    time.sleep(1)      
    pyautogui.press('F4')
    time.sleep(3)
    pyautogui.hotkey('alt', 'D')
    pyautogui.hotkey('crtl', 'shift','home')
    time.sleep(1)
    pyautogui.hotkey('crtl', 'shift','end')
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1) 
    codigo = clipboard.paste()
    print(codigo)
    
    while True:
        imagem_tela = "screenshot2.png"
        pyautogui.screenshot(imagem_tela)
        cor_procurada = (48, 159, 255)
        posicao_cor = procurar_cor_na_imagem(imagem_tela, cor_procurada)
        if posicao_cor is None:
            continue
        else:     
            break
    pyautogui.press('tab',presses=16)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)
    texto = clipboard.paste()
    print(clipboard.paste())
    if "encontrado!" or "cadastrada" in texto: 
        print("Não Encontrado")
        exit()
        pyautogui.press('esc')
        time.sleep(0.75)
        pyautogui.press('space')
        pyautogui.hotkey('shift', 'tab')
        pyautogui.press('tab',presses=13)
        pyautogui.press('r')
        pyautogui.hotkey('alt', 'P')
        time.sleep(0.75)
        pyautogui.press('s')
        while True:
            imagem_tela = "screenshot3.png"
            pyautogui.screenshot(imagem_tela)
            cor_procurada = (47, 176, 192)
            posicao_cor = procurar_cor_na_imagem(imagem_tela, cor_procurada)
            if posicao_cor is None:
                continue
            else:     
                break
        pyautogui.press('esc')
        pyautogui.press('F4')
        pyautogui.hotkey('shift', 'tab')
        pyautogui.press('tab',presses=4)
        pyautogui.write('01',interval=0.1)
        pyautogui.press('F4') 
        pyautogui.hotkey('shift', 'tab')
        pyautogui.press('tab',presses=13)
        pyautogui.press('C')
        pyautogui.press('tab',presses=3)
        pyautogui.press('space')
        pyautogui.hotkey('alt', 'P')
        time.sleep(0.75)
        pyautogui.press('s')
        while True:
            imagem_tela = "screenshot4.png"
            pyautogui.screenshot(imagem_tela)
            cor_procurada = (47, 176, 192)
            posicao_cor = procurar_cor_na_imagem(imagem_tela, cor_procurada)
            if posicao_cor is None:
                continue
            else:     
                break
        pyautogui.press('esc')
        pyautogui.press('F4')
        contador += 1
    else:
        contador += 1    