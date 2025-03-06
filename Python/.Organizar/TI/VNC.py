import vncdotool

# Conexão ao servidor VNC
vnc = vncdotool.VNCSession('192.168.0.142', '5900')

# Movendo o mouse e clicando
vnc.move(100, 100)
vnc.click()

# Pressionando a tecla 'a'
vnc.keyPress('a')

# Capturando uma screenshot
vnc.captureScreen('<nome_do_arquivo>.png')

# Fechando a conexão
vnc.close()