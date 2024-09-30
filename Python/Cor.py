from PIL import Image
import pyautogui

def procurar_cor_na_imagem(imagem, cor):
    # Abrir a imagem
    img = Image.open(imagem)

    # Converter a imagem para o modo RGB
    img_rgb = img.convert("RGB")

    # Obter as dimensões da imagem
    largura, altura = img_rgb.size

    # Percorrer todos os pixels da imagem
    for x in range(largura):
        for y in range(altura):
            # Obter a cor do pixel na posição (x, y)
            pixel = img_rgb.getpixel((x, y))

            # Verificar se a cor do pixel corresponde à cor procurada
            if pixel == cor:
                return (x, y)  # Retornar a posição do pixel

    return None  # Retornar None se a cor não for encontrada

# Tirar um print da tela e salvar como imagem
imagem_tela = "screenshot.png"
#pyautogui.screenshot(imagem_tela)

# Definir a cor a ser procurada (no formato RGB)
cor_procurada = (192, 192, 192)

# Procurar a cor na imagem
posicao_cor = procurar_cor_na_imagem(imagem_tela, cor_procurada)

if posicao_cor is not None:
    print("A cor foi encontrada na posição:", posicao_cor)
else:
    print("A cor não foi encontrada na imagem.")