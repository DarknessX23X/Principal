import pyautogui
import pygetwindow as gw
import time

time.sleep(3)
for _ in range(181):
    pyautogui.hotkey('shift','tab')
    pyautogui.hotkey('shift','tab')
    pyautogui.press('backspace',presses=10)
    pyautogui.typewrite('10/06/2024')
    pyautogui.press('tab',presses=2)
    pyautogui.press('F12')
    time.sleep(1) 
    pyautogui.hotkey('shift','tab') 
    pyautogui.press('tab',presses=2)
    pyautogui.press('E')
    pyautogui.press('tab',presses=5)
    pyautogui.typewrite('001')
    pyautogui.press('tab',presses=2)
    pyautogui.press('F4')
    pyautogui.press('F12')
    pyautogui.press('tab',presses=3)
    pyautogui.typewrite('TRANSACAO INDEVIDA')
    pyautogui.hotkey('alt','c',interval=2)
    time.sleep(2)
    pyautogui.press('S')
    time.sleep(2)
    pyautogui.press('enter')
    print(_)

#'1013865'
#'1014176'