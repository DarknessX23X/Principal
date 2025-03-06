import csv

def remove_trailing_commas(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        rows = [','.join(row).rstrip(',') for row in reader]

    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows([row.split(',') for row in rows])

# Exemplo de uso
caminho_arquivo = 'E:\\OneDrive\\Virtual Age\\DICFM001_BI\\Produtos_Vendas_VA.csv'
remove_trailing_commas(caminho_arquivo)