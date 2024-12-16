import csv
import re
import tkinter as tk
from tkinter import filedialog

def abrir_arquivo():
    """Abre uma caixa de diálogo para o usuário selecionar um arquivo."""
    global nome_do_arquivo
    nome_do_arquivo = filedialog.askopenfilename(
        initialdir="/",
        title="Selecione o arquivo CSV",
        filetypes=(("Arquivos CSV", "*.csv"), ("Todos os arquivos", "*.*"))
    )
    if nome_do_arquivo:
        processar_arquivo()

def escolher_pasta():
    """Abre uma caixa de diálogo para o usuário escolher uma pasta."""
    global pasta_destino
    pasta_destino = filedialog.askdirectory(
        initialdir="/",
        title="Selecione a pasta de destino"
    )
    if pasta_destino:
        print(f"Pasta de destino selecionada: {pasta_destino}")

def processar_arquivo():
    """Processa o arquivo CSV selecionado."""
    global contador_quantidade, contagem_por_cnpj, numeros_exportados

    contador_quantidade = 0
    contagem_por_cnpj = {}
    numeros_exportados = set()

    with open(nome_do_arquivo, 'r', encoding='latin-1') as arquivo:
        leitor = csv.reader(arquivo, delimiter=';')
        for row in leitor:
            if any(row):  # Verifica se a linha possui algum elemento não vazio
                cnpj = row[0]  # Obtém o CNPJ da primeira coluna
                if 'Quantidade' in ''.join(row):  # Verifica se a palavra 'quantidade' está presente na linha
                    contador_quantidade += 1
                    #print(row[8])
                    numeros = re.findall(r"produto:\s*(\d+)", row[8])
                    numeros1 = re.findall(r"produto\s*(\d+)", row[8])
                    
                    if numeros:
                        numero = numeros[0]
                        if cnpj in contagem_por_cnpj:
                            if numero in contagem_por_cnpj[cnpj]:
                                contagem_por_cnpj[cnpj][numero] += 1
                            else:
                                contagem_por_cnpj[cnpj][numero] = 1
                        else:
                            contagem_por_cnpj[cnpj] = {numero: 1}
                    elif numeros1:
                        numero = numeros1[0]
                        if cnpj in contagem_por_cnpj:
                            if numero in contagem_por_cnpj[cnpj]:
                                contagem_por_cnpj[cnpj][numero] += 1
                            else:
                                contagem_por_cnpj[cnpj][numero] = 1
                        else:
                            contagem_por_cnpj[cnpj] = {numero: 1}
                elif 'Item/Produto' in ''.join(row):
                    numeros3 = re.findall(r"(\d+)\s*da N\.F\.", row[8])
                    nome_arquivo_csv = f"{pasta_destino}/Divergentes.csv"
                    if numeros3:
                        for numero in numeros3:
                            if numero not in numeros_exportados:
                                with open(nome_arquivo_csv, 'a', encoding='latin-1', newline='') as arquivo_csv:
                                    escritor_csv = csv.writer(arquivo_csv, delimiter=';')
                                    escritor_csv.writerow([numero])
                                numeros_exportados.add(numero)  # Adiciona o número ao conjunto de números exportados

    # Exportar os CNPJs para dois arquivos CSV delimitados por vírgula
    for i, (cnpj, contagem) in enumerate(contagem_por_cnpj.items()):    
        if cnpj == '09041289000161':
            nome_arquivo_csv = f"{pasta_destino}/Ajuste 14.csv"
        else:
            nome_arquivo_csv = f"{pasta_destino}/Ajuste 79.csv"    
        with open(nome_arquivo_csv, 'w', encoding='latin-1', newline='') as arquivo_csv:
            escritor_csv = csv.writer(arquivo_csv, delimiter=',')
            #escritor_csv.writerow(["Número", "Quantidade"])
            for numero, quantidade in contagem.items():
                escritor_csv.writerow([numero, quantidade])

    print(f"O contador de linhas com 'quantidade' é: {contador_quantidade}")

# Cria a janela principal do Tkinter
janela = tk.Tk()
janela.title("Selecionar Arquivo CSV")

# Cria o botão "Abrir Arquivo"
botao_abrir = tk.Button(janela, text="Abrir Arquivo", command=abrir_arquivo)
botao_abrir.pack(pady=10)

# Cria o botão "Escolher Pasta"
botao_pasta = tk.Button(janela, text="Escolher Pasta", command=escolher_pasta)
botao_pasta.pack(pady=10)

# Inicia o loop principal do Tkinter
janela.mainloop()