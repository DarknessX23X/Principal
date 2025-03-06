from flask import Flask, request, render_template, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Configurações do banco de dados (MySQL)
DATABASE_CONFIG = {
        'user': 'root',
        'password': 'Tec2024K@3,14colli',
        'host': '192.168.0.12',
        'database': 'kazzo',
        'raise_on_warnings': True
        }


# Função para criar a tabela no banco de dados (se não existir)
def create_table():
    try:
        mydb = mysql.connector.connect(**DATABASE_CONFIG)
        cursor = mydb.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS dados (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(255),
                idade INT
            )
        ''')
        mydb.commit()
        cursor.close()
        mydb.close()
    except mysql.connector.Error as err:
        print(f"Erro ao criar tabela: {err}")


# Rota para o formulário de entrada (mesmo que antes)
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nome = request.form['nome']
        idade = request.form['idade']
        insert_data(nome, idade)
        return redirect(url_for('index'))
    return render_template('index.html')


# Função para inserir dados no banco de dados
def insert_data(nome, idade):
    try:
        mydb = mysql.connector.connect(**DATABASE_CONFIG)
        cursor = mydb.cursor()
        sql = "INSERT INTO dados (nome, idade) VALUES (%s, %s)"
        val = (nome, idade)
        cursor.execute(sql, val)
        mydb.commit()
        cursor.close()
        mydb.close()
    except mysql.connector.Error as err:
        print(f"Erro ao inserir dados: {err}")


# Cria a tabela ao iniciar o aplicativo
create_table()

if __name__ == '__main__':
    app.run(debug=True)