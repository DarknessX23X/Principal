import pandas as pd
import warnings
warnings.filterwarnings("ignore")

# Carregar o arquivo xlsx
df = pd.read_excel('X:\\TI\\Jeferson\\0. Planilhas\\TOTVS - Liberação.xlsx', sheet_name='185 - Comp. por Grupo')

# Procurar um valor específico
coluna_especifica = 'Cod. Grupo'  # Substitua pelo nome da coluna que você deseja filtrar
valor_especifico = "TRAFL016"  # Substitua pelo valor que você deseja buscar

df_filtrado = df.loc[(df["Cod. Grupo"] > 4000)  & (df.isin([valor_especifico]).any(axis=1))]

print(df_filtrado)