from brother import Brother, SnmpError, UnsupportedModelError
import asyncio
import logging
import pysnmp.hlapi.asyncio as hlapi
import os

HOST = {"192.168.0.60","192.168.0.61","192.168.0.62","192.168.0.63","192.168.0.64","192.168.0.65","192.168.0.67","192.168.0.68","192.168.0.69","192.168.0.70","192.168.10.55"}  # Substitua pelo endereço IP da sua impressora
LOCAL = {"ALMOXARIFADO","ETIQUETAS","FINANCEIRO","COLORIDA","ADMINISTRATIVO","DEPARTAMENTO PESSOAL","RECEBIMENTO","LAVANDERIA","EXPEDIÇÃO","MODELAGEM","TREVÃO"}
PRINTER_TYPE = "laser"  # Ou "ink" para impressoras jato de tinta
#logging.basicConfig(level=logging.DEBUG)
snmp_engine = hlapi.SnmpEngine()

import socket

def check_connection(host, port=80): 
  try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
      sock.settimeout(1)  # Definir um tempo limite para a conexão
      sock.connect((host, port))
      return True
  except socket.error:
    return False


async def main():
 for item in HOST:
    try:
        if check_connection(item):
            brother = await Brother.create(item, printer_type=PRINTER_TYPE, snmp_engine=snmp_engine)
            data = await brother.async_update()
            if item =="192.168.0.63": 
                    bw_counter = data.bw_counter
                    color_counter = data.color_counter
                    print(f"{item} - Colorida Contador: {color_counter}")
                    print(f"{item} - Preto Contador: {bw_counter}")
            else: 
                    page_counter = data.page_counter 
                    print(f"{item} Contador: {page_counter}")   
        else:
            print(f"{item} está desligado.")    
        

    except (ConnectionError, SnmpError, UnsupportedModelError) as error:
     print(f"Erro: {error}")

asyncio.run(main()) 
