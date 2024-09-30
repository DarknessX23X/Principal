import pyodbc
from datetime import datetime
from flask import Flask, render_template, request

app = Flask(__name__)

# Conexão com o banco de dados SQL Server
conn = pyodbc.connect(
    'DRIVER={SQL Server};'
    'SERVER=192.168.0.5\MICROMAP;'
    'DATABASE=MapAcesso;'
    'UID=sa;'
    'PWD=Oramap82;'
)

@app.route('/', methods=['GET', 'POST'])
def index():
    mensagem = None  # Inicializa a variável mensagem
    if request.method == 'POST':
        data_filtroi = request.form.get('datai')
        data_filtrof = request.form.get('dataf')
        # Formata as datas para o formato do SQL Server
        data_sql_i = datetime.strptime(data_filtroi, '%Y-%m-%d').strftime('%Y-%m-%d')
        data_sql_f = datetime.strptime(data_filtrof, '%Y-%m-%d').strftime('%Y-%m-%d')

        # Executa a consulta com o filtro
        cursor = conn.cursor()
        cursor.execute(f"select a.data,a.hora,a.cartao,b.NOME,c.MATRICULA from COLETAOFFLINE a,CARTOES b,FUNCIONARIOS c where b.NUM_CARTAO=a.CARTAO and c.COD_PESSOA =b.COD_PESSOA and a.data between '{data_sql_i}' and '{data_sql_f}'")
        results = cursor.fetchall()
        caminho = "X:\\Depto Pessoal\\Captu\\INNERGRADE.TXT"

        # Gera a lista de resultados para o HTML
        with open(caminho, "w", encoding="utf-8") as arquivo:
            for row in results:
                data_formatada = datetime.strptime(row[0], '%Y-%m-%d').strftime('%d/%m/%y')
                hora_formatada = datetime.strptime(row[1], '%H:%M:%S').strftime('%H:%M')
                arquivo.write(f"010 {data_formatada} {hora_formatada} {row[4]} 15 1 \n")

        mensagem = "Arquivo Gerado com Sucesso!"  # Define a mensagem de sucesso

        return render_template('index.html', mensagem=mensagem)  # Retorna o template com a mensagem

    return render_template('index.html') # Retorna o template sem a mensagem

if __name__ == "__main__":
    app.run(debug=True,port='9000',host='0.0.0.0')