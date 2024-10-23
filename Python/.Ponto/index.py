from flask import Flask, render_template
import pyodbc
import io
import base64
from PIL import Image

app = Flask(__name__)

# String de conexão com o SQL Server
conn_str = (
    "Driver={SQL Server};"
    "Server=192.168.0.4;"
    "Database=CorporeRM;"
    "UID=SA;"
    "PWD=sqlserver;"
)

@app.route('/')
def index():
    try:
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()

        # Executar a consulta SQL para obter a imagem
        cursor.execute('select a.ID,a.imagem from GIMAGEM a')  # Ajuste a consulta se necessário
        resultado = cursor.fetchone()

        if resultado:
            id_imagem, imagem_base64 = resultado
            image_src = f"data:image/jpeg;base64,{imagem_base64}"  # Assumindo que a imagem é JPEG
            return render_template('index.html', image_src=image_src)
        else:
            return "Nenhuma imagem encontrada."

    except Exception as e:
        return f"Erro ao conectar ao banco de dados: {e}"

    finally:
        if conn:
            conn.close()

@app.route('/imagem/<int:id>')
def imagem(id):
    try:
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()

        # Executar a consulta SQL para obter a imagem pelo ID
        cursor.execute('select a.ID,a.imagem,b.NOME,c.CHAPA from GIMAGEM a,PPESSOA b,pfunc c where b.IDIMAGEM=a.ID and c.NOME=b.NOME and c.chapa = ? ', id)  # Ajuste a consulta se necessário
        resultado = cursor.fetchone()

        if resultado:
            imagem_base64 = resultado[0]
            image_src = f"data:image/jpeg;base64,{imagem_base64}"  # Assumindo que a imagem é JPEG
            return render_template('imagem.html', image_src=image_src)
        else:
            return "Imagem não encontrada."

    except Exception as e:
        return f"Erro ao conectar ao banco de dados: {e}"

    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    app.run(debug=True)