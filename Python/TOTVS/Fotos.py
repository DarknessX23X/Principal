import pyodbc
import io
import base64
from PIL import Image

# Configurar a string de conexão
conn_str = (
    "Driver={SQL Server};"
    "Server=192.168.0.4;"
    "Database=CorporeRM;"
    "UID=SA;"
    "PWD=sqlserver;"
    )

caminho_arquivo = 'C:\\config\\1.jpg'

# Conectar ao banco de dados
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

cursor.execute('select a.ID,a.imagem,b.NOME from GIMAGEM a,PPESSOA b where b.IDIMAGEM=a.ID')
resultados = cursor.fetchall()

#imagem_bytes = cursor.fetchone()[0]

for row in resultados:
    caminho_arquivo = 'C:\\config\\Fotos\\'f'{row[2]}.jpg'
    print(caminho_arquivo)
    with open(caminho_arquivo, "wb") as arquivo:
        arquivo.write(row[1])   


conn.close()
#