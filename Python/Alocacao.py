import psutil
import os
import pyautogui
from PIL import Image
import time
import csv
import numpy as np
import clipboard
import cv2




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

def abrir_atalho(nome_atalho):
    caminho_area_trabalho = os.path.expandvars('%USERPROFILE%\\Desktop')
    caminho_completo = os.path.join(caminho_area_trabalho, nome_atalho)
    print(caminho_completo)
    os.startfile(caminho_completo)

with open('Alocacao.csv', 'r') as file:
    csv_reader = csv.reader(file, delimiter=";")
    
    # Pular o cabeçalho
    next(csv_reader)
    
    # Criar listas vazias para armazenar os valores das colunas 2, 3 e 6
    coluna2 = []
    coluna3 = []
    coluna6 = []
    
    # Iterar sobre as linhas do arquivo CSV
    for linha in csv_reader:
        # Obter os valores das colunas 2, 3 e 6
        valor_coluna2 = linha[1]
        valor_coluna3 = linha[2]
        valor_coluna6 = linha[5]
        
        # Adicionar os valores nas respectivas listas
        coluna2.append(valor_coluna2)
        coluna3.append(valor_coluna3)
        coluna6.append(valor_coluna6)

# Imprimir as listas com os valores das colunas 2, 3 e 6
OP=coluna2[0]
SKU=coluna3[0]
QTDE=coluna6[0]
#print("OP:", OP)
#print("SKU:", SKU)
#print("Quantidade:", QTDE)

print(len(coluna2))

nome_atalho = "Treino.lnk"
nome_processo = "ua-client.exe"
if verificar_processo(nome_processo):
    fechar_processo(nome_processo)

abrir_atalho(nome_atalho)
while True:
        imagem_tela = ".\\Rotinas\\screenshot\\screenshot.png"
        pyautogui.screenshot(imagem_tela)
        cor_procurada = (55, 42, 31)
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
        imagem_tela = ".\\Rotinas\\screenshot\\screenshot1.png"
        pyautogui.screenshot(imagem_tela)
        cor_procurada = (234, 155, 62)
        posicao_cor = procurar_cor_na_imagem(imagem_tela, cor_procurada)
        if posicao_cor is None:            
            continue
        else:            
            pyautogui.press('esc')     
            break

time.sleep(1)
pyautogui.hotkey('alt', 'O')
pyautogui.press('C')
while True:
        imagem_tela = ".\\Rotinas\\screenshot\\screenshot2.png"
        pyautogui.screenshot(imagem_tela)
        cor_procurada = (199, 249, 254)
        posicao_cor = procurar_cor_na_imagem(imagem_tela, cor_procurada)
        if posicao_cor is None:
            continue
        else:     
            break
    
pyautogui.write('CDFFM163',interval=0.1)
pyautogui.press('F12')
while True:
        imagem_tela = ".\\Rotinas\\screenshot\\screenshot3.png"
        pyautogui.screenshot(imagem_tela)
        cor_procurada = (255, 255, 230)
        posicao_cor = procurar_cor_na_imagem(imagem_tela, cor_procurada)
        if posicao_cor is None:
            continue
        else:     
            break 

pyautogui.press("tab",presses=2)
pyautogui.hotkey('alt', 'V')
pyautogui.write(SKU,interval=0.1)
pyautogui.press("tab",presses=2)
pyautogui.write("110000001",interval=0.1)   
pyautogui.press("tab",presses=3)
pyautogui.write("2917",interval=0.1)  
pyautogui.press("tab",presses=3)
pyautogui.press("space")
pyautogui.press("F4")

img_rgb = cv2.imread(".\\Rotinas\\screenshot\\screenshot4.png")
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread(".\\Rotinas\\screenshot\\botao.png", 0)
w, h = template.shape[::-1]
res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where(res >= threshold)
posicoes_x = []
posicoes_y = []

# Capture as coordenadas X e Y dos retângulos encontrados
for pt in zip(*loc[::-1]):
    posicoes_x.append(pt[0] + w // 2)
    posicoes_y.append(pt[1] + h // 2)

# Exiba as coordenadas X e Y
for i in range(len(posicoes_x)):
    print(f'Posição {i+1}: X={posicoes_x[i]}, Y={posicoes_y[i]}')

# Desenhe retângulos ao redor das correspondências encontradas
centros_x = []
centros_y = []
for pt in zip(*loc[::-1]):
    x = pt[0] + w // 2
    y = pt[1] + h // 2
    centros_x.append(x)
    centros_y.append(y)
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 2)
    cv2.circle(img_rgb, (x, y), 5, (255, 0, 0), -1)



# Salve a imagem com os retângulos
cv2.imwrite('.\\Rotinas\\screenshot\\imagem_saida.png', img_rgb)

for i in range(len(centros_x)):
    #print(f'Centro {i+1}: X={centros_x[i]}, Y={centros_y[i]}')
    time.sleep(7)
    pyautogui.doubleClick(centros_x[i],301)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)

qtderestante = clipboard.paste()
#print(conteudo)
qtderestante = qtderestante.replace(",", ".")
qtdemax = 0
qtdealoc = sum(int(item) for item in coluna6)
qtdedif = 0
qtderest = 1 
#print(qtdealoc)

while qtderest != 0:
       pyautogui.doubleClick(centros_x[i],301)
       pyautogui.hotkey('ctrl', 'c')
       time.sleep(1)
       qtderestante = clipboard.paste()
       qtdealoc = int(float(qtdealoc)) - int(float(qtderestante))
       qtderest = qtderestante.replace(".", ",") 
       pyautogui.hotkey('alt', 'A')
       time.sleep(7)
       pyautogui.press('tab')      
       pyautogui.write(coluna2[i],interval=0.1)
       pyautogui.press('tab')
       pyautogui.write(qtderest,interval=0.1)
       pyautogui.press('tab',presses=2)
       pyautogui.press('F3')
       time.sleep(5)
       pyautogui.press('esc')
       time.sleep(3)
i = i +1     




