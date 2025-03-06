import requests

def get_valid_ip():
    try:
        response = requests.get('https://api.ipify.org?format=text')
        if response.status_code == 200:
            return response.text.strip()
        else:
            return "Não foi possível obter o IP válido."
    except requests.exceptions.RequestException as e:
        return str(e)

ip = get_valid_ip()
print(ip)