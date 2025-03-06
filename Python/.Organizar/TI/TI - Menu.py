import tkinter as tk
import subprocess

def open_program():
    try:
        subprocess.run("C:\\Program Files\\uvnc bvba\\UltraVNC\\vncviewer.exe")  # Substitua "nome_do_programa" pelo nome do programa que você deseja abrir
    except FileNotFoundError:
        print("O programa especificado não foi encontrado.")

def button_click():
    label.config(text="Botão clicado!")
    open_program()
window = tk.Tk()

label = tk.Label(window, text="Olá, mundo!")
label.pack()

button = tk.Button(window, text="Clique aqui!", command=button_click)
button.pack()

window.mainloop()