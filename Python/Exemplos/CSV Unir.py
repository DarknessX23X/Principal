import glob
import pandas as pd

# Obter todos os caminhos dos arquivos CSV na pasta
file_list = glob.glob('X:\\TI\\GIOVANE\\Automações/*.CSV')

# Inicializar um DataFrame vazio
full_df = pd.DataFrame()

# Iterar sobre a lista de caminhos e concatenar os DataFrames
for file in file_list:
    df = pd.read_csv(file)
    full_df = pd.concat([full_df, df])

# Salvar o DataFrame completo em um único arquivo CSV
full_df.to_csv('arquivo_final.csv', index=False)