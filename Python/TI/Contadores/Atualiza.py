from google.cloud import bigquery
from google.oauth2 import service_account
# Inicialize o client do BigQuery

caminho_credenciais = 'credenciais.json'

credenciais = service_account.Credentials.from_service_account_file(caminho_credenciais)

client = bigquery.Client(credentials=credenciais)
# Defina o projeto e dataset onde a tabela está localizada
projeto = "sinuous-vent-418310"
dataset = "BI"
tabela = "IMPRESSORAS"

# Dados a serem inseridos (substitua pelos seus próprios dados)
dados = [
    {"impressora": "Departamento Pessoal", "mes": "JULHO","ano":"2024","quantidade":"269948"},
    {"impressora": "Administrativo", "mes": "JULHO","ano":"2024","quantidade":"777456"},
    {"impressora": "Financeiro", "mes": "JULHO","ano":"2024","quantidade":"95445"},
    {"impressora": "Almoxarifado", "mes": "JULHO","ano":"2024","quantidade":"320923"},
    {"impressora": "Etiquetas", "mes": "JULHO","ano":"2024","quantidade":"491226"},
    {"impressora": "Expedição", "mes": "JULHO","ano":"2024","quantidade":"499900"},
    {"impressora": "Lavanderia", "mes": "JULHO","ano":"2024","quantidade":"462534"},
    {"impressora": "Recebimento", "mes": "JULHO","ano":"2024","quantidade":"177212"},
    {"impressora": "Trevão", "mes": "JULHO","ano":"2024","quantidade":"473274"},
    {"impressora": "Kabmadeira", "mes": "JULHO","ano":"2024","quantidade":"4119"},
    {"impressora": "Colorida - Color", "mes": "JULHO","ano":"2024","quantidade":"6490"},
    {"impressora": "Colorida - Preto", "mes": "JULHO","ano":"2024","quantidade":"42035"},
    {"impressora": "Modelagem", "mes": "JULHO","ano":"2024","quantidade":"272688"},
]

# Insira os dados na tabela
table_id = f"{projeto}.{dataset}.{tabela}"
client.insert_rows_json(table_id, dados)

print("Dados inseridos com sucesso no BigQuery!")