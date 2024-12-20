﻿import configparser
import os
import subprocess
import time
import pyautogui
from PIL import Image
import psutil
import csv
import pandas as pd
import os
import shutil
import subprocess
from datetime import datetime



#Dependencias
# pip install psutil
# pip install pyautogui
#pip install PIL

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



def abrir_atalho(nome_atalho):
    #caminho_area_trabalho = os.path.expandvars('%USERPROFILE%\\Desktop')
    #caminho_completo = os.path.join(caminho_area_trabalho, nome_atalho)
    #print(caminho_completo)
    os.startfile(nome_atalho)

def pegar_valor(arquivo_ini):
    config = configparser.ConfigParser()
    config.read(arquivo_ini)

    # Substitua 'SECAO' e 'X' pela seção e chave corretas
    x = config.get('PARAMETROS', 'X')
    y = config.get('PARAMETROS', 'Y')
    atalho = config.get('PARAMETROS', 'atalho')
    usuario = config.get('PARAMETROS', 'usuario')
    senha = config.get('PARAMETROS', 'senha')
    tempova = config.get('PARAMETROS', 'tempova')
    tempotela = config.get('PARAMETROS', 'tempotela')
    tempodicfm = config.get('PARAMETROS', 'tempoDICFM')
    tempovalidacao= config.get('PARAMETROS', 'tempovalidacao')
    caminhoorigem= config.get('PARAMETROS', 'caminhoorigem')
    caminhodestino= config.get('PARAMETROS', 'caminhodestino')
    temporelatorio= config.get('PARAMETROS', 'temporelatorio')

    return x,y,atalho,usuario,senha,tempova,tempotela,tempodicfm,tempovalidacao,caminhoorigem,caminhodestino,temporelatorio
    

def fechar_processo(nome_processo):
    for processo in psutil.process_iter(['name']):
        if processo.info['name'] == nome_processo:
            processo.kill()


def verificar_processo(nome_processo):
    for processo in psutil.process_iter(['name']):
        if processo.info['name'] == nome_processo:
            return True
    return False

while True:
# Carrrega Paramatros para as variaveis
    valor_x,valor_y,valor_atalho,valor_usuario,valor_senha,tempo_va,tempo_tela,tempo_dicfm,tempo_validacao,caminho_origem,caminho_destino,tempo_relatorio = pegar_valor('.\Config.ini')


    nome_processo = "ua-client.exe"
    if verificar_processo(nome_processo):
        fechar_processo(nome_processo)


# Inicia o Virtual Age
    abrir_atalho(valor_atalho)

#Conecta na Empresa
    time.sleep(int(tempo_va))
    pyautogui.typewrite(valor_usuario)
    pyautogui.press('tab')
    pyautogui.typewrite(valor_senha) 
    pyautogui.press('enter')
    time.sleep(int(tempo_tela))
    pyautogui.press('1')
    time.sleep(int(tempo_tela))
    pyautogui.press('enter')
    time.sleep(int(tempo_tela))
    pyautogui.press('enter')
    time.sleep(int(tempo_tela))

#Verifica se consegue entrar no TOTVS
    imagem_tela = "screenshot.png"
    pyautogui.screenshot(imagem_tela)
    cor_procurada = (239, 159, 63)
    posicao_cor = procurar_cor_na_imagem(imagem_tela, cor_procurada)

    if posicao_cor is not None:
        nome_processo = "ua-client.exe"
        if verificar_processo(nome_processo):
            fechar_processo(nome_processo)
            agora = datetime.now()
            hora_formatada = agora.strftime("%H:%M:%S")
            print("SEM VAGA PARA ENTRAR :", hora_formatada)
            continue
    else:
        time.sleep(int(tempo_va))   
        pyautogui.press('tab', presses=6)
        pyautogui.write('DICFM001',interval=0.1)
        time.sleep(int(tempo_tela))
        pyautogui.press('enter')
        time.sleep(int(tempo_dicfm))


    pyautogui.screenshot(imagem_tela)
    cor_procurada = (112, 159, 175)
    posicao_cor = procurar_cor_na_imagem(imagem_tela, cor_procurada)
    if posicao_cor is not None:
        print("A cor foi encontrada na posição:", posicao_cor)
        pyautogui.click(posicao_cor[0], posicao_cor[1])
    else: 
        nome_processo = "ua-client.exe"
        if verificar_processo(nome_processo):
            fechar_processo(nome_processo)
            agora = datetime.now()
            hora_formatada = agora.strftime("%H:%M:%S")
            print("ERRO DICFM001 :", hora_formatada)
            continue

    time.sleep(int(tempo_tela))

    pyautogui.screenshot(imagem_tela)
    cor_procurada = (44, 146, 36)
    posicao_cor = procurar_cor_na_imagem(imagem_tela, cor_procurada)
    if posicao_cor is not None:
        print("A cor foi encontrada na posição:", posicao_cor)
        pyautogui.click(posicao_cor[0], posicao_cor[1])
        
    else: 
         nome_processo = "ua-client.exe"
         if verificar_processo(nome_processo):
            fechar_processo(nome_processo)
            agora = datetime.now()
            hora_formatada = agora.strftime("%H:%M:%S")
            print("ERRO DICFM001 - TELA 2 :", hora_formatada)
            
            continue        

    time.sleep(int(tempo_relatorio))
    #script_path = '.\Mesclar View.py'
    #subprocess.run(['python', script_path])  



    time.sleep(int(tempo_validacao))

#ACD2F6
#EF9F3F
#2C9224
