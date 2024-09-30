import os
import subprocess
from screeninfo import get_monitors
import pyautogui
import psutil
import time
from pynput import mouse
import keyboard
import pygetwindow as gw
from PIL import Image

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

def on_key_press(event):
    if event.name == 'enter' and keyboard.is_pressed('ctrl'):
        print("Combinação de teclas Ctrl + Enter pressionada!")

def on_click(x, y, button, pressed):
    if pressed:
        print('Mouse clicked at ({0}, {1})'.format(x, y))

# Inicia o listener do mouse
#with mouse.Listener(on_click=on_click) as listener:
    #listener.join()

def verificar_processo(nome_processo):
    for processo in psutil.process_iter(['name']):
        if processo.info['name'] == nome_processo:
            return True
    return False

def fechar_processo(nome_processo):
    for processo in psutil.process_iter(['name']):
        if processo.info['name'] == nome_processo:
            processo.kill()

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

def open_shortcut_on_monitor(shortcut_path, monitor_number):
    # Obter a lista de monitores conectados
    monitors = get_monitors()

    # Verificar se o número do monitor fornecido é válido
    if monitor_number < 1 or monitor_number > len(monitors):
        print("Número de monitor inválido!")
        return

    # Obter as informações do monitor desejado
    monitor = monitors[monitor_number - 1]
    x = monitor.x
    y = monitor.y
    width = monitor.width
    height = monitor.height

    # Abrir o atalho usando o comando subprocess
    subprocess.Popen([shortcut_path], shell=True)

    # Aguardar um segundo para a janela do atalho abrir
    time.sleep(1)

    # Obter a janela mais recente (a janela do atalho)
    #shortcut_window = gw.getWindowsWithTitle('TOTVS Moda')[0]

    # Mover a janela do atalho para as coordenadas corretas
    #shortcut_window.moveTo(x, y)
    #shortcut_window.resizeTo(width, height)


#pyautogui.move(1070, 130)


nome_processo = "ua-client.exe"
if verificar_processo(nome_processo):
    fechar_processo(nome_processo)
nome_atalho = "VirtualAge.lnk"
monitor_desejado = 1  # Índice do monitor desejado (começando em 0)

lista = []

# Loop infinito
while True:
    # Solicita ao usuário para digitar um valor
    valor = input("Digite o numero das requisições: ")

    # Verifica se o usuário digitou 'sair'
    if valor.lower() =='sair':
     break
        
    lista.append(valor)

# Exibe a lista
#print("A lista é:", lista)

shortcut_path = '%USERPROFILE%\\Desktop\\VirtualAge.lnk'
monitor_number = 1
open_shortcut_on_monitor(shortcut_path, monitor_number)

while True:
        imagem_tela = ".\\Rotinas\\screenshot\\screenshot1.png"
        pyautogui.screenshot(imagem_tela)
        cor_procurada = (255, 159, 111)
        posicao_cor = procurar_cor_na_imagem(imagem_tela, cor_procurada)
        if posicao_cor is None:
            continue
        else:     
            break

#abrir_atalho(nome_atalho, monitor_desejado)
time.sleep(30)
pyautogui.typewrite("giovane")
pyautogui.press('tab')
pyautogui.typewrite("Darkness") 
pyautogui.press('enter')
time.sleep(1)
pyautogui.typewrite('1')
time.sleep(1)
pyautogui.press('down')
time.sleep(1)
pyautogui.press('down')
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)
pyautogui.press('enter')
time.sleep(3)
#pyautogui.keyDown('esc')
#time.sleep(3)
pyautogui.keyDown('alt')
time.sleep(3)
pyautogui.press('o')
time.sleep(3)
pyautogui.keyUp('alt')
time.sleep(3)
pyautogui.press('c')
time.sleep(3)
pyautogui.typewrite("CMCFP019")
time.sleep(3)
pyautogui.press('F12')
time.sleep(3)


for valor in lista:
    # Percorre cada linha do arquivo
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.typewrite(valor)
        time.sleep(1)
        pyautogui.press('tab')    
        time.sleep(1)    
        pyautogui.keyDown('alt')
        time.sleep(1)
        pyautogui.press('o')
        time.sleep(1)
        pyautogui.keyUp('alt')
        time.sleep(1)
        pyautogui.press('F4')
        time.sleep(1)   
        pyautogui.click(977, 190)
        time.sleep(1)
        pyautogui.keyDown('alt')
        time.sleep(1)
        pyautogui.press('a')
        time.sleep(1)
        pyautogui.keyUp('alt')
        pyautogui.typewrite("D")
        pyautogui.keyDown('alt')
        time.sleep(1)
        pyautogui.press('o')
        time.sleep(1)
        pyautogui.keyUp('alt')
        time.sleep(1)
        pyautogui.keyDown('esc')        
        time.sleep(1)
        pyautogui.press('F2')

if verificar_processo(nome_processo):
    fechar_processo(nome_processo)
