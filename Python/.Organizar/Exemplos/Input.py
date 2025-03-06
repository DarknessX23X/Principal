from tkinter import *
import psutil
import os
import tkinter.messagebox as messagebox
import time
import pyautogui
from PIL import Image

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

def retrieve_input(event=None):
    input_value = textBox.get()
    input_array.append(input_value)
    textBox.delete(0, "end")

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

def continue_code(event=None):
    with open("array.txt", "w") as file:
        for item in input_array:
            file.write(item + "\n")
    root.destroy()
    print(input_array)
    nome_processo = "ua-client.exe"
    if verificar_processo(nome_processo):
        fechar_processo(nome_processo)

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
    
    pyautogui.write('CMCFP019',interval=0.1)
    pyautogui.press('F12')

    while True:
        imagem_tela = "screenshot3.png"
        pyautogui.screenshot(imagem_tela)
        cor_procurada = (255, 255, 224)
        posicao_cor = procurar_cor_na_imagem(imagem_tela, cor_procurada)
        if posicao_cor is None:
            continue
        else:     
            break
    
    pyautogui.press('enter')    
    for caractere in input_array:
        pyautogui.press('tab',presses=5)
        time.sleep(1)
        pyautogui.typewrite(caractere)
        pyautogui.press('tab')
        pyautogui.hotkey('alt', 'o')
        pyautogui.hotkey('F4')
        while True:
            imagem_tela = "screenshot4.png"
            pyautogui.screenshot(imagem_tela)
            cor_procurada = (239, 159, 63)
            posicao_cor = procurar_cor_na_imagem(imagem_tela, cor_procurada)
            if posicao_cor is None:
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
                pyautogui.press('enter')
                break
            else:     
                pyautogui.press('esc')
                pyautogui.press('F2')
                pyautogui.press('enter')
                break
                     

root = Tk()

# Set window title
root.title("TOTVS - Requisições")

# Set window icon
root.iconbitmap("X:\\TI\\Giovane\\Automações\\Exemplos\\favicon.ico")

# Get screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate position
x = (screen_width / 2) - (200 / 2)
y = (screen_height / 2) - (100 / 2)

root.geometry('%dx%d+%d+%d' % (225, 75, x, y))

root.resizable(False, False)

label = Label(root, text="Requisições:")
label.grid(row=0, column=0, padx=5, pady=5)


textBox = Entry(root, width=15)
textBox.grid(row=0, column=1, padx=5, pady=5)
textBox.bind('<space>', retrieve_input)
root.bind('<Return>', continue_code)

#buttonOK = Button(root, height=1, width=10, text="OK", 
 #                   command=retrieve_input)
#buttonOK.grid(row=1, column=0, padx=15, pady=5)

buttonCancel = Button(root, height=1, width=10, text="Encerrar", 
                    command=continue_code)
buttonCancel.grid(row=1, column=1, padx=15, pady=5)

input_array = []

textBox.focus_set()

mainloop()