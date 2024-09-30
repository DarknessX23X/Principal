import csv
import pandas as pd
import os
import shutil
import time

#pasta = 'R:\\Virtual Age\\DICFM001_BI_AJUSTAR_VIEWS'
#pasta_destino = 'R:\\Virtual Age\\DICFM001_BI'

pasta = 'E:\\OneDrive\\Virtual Age\\DICFM001_BI_AJUSTAR_VIEWS'
pasta_destino = 'E:\\OneDrive\\Virtual Age\\DICFM001_BI'

def verifica_arquivo_em_uso(nome_arquivo):
    try:
        arquivo = open(nome_arquivo, "a+")  # tenta abrir o arquivo no modo 'append and read'
        arquivo.close()
        return False  # retorna False se o arquivo NÃO estiver em uso
    except IOError:
        return True  # retorna True se o arquivo estiver em uso

def remover_espaco(caminho_pasta):
    linhas_filtradas = []
    with open(caminho_pasta, 'r', errors='ignore') as arquivo_entrada:
        leitor_csv = csv.reader(arquivo_entrada, delimiter=';')

    # Filtra as linhas que não estão totalmente em branco
        for linha in leitor_csv:
            if any(campo.strip() for campo in linha):
            # Adicionando a linha à lista linhas_filtradas
                linhas_filtradas.append(linha)
   

    # Abre um novo arquivo CSV de saída para escrita
    with open(caminho_pasta, 'w', newline='') as arquivo_saida:
        escritor_csv = csv.writer(arquivo_saida, delimiter=';')
        
        escritor_csv.writerows(linhas_filtradas)
    #print("O arquivo de saída foi salvo em:", caminho_pasta)

def deletar_arquivos_csv_em_pasta(caminho_pasta):
    # Verifica se o caminho é uma pasta válida
    if os.path.isdir(caminho_pasta):
        # Lista todos os arquivos e diretórios dentro da pasta
        conteudo_pasta = os.listdir(caminho_pasta)
        
        # Filtra apenas os arquivos CSV
        arquivos_csv = [arquivo for arquivo in conteudo_pasta if arquivo.endswith(".csv") or arquivo.endswith(".CSV")  ]
        
        if len(arquivos_csv) > 0:
            print("Deletando arquivos CSV na pasta:")
            for arquivo in arquivos_csv:
                print(arquivo)
                os.remove(os.path.join(caminho_pasta, arquivo))
            print("Todos os arquivos CSV foram deletados.")
        else:
            print("A pasta não contém arquivos CSV.")
    else:
        print("O caminho especificado não é uma pasta válida.")

def remove_trailing_commas(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        rows = [','.join(row).rstrip(',') for row in reader]

    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows([row.split(',') for row in rows])

def lowercase_csv_extension(file_path):
    file_name, file_extension = os.path.splitext(file_path)
    if file_extension.lower() == '.csv':
        new_file_path = file_name + file_extension.lower()
        os.rename(file_path, new_file_path)

while True:
 dataframes = []
 arquivos = os.listdir(pasta)
 num_csv = sum(1 for arquivo in arquivos if arquivo.endswith('.csv') or arquivo.endswith('.CSV'))
 if num_csv >= 1:
  for arquivo in os.listdir(pasta):
    if arquivo.endswith('.csv') or arquivo.endswith('.CSV') :
        caminho_arquivo = os.path.join(pasta, arquivo)
        caminho_destino = os.path.join(pasta_destino,arquivo)
        print(caminho_arquivo)
        with open(caminho_arquivo, 'r', errors='ignore') as file:   
            reader = csv.reader(file)    
            valid_rows = []
    
            for row in reader:
                try:
                    row = [coluna.rstrip(',') for coluna in row]
                    valid_rows.append(row)
                except csv.Error as e:            
                    print(f"Error processing row: {e}")


            df = pd.DataFrame(valid_rows)
            df.drop_duplicates(keep='first', inplace=True)  
            df.to_csv(caminho_destino, index=False, header=False, escapechar=' ')
            remove_trailing_commas(caminho_destino)
            lowercase_csv_extension(caminho_destino)
            remover_espaco(caminho_destino)          
            

                
     
