import requests
from xml.dom import minidom


xml_file = 'C:\\Config\\XML\\1.xml'

dom = minidom.parse(xml_file)

cprod_elements = dom.getElementsByTagName('cProd')
Ucom = dom.getElementsByTagName('uCom')

for cprod in cprod_elements:
    prd = cprod.firstChild.nodeValue

for uni in Ucom:
    print(uni.firstChild.nodeValue)    
    




url = 'https://www30.bhan.com.br:9443/api/totvsmoda/authorization/v2/token'
data = {'grant_type': 'password', 'client_id': 'kazzoconfeccoesapiv2', 'client_secret': '9325991742', 'username': 'giovane', 'password': 'Darkness'}

response = requests.post(url, data=data, headers={'Content-Type': 'application/x-www-form-urlencoded'})


if response.status_code == 200:
    print('Requisição bem-sucedida!')
    response_json = response.json()
    access_token = response_json['access_token']
    #print(f"Access token: {access_token}")
else:
    print('Erro na requisição:', response.status_code)


url = 'https://www30.bhan.com.br:9443/api/totvsmoda/product/v2/products/'f'{prd}/1'
headers = {'Authorization': f'Bearer {access_token}'}
response = requests.get(url, headers=headers)   

if response.status_code == 200:
    print('Requisição bem-sucedida!')
    response_json = response.json()
    print(response_json)
else:
    print('Erro na requisição:', response.status_code)

