import csv
import pyautogui
import time
import pyperclip

# Substitua 'seu_arquivo.csv' pelo caminho do seu arquivo
with open('C:\\config\\OPS.CSV', mode='r', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter=';')
    time.sleep(1)
    pyautogui.click(123,146)
    next(reader)                    
    # Exibir as linhas do arquivo
    for row in reader:        
        pyautogui.press('tab')
        pyautogui.write(row[2])
        pyautogui.press('tab')
        time.sleep(0.5)
        pyautogui.click(334,433,clicks=2)
        pyautogui.click(617,433,clicks=2)
        pyautogui.click(477,433,clicks=2)
        pyautogui.click(477,451,clicks=2)         
        time.sleep(2.5)
        pyautogui.click(954,554)        
        time.sleep(0.5)
        pyautogui.press('down')
        time.sleep(0.5)
        pyautogui.press('enter')
        time.sleep(0.5)
        pyautogui.press('tab')  
        time.sleep(0.5) 
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(1)
        sku =""  
        print(row[2] + ' - ' + row[4] + ' - ' + row[5])      
        while sku != row[4]:
            #print(row[4])
            time.sleep(0.25) 
            pyautogui.hotkey('ctrl', 'c')
            time.sleep(1)
            try:
                sku = pyperclip.paste()
            except:
                sku = pyperclip.paste()
            #print(sku)
            if sku != row[4]:                
                pyautogui.press('tab',presses=5)
        time.sleep(0.5)
        pyautogui.press('tab',presses=4)
        time.sleep(0.5)
        pyautogui.press('0')
        time.sleep(0.5)
        pyautogui.press('tab')
        time.sleep(0.5)
        pyautogui.hotkey('alt','o')
        time.sleep(2)
        pyautogui.press('F3')
        time.sleep(2)
        pyautogui.press('F2')            
        

