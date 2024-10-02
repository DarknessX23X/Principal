from brother import Brother, SnmpError, UnsupportedModelError
import asyncio
import logging
import pysnmp.hlapi.asyncio as hlapi
import os
import socket
from flask import Flask, render_template
from itertools import zip_longest

app = Flask(__name__)

HOST = ["192.168.0.60","192.168.0.61","192.168.0.62","192.168.0.63","192.168.0.64","192.168.0.65","192.168.0.67","192.168.0.68","192.168.0.69","192.168.0.70","192.168.10.55"]  # Substitua pelo endereço IP da sua impressora
LOCAL = ["ALMOXARIFADO","ETIQUETAS","FINANCEIRO","COLORIDA","ADMINISTRATIVO","DEPARTAMENTO PESSOAL","RECEBIMENTO","LAVANDERIA","EXPEDIÇÃO","MODELAGEM","TREVÃO"]
PRINTER_TYPE = "laser"  # Ou "ink" para impressoras jato de tinta
#logging.basicConfig(level=logging.DEBUG)
snmp_engine = hlapi.SnmpEngine()

def check_connection(host, port=80): 
  try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
      sock.settimeout(1)  # Definir um tempo limite para a conexão
      sock.connect((host, port))
      return True
  except socket.error:
    return False


async def get_printer_data():
  data = []
  for item,item2 in zip_longest(HOST,LOCAL, fillvalue="N/A"):
    try:
        if check_connection(item):
            brother = await Brother.create(item, printer_type=PRINTER_TYPE, snmp_engine=snmp_engine)
            data_item = await brother.async_update()
            page_counter = data_item.page_counter
            if item =="192.168.0.63": 
                    bw_counter = data_item.bw_counter
                    color_counter = data_item.color_counter
                    data.append({'ip': item2 + ' - Colorida' , 'contador': color_counter})
                    data.append({'ip': item2 + ' - Preto' , 'contador': bw_counter})
            else:                            
              data.append({'ip': item2, 'contador': page_counter})
        else:
            data.append({'ip': item2, 'contador': 'Desligada'})    
        
            
    except (ConnectionError, SnmpError, UnsupportedModelError) as error:
     print(f"Erro: {error}")
  return data

@app.route("/")
async def index():
  printer_data = await get_printer_data()
  return render_template('index.html', printer_data=printer_data)

if __name__ == "__main__":
  app.run(debug=True)