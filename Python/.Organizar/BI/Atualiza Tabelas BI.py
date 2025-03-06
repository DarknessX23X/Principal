import csv
import os
import pandas as pd
from google.cloud import bigquery
from pandas_gbq import to_gbq
import time

Plotter = r"X:\\BI\\Atualizador\\Plotters.py"



os.system('cls' if os.name == 'nt' else 'clear')

os.system(f"python {Plotter}")

#time.sleep(15)
# Abre o arquivo CSV em modo de leitura
with open('X:\\BI\\CONFIG\\TABELAS.CSV', newline='') as csvfile:
    # Cria um leitor CSV
    csvreader = csv.reader(csvfile, delimiter=';')
    
    # Itera sobre as linhas do arquivo e imprime cada linha
    for row in csvreader:
        path = os.path.join ("X:\\BI\\DADOS\\",*row) +".CSV"
        table ="BI."+ row[0]
        #print(table)       
        df = pd.read_csv(path,delimiter=';', encoding='latin-1',low_memory=False)
        to_gbq(df, destination_table=table, project_id='sinuous-vent-418310', if_exists='replace')
        print("Tabela " +row[0]+" Atualizada")

#os.system('cls' if os.name == 'nt' else 'clear')