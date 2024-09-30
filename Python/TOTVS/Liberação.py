from tkinter import Tk, StringVar, OptionMenu, Label, Button, ttk,Radiobutton,messagebox
import pandas as pd

def autocompletar(event):
    entrada = codigo_var.get()
    if entrada:
        possibilidades = []
        for item in itens_coluna5:
            if item.startswith(entrada):
                possibilidades.append(item)
        codigo_dropdown['values'] = possibilidades
    else:
        codigo_dropdown['values'] = itens_coluna5

def autocompletar2(event):
    entrada = telas_var.get()
    if entrada:
        possibilidades = []
        for item in itens_coluna2:
            if item.startswith(entrada):
                possibilidades.append(item)
        telas_dropdown['values'] = possibilidades
    else:
        telas_dropdown['values'] = itens_coluna2


def filtrar_dados():
    codigo_usuario = codigo_var.get()
    telas_usuario = telas_var.get()
    opcao_selecionada = opcoes_var.get()

    df = pd.read_csv(filename, encoding='latin1', delimiter=';')

    if opcao_selecionada == "grupo" :
       df['Nome'] = df['Nome'].astype(str)
       dados_filtrados = df[df['Nome'] == codigo_usuario].iloc[:, :6]

    if opcao_selecionada == "telas" :
       df['Componente'] = df['Componente'].astype(str)
       dados_filtrados = df[df['Componente'] == telas_usuario].iloc[:, :6]   

    treeview.delete(*treeview.get_children())

    for index, row in dados_filtrados.iterrows():
        treeview.insert('', 'end', values=row.tolist())

  
    #messagebox.showinfo("Opção Selecionada", f"Você selecionou: {opcao_selecionada}")
    

root = Tk()
root.title("Liberação")

filename = 'C:\\config\\Liberacao.CSV'
df = pd.read_csv(filename, encoding='latin1', delimiter=';')
itens_coluna5 = sorted(df.iloc[:, 5].drop_duplicates().tolist())
itens_coluna2 = sorted(df.iloc[:, 2].drop_duplicates().tolist())


grupo_label = Label(root, text="Grupo")
grupo_label.grid(row=0, column=0, padx=0, pady=10)

codigo_var = StringVar(root)
codigo_var.set(itens_coluna5[0])

telas_var = StringVar(root)
telas_var.set(itens_coluna2[0])

codigo_dropdown = ttk.Combobox(root, textvariable=itens_coluna5)
codigo_dropdown['values'] = itens_coluna5
codigo_dropdown.bind('<KeyRelease>', autocompletar)
codigo_dropdown.config(width=30)
codigo_dropdown.grid(row=1, column=0, padx=0, pady=10)
#codigo_dropdown.pack()

filtrar_button = Button(root, text="Filtrar", command=filtrar_dados)
filtrar_button.grid(row=2, column=0, padx=10, pady=10)

telas_label = Label(root, text="Telas")
telas_label.grid(row=0, column=1, padx=0, pady=10)

telas_dropdown = ttk.Combobox(root, textvariable=itens_coluna2)
telas_dropdown['values'] = itens_coluna2
telas_dropdown.bind('<KeyRelease>', autocompletar2)
telas_dropdown.config(width=30)
telas_dropdown.grid(row=1, column=1, padx=0, pady=10)

opcoes_var = StringVar()
opcoes_var.set(None)  # Opção inicial vazia

opcoes_frame = ttk.Frame(root)
opcoes_frame.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

opcao1 = Radiobutton(opcoes_frame, text="Grupo", variable=opcoes_var, value="grupo")
opcao1.pack(side="left", padx=10)

opcao2 = Radiobutton(opcoes_frame, text="Telas", variable=opcoes_var, value="telas")
opcao2.pack(side="left", padx=10)

opcao3 = Radiobutton(opcoes_frame, text="Usuarios", variable=opcoes_var, value="usuarios")
opcao3.pack(side="left", padx=10)


frame = ttk.Frame(root)
frame.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

treeview = ttk.Treeview(frame, columns=list(df.columns[:6]), show='headings')

for col in df.columns[:6]:
    treeview.heading(col, text=col)

treeview.pack(side='left', fill='both')

scrollbar = ttk.Scrollbar(frame, orient='vertical', command=treeview.yview)
scrollbar.pack(side='right', fill='y')

treeview.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=treeview.yview)


root.mainloop()