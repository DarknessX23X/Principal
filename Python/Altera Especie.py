import time
import pyautogui

time.sleep(3)

with open('C:\\config\\linhas.txt', 'r') as arquivo:
    # Inicializa o contador de linha
    numero_linha = 1

    # Itera sobre as linhas do arquivo
    for linha in arquivo:
        # Remove quebras de linha e espaços em branco
        linha = linha.strip()
        pyautogui.hotkey('Alt','C')
        pyautogui.hotkey('Alt','V')
        pyautogui.write(linha)
        pyautogui.press('tab')
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.click(82,512)
        pyautogui.press('backspace',2)
        pyautogui.write('CN')
        pyautogui.press('tab')
        pyautogui.press('F3')
        time.sleep(1)
        pyautogui.press('F2')        
        # Imprime o número da linha e seu valor
        print(f"Linha {numero_linha}: {linha}")        
        # Incrementa o contador de linha
        numero_linha += 1