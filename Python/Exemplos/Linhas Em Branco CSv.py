import csv

# Abre o arquivo CSV de entrada para leitura
with open('E:\\OneDrive\\Virtual Age\\DICFM001_BI\\Faturamento_Kazzo.csv', 'r', errors='ignore') as arquivo_entrada:
    leitor_csv = csv.reader(arquivo_entrada, delimiter=';')
    
        
    # Filtra as linhas que não estão totalmente em branco
    linhas_filtradas = [linha for linha in leitor_csv if any(campo.strip() for campo in linha)]
    
    quantidade_colunas = len(linhas_filtradas[0])

    # Abre um novo arquivo CSV de saída para escrita
    with open('E:\\OneDrive\\Virtual Age\\DICFM001_BI\\Faturamento_Kazzo.csv', 'w', newline='') as arquivo_saida:
        escritor_csv = csv.writer(arquivo_saida, delimiter=';')
        
        escritor_csv.writerows(linhas_filtradas)

print("A quantidade de colunas é:", quantidade_colunas)