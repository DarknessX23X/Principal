import curses
import os
import time

def criar_usuario(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "Criando usuário...")
    stdscr.addstr(1, 0, "Digite o nome de usuário: ")
    stdscr.refresh()

    curses.echo()  # Habilita a exibição da entrada do usuário
    nome_usuario = stdscr.getstr(1, 20, 20).decode() # Lê até 20 caracteres, a partir da posição (1,20)
    curses.noecho() # Desabilita a exibição da entrada do usuário

    stdscr.addstr(2, 0, f"Nome de usuário: {nome_usuario}")
    stdscr.refresh()
    time.sleep(1)

def liberar_acesso():
    # Implemente a lógica para liberar acesso aqui...
    print("Liberando acesso...")

def alterar_senha():
    # Implemente a lógica para alterar a senha aqui...
    print("Alterando senha...")

def sair():
    pass #Função vazia para sair


def main(stdscr):
    # Inicializa cores (opcional, mas melhora a aparência)
    os.system('mode con: cols=20 lines=6') #Ajustar o tamanho da janela do terminal
    os.system('title Kazzo')
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    # Define as opções do menu e suas funções correspondentes
    options = [
        ("1. Criar Usuário", criar_usuario),
        ("2. Liberar Acesso", liberar_acesso),
        ("3. Alterar Senha", alterar_senha),
        ("4. Sair", sair)
    ]

    # Variáveis de estado
    current_option = 0
    selected = False

    while not selected:
        stdscr.clear()  # Limpa a tela a cada iteração
        stdscr.addstr(0, 1, "   TI - KAZZO")  # Título do menu

        for i, (option_text, _) in enumerate(options):  #Usa apenas o texto da opção para desenhar
            attr = curses.color_pair(1) if i == current_option else curses.A_NORMAL
            stdscr.addstr(i + 1, 1, option_text, attr)

        stdscr.refresh()
        key = stdscr.getch()

        if key == curses.KEY_UP and current_option > 0:
            current_option -= 1
        elif key == curses.KEY_DOWN and current_option < len(options) - 1:
            current_option += 1
        elif key == ord('\n'):
            selected = True
        elif key == ord('q'):
            selected = True
            current_option = len(options) - 1

   # Ação com base na opção selecionada
    if current_option < len(options) -1:
        options[current_option][1](stdscr) # Chama a função associada à opção selecionada
        stdscr.getch() #Aguarda uma tecla para continuar


if __name__ == "__main__":
    curses.wrapper(main)