import csv
import mysql.connector

# Configurações para conexão ao banco de dados
config = {
    'user': 'root',
    'password': 'Tec2024K@3,14colli',
    'host': '192.168.0.12',
    'database': 'kazzo',
    'raise_on_warnings': True
}

# Nome do arquivo CSV a ser importado
csv_file = '.\Liberacao\Static\LIBERACAO.CSV'

try:
    # Estabelece a conexão com o banco de dados MySQL
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()

    sql = "DELETE FROM PERMISSOES"  # Modifique de acordo com a estrutura da sua tabela e os índices das colunas
    cursor.execute(sql)
    connection.commit()
    i = 1
    # Itera sobre as linhas do arquivo CSV e insere os dados no banco de dados
    with open(csv_file, 'r', encoding='latin-1') as file:
        csv_data = csv.reader(file,delimiter=";")
        next(csv_data)  # Ignora o cabeçalho        
        for row in csv_data:
            if len(row) == 6: 
                sql = f"INSERT INTO permissoes (codigo, nome, componente,ds_componente,cd_grupo,ds_grupo) VALUES ('{row[0]}', '{row[1]}', '{row[2]}', '{row[3]}', '{row[4]}', '{row[5]}')"  # Modifique de acordo com a estrutura da sua tabela e os índices das colunas
                cursor.execute(sql)
                i = i+1
                print("Importado"f"{i} Registros")
            
            else:
                print(f"A linha {row} não contém o número correto de colunas.") 

    # Efetua o commit das alterações
    connection.commit()
    cursor.close()
    connection.close()

    print("Importação do arquivo CSV concluída com sucesso.")

except Exception as e:
    print(f"Erro ao importar o arquivo CSV: {e}")