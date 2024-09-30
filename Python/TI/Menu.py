import curses
import os
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options



def set_window_size(rows, columns):
    if sys.platform.startswith('win'):
        os.system('mode con: cols={} lines={}'.format(columns, rows))
    else:
        os.system('stty cols {} rows {}'.format(columns, rows))

def set_window_title(title):
    sys.stdout.write("\x1b]2;{}\x07".format(title))
    sys.stdout.flush()

def main(stdscr):
    # Configurações iniciais
    sys.stdout = open(sys.stdout.fileno(), 'w', encoding='utf-8', closefd=False)
    curses.curs_set(0)  # Oculta o cursor
    stdscr.nodelay(True)  # Torna a leitura de entrada não bloqueante

    # Define o tamanho desejado da janela
    height, width = 10, 30
    stdscr.resize(height, width)

    # Lista de opções do menu
    menu_options = ["Firewall", "Roteador", "Opção 3", "Opção 4", "Sair"]
    current_option = 0
    set_window_title("TI - KAZZO")
    #set_window_size(30, 10)
    # Loop principal
    while True:
        # Lê a entrada do usuário
        key = stdscr.getch()

        

        # Verifica se o usuário pressionou a tecla ESC para sair
        if key == 27:
            break

        # Verifica se o usuário pressionou a tecla para cima
        elif key == curses.KEY_UP:
            current_option = (current_option - 1) % len(menu_options)

        # Verifica se o usuário pressionou a tecla para baixo
        elif key == curses.KEY_DOWN:
            current_option = (current_option + 1) % len(menu_options)

        # Verifica se o usuário pressionou Enter na opção 1
        elif key == 10 and current_option == 0:
            stdscr.clear()
            stdscr.addstr(0, 0, "Abrindo o atalho do programa...")
            stdscr.refresh()
            chrome_options = Options()
            chrome_options.add_argument("--start-maximized")
            driver = webdriver.Chrome(chrome_options)
            driver.get('http://192.168.0.1:14000/')
            elemento = driver.find_element("name","usernamefld")
            elemento.send_keys("giovane.adm")
            elemento = driver.find_element("name","passwordfld")
            elemento.send_keys("DarknessX23X")
            elemento.send_keys(Keys.RETURN)
            driver.get("http://192.168.0.1:14000/services_dhcp.php")
            elemento = driver.find_elements(By.TAG_NAME,"td")

        
        
        
        stdscr.clear()

        # Exibe as opções do menu
        for i, option in enumerate(menu_options):
            start_x = width // 2 - len(option) // 2
            x = (width - len(option)) // 2
            y = height // 2 - len(menu_options) // 2 + i
            if i == current_option:
                stdscr.addstr(y, x, option, curses.A_REVERSE)
            else:
                stdscr.addstr(y, x, option)

        # Atualiza a tela
        stdscr.refresh()

# Inicia o programa

curses.wrapper(main)