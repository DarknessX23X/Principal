from pynput.mouse import Listener

def on_click(x, y, button, pressed):
    if pressed:
        print(f'Posição do mouse: X={x}, Y={y}')

# Crie uma instância do Listener
listener = Listener(on_click=on_click)

# Inicie o Listener
listener.start()

# Aguarde pressionar 'q' para parar o Listener
listener.join()