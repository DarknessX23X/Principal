from flask import Flask, render_template, request
import mysql.connector
import csv
import os
import pandas as pd

app = Flask(__name__)

def get_data_from_mysql(pesquisa,opcao):        
    try:
        config = {
        'user': 'root',
        'password': 'Tec2024K@3,14colli',
        'host': '192.168.0.12',
        'database': 'kazzo',
        'raise_on_warnings': True
        }

        connection = mysql.connector.connect(**config)

        if connection.is_connected():
            db_info = connection.get_server_info()
            print(f"Conectado ao servidor MySQL versão {db_info}")

  # Executa uma consulta
            cursor = connection.cursor()

            if opcao == "Telas" :
            #print("SELECT distinct(CD_grupo) as Codigo,ds_grupo as Grupo, Componente as Codigo,ds_componente as Componente FROM permissoes where componente like \""+pesquisa+"%\" order by cd_grupo")
                cursor.execute("SELECT distinct(CD_grupo) as Codigo,ds_grupo as Grupo, Componente as Codigo,ds_componente as Componente FROM permissoes where componente like \""+pesquisa+"%\" and cd_grupo >=4000 order by cd_grupo ")
                column_names = [desc[0] for desc in cursor.description]
                table_data = cursor.fetchall()

            if opcao == "Grupos" :
            #print("SELECT distinct(CD_grupo) as Codigo,ds_grupo as Grupo, Componente as Codigo,ds_componente as Componente FROM permissoes where componente like \""+pesquisa+"%\" order by cd_grupo")
                cursor.execute("SELECT distinct(CD_grupo) as Codigo,ds_grupo as Grupo, Componente as Codigo,ds_componente as Componente FROM permissoes where CD_grupo like \""+pesquisa+"%\" order by ds_componente ")
                column_names = [desc[0] for desc in cursor.description]
                table_data = cursor.fetchall() 

            if opcao == "Usuarios" :
                #print("SELECT distinct(codigo) as Codigo,CONCAT(cd_grupo, ' - ', ds_grupo) as Grupo, Componente as Codigo,ds_componente as Componente FROM permissoes where Codigo like \""+pesquisa+"%\" order by cd_grupo ")
                cursor.execute("SELECT distinct(codigo) as Codigo,Nome, CONCAT(cd_grupo, ' - ', ds_grupo) as Grupo, Componente as Codigo,ds_componente as Componente FROM permissoes where Codigo = \""+pesquisa+"\"  order by cd_grupo ")
                column_names = [desc[0] for desc in cursor.description]
                table_data = cursor.fetchall()         

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


            return column_names, table_data



@app.route('/', methods=['GET', 'POST'])
def index(): 
       

   return render_template('index.html')



@app.route('/pesquisar', methods=['POST'])
def pesquisar(): 
    opcoes = request.form.get('opcoes')    
    pesquisa = request.form.get('pesquisa')    

    column_names, table_data = get_data_from_mysql(request.form.get('pesquisa'),opcoes)
    return render_template('index.html', column_names=column_names, table_data=table_data)

@app.route('/atualizar_tabelas', methods=['POST'])
def atualizar_tabelas(): 
    config = {
        'user': 'root',
        'password': 'Tec2024K@3,14colli',
        'host': '192.168.0.12',
        'database': 'kazzo',
        'raise_on_warnings': True,
        'connection_timeout':300
        }
    caminho_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_arquivo_opcoes = os.path.join(caminho_atual, "LIBERACAO.CSV")
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    data = []
    with open(caminho_arquivo_opcoes, 'r', encoding='latin-1') as csvfile:
        reader = csv.reader(csvfile,delimiter=";")
    # Ignorar a primeira linha (cabeçalho)
        next(reader)
        for row in reader:
        # Verificar se a linha não está vazia
         if any(row): 
            data.append(row)
    sql ="DELETE FROM PERMISSOES"
    cursor.execute(sql)
    connection.commit()
    sql ="SET GLOBAL max_allowed_packet = 500 * 1024 * 1024"
    cursor.execute(sql)
    sql = "INSERT INTO permissoes (codigo, nome, componente,ds_componente,cd_grupo,ds_grupo) VALUES (%s, %s, %s,%s, %s, %s)"    
    cursor.executemany(sql, data)
    connection.commit()
    cursor.close()
    connection.close()


    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port="8081")