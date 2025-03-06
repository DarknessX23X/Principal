import mysql.connector

# Configurações para conexão ao banco de dados
config = {
  'user': 'root',
  'password': 'Tec2024K@3,14colli',
  'host': '192.168.0.12',
  'database': 'kazzo',
  'raise_on_warnings': True
}

try:
  # Estabelece a conexão com o banco de dados
  connection = mysql.connector.connect(**config)

  if connection.is_connected():
    db_info = connection.get_server_info()
    print(f"Conectado ao servidor MySQL versão {db_info}")

  # Executa uma consulta
  cursor = connection.cursor()
  cursor.execute("SELECT * FROM suporte")

  # Obtém os resultados da consulta
  rows = cursor.fetchall()
  for row in rows:
    print(row)

except mysql.connector.Error as e:
  print(f"Erro ao conectar ao banco de dados MySQL: {e}")

finally:
  # Fecha a conexão com o banco de dados
  if 'connection' in locals() and connection.is_connected():
    cursor.close()
    connection.close()
    print("Conexão ao banco de dados MySQL encerrada")