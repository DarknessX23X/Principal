import tkinter as tk
from tkinter import ttk

# Função para exibir o tooltip com contador regressivo
def show_tooltip(event):
    x = event.x_root
    y = event.y_root

    tooltip = tk.Toplevel(root)
    tooltip.wm_overrideredirect(True)
    tooltip.wm_geometry(f"+{x}+{y}")

    label = ttk.Label(tooltip, text="100")
    label.pack()

    # Função para atualizar o contador regressivo
    def update_counter(value):
        label.config(text=str(value))
        if value > 0:
            tooltip.after(1000, update_counter, value - 1)
        else:
            tooltip.destroy()
    
    # Inicia o contador regressivo
    update_counter(100)

# Cria a janela principal
root = tk.Tk()

# Associa o evento de passar o mouse sobre a janela à função que exibe o tooltip
root.bind("<Enter>", show_tooltip)

# Inicia o loop principal da janela
root.mainloop()