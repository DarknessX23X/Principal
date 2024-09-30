from google.cloud import bigquery
from google.oauth2 import service_account


def consultar_coluna():
    caminho_credenciais = 'credenciais.json'
    credenciais = service_account.Credentials.from_service_account_file(caminho_credenciais)
    client = bigquery.Client(credentials=credenciais)
    
    valores_finais = []
    valores = [] 
    with open('dados.txt', 'r', encoding='utf-8') as file:
        valores_finais = []
        lines = file.readlines()
        for line in lines:
         cols = line.strip().split(',')  
         sql = "SELECT DISTINCT(QUANTIDADE) FROM `sinuous-vent-418310.BI.IMPRESSORAS` WHERE IMPRESSORA = "f"'{cols[0]}' AND ANO='2024'"   
         #print(sql)
         #exit() 
         resultados = client.query(sql).result()
         valores_coluna = [row[0] for row in resultados]
         valores_formatados = [str(valor) for valor in valores_coluna]
         valores_finais.extend(valores_formatados)  # Adiciona os valores formatados à lista final
        valores.append(valores_finais)
        valores_sem_colchetes = ', '.join(valores_finais)  # Converte a lista em uma string separada por vírgulas
    
    print(valores_sem_colchetes)

    return valores

consultar_coluna()