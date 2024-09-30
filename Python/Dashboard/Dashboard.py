import dash
import dash_table
import pandas as pd
import datetime
from dash.dependencies import Input, Output
import time

# Obter o primeiro dia do mês atual
hoje = datetime.date.today()
primeiro_dia_mes_atual = hoje.replace(day=1)

# Criar as datas do mês atual, de 1 a 31
datas_mes_atual = pd.date_range(start=primeiro_dia_mes_atual, periods=31, freq='D')

# Carregar o arquivo CSV com ponto e vírgula como delimitador
df = pd.read_csv('.\\Dashboard\\Dados.CSV', delimiter=';')

# Obter apenas os valores únicos da coluna "Ds. Localorigem"
nomes_unicos = df['Ds. Localorigem'].unique()
paginated_data = [{"Nomes Únicos": nome} for nome in nomes_unicos[:10]]

# Inicializar o Dash
app = dash.Dash(__name__)

# Layout do dashboard
app.layout = dash_table.DataTable(
    id='tabela',
    columns=[{"name": "Nomes Únicos", "id": "Nomes Únicos"}],
    data=paginated_data,
    style_cell={'textAlign': 'center', 'fontSize': '9px', 'fontWeight': 'bold'},
    sort_action='native',
    page_current=0,
    page_size=10
)

@app.callback(
    Output('tabela', 'data'),
    [Input('tabela', 'page_current')]
)
def update_table(page_current):
    paginated_data = [{"Nomes Únicos": nome} for nome in nomes_unicos[10*(page_current):10*(page_current+1)]]
    return paginated_data

@app.callback(
    Output('tabela', 'page_current'),
    [Input('tabela', 'page_current')]
)
def increment_page(page_current):
    time.sleep(10)
    if page_current >= len(nomes_unicos) // 10 - 1:
        return 0
    else:
        return page_current + 1

if __name__ == '__main__':
    app.run_server(debug=True)