import keyboard

def on_key_press(event):
    if event.name == 'enter' and keyboard.is_pressed('ctrl'):
        print("Combinação de teclas Ctrl + Enter pressionada!")
        keyboard.unhook_all()  # Para a detecção de teclas
        gerar_arquivo(lista_texto)

def gerar_arquivo(lista):
    with open("texto.txt", "w") as arquivo:
        for item in lista:
            arquivo.write(item + "\n")
    print("Arquivo gerado com sucesso!")

keyboard.on_press(on_key_press)

lista_texto = []

while True:
    texto = input("Digite algo (ou pressione Enter para parar): ")
    if texto == "":
        break
    lista_texto.append(texto)

keyboard.wait()