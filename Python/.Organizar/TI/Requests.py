import requests

# URL base da API
base_url = "https://www30.bhan.com.br:9443/api/v1/pacotes/"

# Fazer uma requisição HTTP para a URL base
response = requests.get(base_url)

# Verificar se a requisição foi bem-sucedida (código de status 200)
if response.status_code == 200:
    # Extrair os métodos disponíveis da resposta
    methods = response.json().keys()

    # Imprimir os métodos disponíveis
    for method in methods:
        print(method)
else:
    print("Erro ao fazer a requisição:", response.status_code)