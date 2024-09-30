import csv
import pyautogui
import time
import pyperclip
import keyboard
import sys

# Abre o arquivo CSV em modo de leitura
time.sleep(3)
with open('./Faturas.csv', 'r') as file:
    # Cria um leitor de CSV
    csv_reader = csv.reader(file, delimiter=';')
    # Itera sobre as linhas do arquivo e imprime cada item
    for row in csv_reader:        
        pyautogui.press('tab') 
        pyautogui.write(row[1])
        pyautogui.press('tab',presses=1)
        pyautogui.write(row[3])
        pyautogui.press('tab',presses=3)        
        pyautogui.press('F')
        pyautogui.press('F4')
        pyautogui.press('tab')
        pyautogui.click(541,306,button='right') 
        pyautogui.hotkey('Ctrl','C')
        valor = pyperclip.paste()
        time.sleep(1)
        pyautogui.click(452,306,button='right') 
        pyautogui.hotkey('Ctrl','C')
        data = pyperclip.paste()
        time.sleep(1)
        pyautogui.click(99,306,button='right') 
        pyautogui.hotkey('Ctrl','C')
        fatura = pyperclip.paste()
        pyautogui.click(768,306)
        pyautogui.hotkey('Alt','E')
        time.sleep(1) 
        pyautogui.press('S')      
        time.sleep(1) 
        pyautogui.write(valor)
            #pyautogui.write(row[4])
        pyautogui.press('tab') 
        pyautogui.press('F')
        pyautogui.press('tab') 
        pyautogui.write(fatura)
        pyautogui.press('tab')
        pyautogui.write(data)
        pyautogui.hotkey('Alt','o')
        time.sleep(2)
        pyautogui.press('enter')
        
        