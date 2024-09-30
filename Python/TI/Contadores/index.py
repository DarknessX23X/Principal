from flask import Flask, render_template
from datetime import datetime, timedelta
import calendar
from google.cloud import bigquery
from google.oauth2 import service_account
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from ping3 import ping
import datetime
import locale

app = Flask(__name__)

setor = []
contador =[]
locale.setlocale(locale.LC_TIME, 'pt_BR.utf8')



def check_ping(hostname):
    response = ping(hostname)
    if response is not None:
        print(f"{hostname} está online. Tempo de resposta: {response} segundos.")
    else:
        print(f"{hostname} está offline ou inacessível.")

def Almoxarifado():
    response = check_ping('192.168.0.64')
    if response is not None:
        chrome_options = Options()
        #chrome_options.add_argument("--headless") 
        #chrome_options.add_argument() 
        driver = webdriver.Chrome()
        driver.get("http://192.168.0.64/general/information.html?kind=item")
        elemento = driver.find_element("name","B1350")
        elemento.send_keys("initpass")
        elemento.send_keys(Keys.RETURN)
        elemento = driver.find_elements(By.TAG_NAME,"dd")
        #contador = elemento[5].text        

    #return contador


def obter_mes_anterior():
    hoje = datetime.today()
    primeiro_dia_mes_atual = hoje.replace(day=1)
    primeiro_dia_mes_passado = primeiro_dia_mes_atual - timedelta(days=1)
    
    mes_passado = primeiro_dia_mes_passado.month

    # Ajuste para exibir o nome do mês em português
    nome_mes_passado = calendar.month_name[mes_passado]
    meses_pt = ["", "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    nome_mes_passado_pt = meses_pt[mes_passado]

    return nome_mes_passado_pt

def obter_mes_atual():
    hoje = datetime.today()
    primeiro_dia_mes_atual = hoje.replace(day=1)
    
    mes_atual = primeiro_dia_mes_atual.month

    # Ajuste para exibir o nome do mês em português
    nome_mes_atual = calendar.month_name[mes_atual]
    meses_pt = ["", "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    nome_mes_passado_pt = meses_pt[mes_atual]

    return nome_mes_passado_pt

def ler_dados_txt():
    caminho_credenciais = 'credenciais.json'
    credenciais = service_account.Credentials.from_service_account_file(caminho_credenciais)
    client = bigquery.Client(credentials=credenciais)  
    valores = [] 
    dados = []
    with open('dados.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            cols = line.strip().split(',')
            sql = "SELECT Max(QUANTIDADE) FROM `sinuous-vent-418310.BI.IMPRESSORAS` WHERE IMPRESSORA = "f"'{cols[0]}' AND ANO='2024'"   
            resultados = client.query(sql).result()
            valores_coluna = [row[0] for row in resultados]  
            nome = cols[1]
            link = f'{nome}'  # Adicionando hiperlink na segunda coluna
            Cont = Almoxarifado()
            if valores_coluna:
              dados.append([link,cols[0],cols[2],cols[3],cols[4],valores_coluna[0]],Cont) 
            else:
              dados.append([link,cols[0],cols[2],cols[3],cols[4],'0'],Cont) 


    dados.sort(key=lambda x: x[1])  # Ordenar os dados pela primeira coluna

    #print(dados)
    return dados

@app.route('/')
def tabela():
    dados = ler_dados_txt()
    mes_anterior = obter_mes_anterior()
    mes_atual=obter_mes_atual()
    return render_template('index.html', dados=dados, mes_anterior=mes_anterior,mes_atual=mes_atual)

if __name__ == '__main__':
    app.run()