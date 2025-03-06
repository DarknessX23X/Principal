import pyodbc
from datetime import datetime
from flask import Flask, render_template, request

app = Flask(__name__)

conn_str = (
    'DRIVER={SQL Server};'
    'SERVER=192.168.0.5\MICROMAP;'
    'DATABASE=MapAcesso;'
    'UID=sa;'
    'PWD=Oramap82;'
)

@app.route('/', methods=['GET', 'POST'])
def index():
    data = []
    if request.method == 'POST':
        selected_date = request.form['datai']
        try:
            conn = pyodbc.connect(conn_str)
            cursor = conn.cursor()

            # Use parâmetros para evitar SQL Injection!
            cursor.execute("SELECT Ordem, FORMAT(data, 'dd/MM/yyyy') as Data, HORA FROM BILHETES WHERE NOMEPESSOA = ? AND Data = ? ORDER BY HORA", 'GIOVANE DE CARVALHO FERREIRA', selected_date)
            rows = cursor.fetchall()
            for row in rows:
                row_data = dict(zip([col[0] for col in cursor.description], row))
                #if isinstance(row_data['Data'], datetime):
                  #  row_data['Data'] = row_data['Data'].strftime('%d/%m/%Y')
                data.append(row_data)

            conn.close()
        except pyodbc.Error as ex:
            return f"<h1>Erro ao acessar o banco de dados:</h1><p>{ex}</p>"

    return render_template("index.html", data=data)

@app.route('/detalhes/<int:bilhete_id>')
def detalhes(bilhete_id):
    try:
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        cursor.execute("SELECT Ordem, Data, HORA FROM BILHETES WHERE Ordem = ?", bilhete_id)
        bilhete = cursor.fetchone()
        columns = [column[0] for column in cursor.description]
        bilhete_dict = dict(zip(columns, bilhete))
        conn.close()
        if bilhete_dict:
            
            return render_template('detalhes.html', bilhete=bilhete_dict) # Passe o dicionário aqui
        else:
            return "Bilhete não encontrado"
    except pyodbc.Error as ex:
        return f"Erro ao acessar o banco de dados: {ex}"
@app.route('/atualizar/<int:ordem_id>', methods=['POST'])
def atualizar(ordem_id):
    ordem = request.form['ordem']
    hora = request.form['hora']

    try:
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        cursor.execute("UPDATE BILHETES SET Hora = ? WHERE Ordem = ?",hora, ordem)
        cursor.commit()
        cursor.execute("SELECT Ordem, Data, HORA FROM BILHETES WHERE Ordem = ?", ordem_id)
        bilhete = cursor.fetchone()
        columns = [column[0] for column in cursor.description]
        bilhete_dict = dict(zip(columns, bilhete))
        conn.close()
        if bilhete_dict:
            
            return render_template('index.html') # Passe o dicionário aqui
        else:
            return "Bilhete não encontrado"
    except pyodbc.Error as ex:
        return f"Erro ao acessar o banco de dados: {ex}"


if __name__ == "__main__":
    app.run(debug=True, port='9000', host='0.0.0.0')