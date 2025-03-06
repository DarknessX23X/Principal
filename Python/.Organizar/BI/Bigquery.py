import pandas as pd
from google.cloud import bigquery
from pandas_gbq import to_gbq


credentials = "X:\\TI\\Giovane\\Automações\\BI\\credenciais.json"
client = bigquery.Client.from_service_account_json(credentials)


df = pd.read_csv("C:\\config\\bi\\ops.csv", delimiter=';')
to_gbq(df, destination_table='BI.OPS', project_id='sinuous-vent-418310', if_exists='replace')
print("Tabela OP - Atualizada")

df = pd.read_csv("C:\\config\\bi\\empresas.csv", delimiter=';')
to_gbq(df, destination_table='BI.EMPRESAS', project_id='sinuous-vent-418310', if_exists='replace')
print("Tabela Empresas - Atualizada")

df = pd.read_csv("C:\\config\\bi\\Finalizacao.csv", delimiter=';')
to_gbq(df, destination_table='BI.FINALIZACAO', project_id='sinuous-vent-418310', if_exists='replace')
print("Tabela Finalizacao - Atualizada")