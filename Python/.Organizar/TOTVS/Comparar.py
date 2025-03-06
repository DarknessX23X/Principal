import csv
import os

with open('C:\\Config\\Faltante.csv', 'r', newline='', encoding='utf-8') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv,delimiter=';')
        for linha in leitor_csv:
           caminho_arquivo = "C:\\Config\\Fotos\\"f"{linha[1]}.jpg"
           if os.path.isfile(caminho_arquivo): 
                 print(f"'{linha[1]}'")
           else:
                print("")     