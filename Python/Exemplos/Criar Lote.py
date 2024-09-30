import pyautogui
import time
numero = input("Quantidade de Lotes:")

time.sleep(3)
for i in range(1, int(numero)+1):
    print(i)
    pyautogui.press('tab')
    time.sleep(0.5)
    pyautogui.press('F2')