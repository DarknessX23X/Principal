import pyautogui
import time
import pandas as pd
import os
import pyperclip

# Carrega somente as 10 primeiras linhas do arquivo 'NOTAS.csv'
df = pd.read_csv('C:\\CONFIG\\BI\\NOTAS.csv', delimiter=';', nrows=300)
time.sleep(5)

df_filtrado = df[df['Dt. Emissao'] == '01/12/2022']

df['Ds. Chaveacesso'] = df['Ds. Chaveacesso'].astype(str)
concatenacao = '·;'.join(df['Ds. Chaveacesso'])

# Imprime o valor resultante da concatenação
print(concatenacao)

# Copia a concatenação para a área de transferência
pyperclip.copy(concatenacao)
'''
for index, row in df.iterrows():
    nome_arquivo = "X:\\TI\\Danfe\\"+row[2]+".pdf"
    if os.path.exists(nome_arquivo):
        #print(row[2])
        continue
    print(str(index) +'-'+row[2])
    pyautogui.press('F2')
    pyautogui.press('tab',11)
    time.sleep(2)
    pyautogui.typewrite(row[2]) 
    time.sleep(2)
    pyautogui.press('F4')    
    pyautogui.press('left')
    pyautogui.press('space')
    pyautogui.hotkey('alt','r')
    time.sleep(3)
    pyautogui.click(64,36)  
    time.sleep(2)
    pyautogui.press('F')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.typewrite("X:\\TI\\Danfe\\"+row[2]+".pdf")
    time.sleep(1) 
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.click(574,43)
    time.sleep(3) 
'''
 
