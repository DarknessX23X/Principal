import pyautogui
import time
import pandas as pd
import os
import pyperclip

df = pd.read_csv('C:\\CONFIG\\BI\\LIB.csv', delimiter=';')
#time.sleep(5)

numero_empresa = input("Digite o número da empresa: ")
time.sleep(5)

for index, row in df.iterrows():
    pyautogui.press('F5')
    pyautogui.typewrite(str(row[0]))
    time.sleep(1)
    pyautogui.typewrite(numero_empresa)

pyautogui.hotkey('Alt','A')   
time.sleep(1)
pyautogui.press('S')   

    

    