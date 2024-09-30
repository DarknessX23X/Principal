import pygetwindow as gw
from screeninfo import get_monitors
import subprocess
import time

def close_process_by_window_name(window_name):
    # Obter a janela pelo nome
    window = gw.getWindowsWithTitle(window_name)

    # Verificar se a janela foi encontrada
    if len(window) == 0:
        print("Janela não encontrada!")
        return

    # Fechar o processo da janela
    window[0].close()

def open_shortcut_on_monitor(shortcut_path, monitor_number):
    # Obter a lista de monitores conectados
    monitors = get_monitors()

    # Verificar se o número do monitor fornecido é válido
    if monitor_number < 1 or monitor_number > len(monitors):
        print("Número de monitor inválido!")
        return

    # Obter as informações do monitor desejado
    monitor = monitors[monitor_number - 1]
    x = monitor.x
    y = monitor.y
    width = monitor.width
    height = monitor.height

    # Abrir o atalho usando o comando subprocess
    subprocess.Popen([shortcut_path], shell=True)

    # Aguardar um segundo para a janela do atalho abrir
    time.sleep(1)

    # Obter a janela mais recente (a janela do atalho)
    shortcut_window = gw.getWindowsWithTitle('GIGA VMS')[0]

    # Mover a janela do atalho para as coordenadas corretas
    shortcut_window.moveTo(x, y)
    shortcut_window.resizeTo(width, height)

# Exemplo de uso: abrir o atalho no segundo monitor
shortcut_path = 'C:\\Config\\TV3.lnk'
monitor_number = 3
open_shortcut_on_monitor(shortcut_path, monitor_number)

# Exemplo de uso: fechar o processo da janela com o nome "Nome da Janela"
window_name = "Mensagens do Sandboxie"
close_process_by_window_name(window_name)