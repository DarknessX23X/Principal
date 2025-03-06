import keyboard

while True:
    if keyboard.is_pressed('space'):
        keyboard.press('down')
        keyboard.release('down')