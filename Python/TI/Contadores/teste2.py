from itertools import zip_longest

HOST = ["192.168.0.60","192.168.0.61","192.168.0.62","192.168.0.63","192.168.0.64","192.168.0.65","192.168.0.67","192.168.0.68","192.168.0.69","192.168.0.70","192.168.10.55"]
LOCAL = ["ALMOXARIFADO","ETIQUETAS","FINANCEIRO","COLORIDA","ADMINISTRATIVO","DEPARTAMENTO PESSOAL","RECEBIMENTO","LAVANDERIA","EXPEDIÇÃO","MODELAGEM","TREVÃO"]

for item, item2 in zip_longest(HOST, LOCAL, fillvalue="N/A"):
    print(f"Host: {item}, Local: {item2}")