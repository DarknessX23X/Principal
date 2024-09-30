import csv
import pyautogui
import time
import pyperclip
from datetime import datetime, timedelta

caminho_text = 'c:\\config\\arquivo.txt'

# Caminho do arquivo CSV
caminho_arquivo = 'C:\\CONFIG\\PEDIDOS.csv'

with open(caminho_arquivo, newline='') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv,delimiter=';')    
    time.sleep(5)
    for linha in leitor_csv:            
            pyautogui.typewrite(linha[0])
            time.sleep(0.75)
            pyautogui.press('tab')
            time.sleep(0.75)
            pyautogui.press('tab')            
            pyautogui.click(164, 290,button='right')
            pyautogui.typewrite('001')
            time.sleep(0.75)
            pyautogui.press('tab')            
            time.sleep(0.75)
            pyautogui.press('tab')
            time.sleep(0.75)           
            pyautogui.hotkey('shift','tab')
            time.sleep(0.75)
            pyautogui.hotkey('ctrl','c')
            novopedido = pyperclip.paste()
            time.sleep(0.75)
            pyautogui.press('tab')
            pyautogui.typewrite(linha[2])
            time.sleep(0.75)
            pyautogui.press('tab')
            pyautogui.typewrite('110000050')
            time.sleep(0.75)
            pyautogui.click(148, 367)
            pyautogui.typewrite(linha[1])
            time.sleep(0.75)
            pyautogui.press('tab')
            pyautogui.typewrite(linha[3])
            time.sleep(0.75)
            pyautogui.press('tab',presses=2)
            data_string = linha[3]
            data_formatada = datetime.strptime(data_string, '%d/%m/%Y')  # Converte a string para objeto datetime
            data_final = data_formatada + timedelta(days=7)
            data_final_formatada = data_final.strftime('%d/%m/%Y')
            pyautogui.typewrite(data_final_formatada)
            with open(caminho_text, 'a') as arquivo_txt:
                linha = linha[0]+';'+ novopedido   # Conteúdo a ser adicionado ao arquivo
                arquivo_txt.write(linha)        
            pyautogui.hotkey('alt','D')
            time.sleep(1)
            pyautogui.press('S')
            time.sleep(10)
            pyautogui.press('enter')
            time.sleep(1)
        #print(linha[0])  # Imprime a segunda coluna, considerando que a indexação começa em 0
