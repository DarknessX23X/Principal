import pyodbc

# Configurar a string de conexão
conn_str = (
    "Driver={SQL Server};"
    "Server=192.168.0.4;"
    "Database=CorporeRM;"
    "UID=SA;"
    "PWD=sqlserver;"
    )

# Conectar ao banco de dados
conn = pyodbc.connect(conn_str)

# Criar um cursor
cursor = conn.cursor()

param_value = input("Por favor, insira o nome da pessoa: ")
param_value = param_value.upper()
# Executar uma consulta SQL
#cursor.execute('SELECT a.chapa,a.nome,b.telefone1,b.telefone2,b.cpf,b.dtnascimento,a.salario FROM pfunc a,ppessoa b WHERE a.nome = b.nome and a.nome like ?','%' + param_value +'%')
cursor.execute('SELECT a.chapa, a.nome, b.telefone1, b.telefone2, b.cpf, b.dtnascimento, a.salario, b.rua FROM pfunc a, ppessoa b WHERE a.nome = b.nome AND a.nome LIKE ? ORDER BY a.chapa', (param_value + '%',))
resultados = cursor.fetchall()
# Fechar a conexão
conn.close()

for row in resultados:
    coluna1 = row[0]
    coluna2 = row[1]
    coluna3 = row[2]
    coluna4 = row[3]
    coluna5 = row[4]
    coluna6 = row[5]
    coluna7 = row[6]
    coluna8 = row[7]
    

    print(f"CHAPA: {coluna1}")
    print(f"NOME: {coluna2}")
    print(f"TELEFONE 1: {coluna3}")
    print(f"TELEFONE 2: {coluna4}")
    print(f"CPF: {coluna5}")
    print(f"Data Nascimento: {coluna6}")
    print(f"Salario: {coluna7}")
    print(f"Endereço: {coluna8}")
    