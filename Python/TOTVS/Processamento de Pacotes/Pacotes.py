import requests
import json


url = 'https://www30.bhan.com.br:9443/api/totvsmoda/authorization/v2/token'  # Substitua 'https://exemplo.com/api/json' pela URL do JSON que deseja acessar
url_pacote='https://www30.bhan.com.br:9443/api/totvsmoda/data-package/v2/input-packages?Status=2'
url_pacote_andamento='https://www30.bhan.com.br:9443/api/totvsmoda/data-package/v2/output-packages'
url_reativacao = 'https://www30.bhan.com.br:9443/api/totvsmoda/data-package/v2/packages/reactivate'
url_processamento = 'https://www30.bhan.com.br:9443/api/totvsmoda/data-package/v2/output-packages/receive'


headers = {
        "grant_type": "password",
        "client_id": "kazzoconfeccoesapiv2",
        "client_secret" : "9325991742",
        "username" : "giovane",
        "password" : "Darkness" }
response = requests.post(url,data=headers)


if response.status_code == 200:
    data = response.json()
    access_token = data['access_token']
    #print(access_token)
    
else:
    print('Erro ao fazer o request. Código de status:', response.status_code)

headers_pct = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}"
    }

'''
response_pct = requests.get(url_pacote,headers=headers_pct)
if response_pct.status_code == 200:
    data_pct=response_pct.json()    
    for item in data_pct['items']:
      data = {"packageId": item['packageId']}
      response_reativacao = requests.post(url_reativacao, headers=headers_pct, data=json.dumps(data))
      if response_reativacao.status_code == 200:
         data_reativacao=response_reativacao.json()  
         print(data_reativacao)  
      else:
        print('Erro ao fazer o request. Código de status:', response_reativacao.status_code)      
     #print(item['packageId']) 
else:
    print('Erro ao fazer o request. Código de status:', response_pct.status_code)      
'''

responde_pct_andamento =requests.get(url_pacote_andamento,headers=headers_pct)
if responde_pct_andamento.status_code == 200:
    data_pct_andamento=responde_pct_andamento.json() 
    for item in data_pct_andamento['items']:
     data = {"packageId": item['packageId']}
     print(item['packageId'])
     response_processamento = requests.post(url_processamento, headers=headers_pct, data=json.dumps(data))
     data_processamento=response_processamento.json()  
     print(data_processamento) 
     if response_processamento.status_code == 200:
         data_processamento=response_processamento.json()  
         #print(data_processamento)  
     else:
        print('Erro ao fazer o request. Código de status:', response_processamento.status_code)      
else:
    print('Erro ao fazer o request. Código de status:', responde_pct_andamento.status_code) 
         