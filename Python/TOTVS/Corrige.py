import csv
import pyautogui
import time
import pyperclip

with open('C:\\config\\COLETOR.CSV', mode='r', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter=';')
    next(reader)
    time.sleep(3)
    for row in reader: 
        pyautogui.press('tab') 
        pyautogui.write(row[1])
        print(row[1])
        time.sleep(1)
        pyautogui.press('tab')
        time.sleep(1)        
        pyautogui.hotkey('alt','a')
        time.sleep(1.5)
        pyautogui.press('s')
        time.sleep(1)
        pyautogui.press('F2')
        time.sleep(1) 


