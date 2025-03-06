from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os, re,time
from openpyxl import Workbook
from ping3 import ping
import subprocess
import re
from scapy.all import ARP, Ether, srp
import socket

def obter_mac_address(ip):
    # Cria um pacote ARP para solicitar o endereço MAC do dispositivo
    pacote_arp = ARP(pdst=ip)
    pacote_ethernet = Ether(dst="ff:ff:ff:ff:ff:ff")
    pacote_completo = pacote_ethernet / pacote_arp

    # Envia o pacote ARP e aguarda a resposta
    resultado, _ = srp(pacote_completo, timeout=2, verbose=False)

    # Extrai o endereço MAC da resposta
    if resultado:
        resposta = resultado[0][1]
        mac_address = resposta.hwsrc
        try:
            hostname = socket.gethostbyaddr(ip)[0]
        except:
            hostname ="Vago"
        return mac_address, hostname

    return None,None

def extrair_numeros(string):
    numeros = re.findall(r'\d+', string)
    numeros_int = [int(numero) for numero in numeros]
    numeros_str = ', '.join(map(str, numeros_int))
    return numeros_str

def verificar_e_deletar_arquivo(nome_arquivo):
    if os.path.exists(nome_arquivo):
        os.remove(nome_arquivo)
        print(f"O arquivo {nome_arquivo} foi excluído.")

with open('X:\\TI\\Giovane\\Automações\\.TXTS\\IPS.txt', 'w') as arquivo:
    for i in range(1, 255):
        ip ="192.168.0."+str(i)         
        mac_address, hostname = obter_mac_address(ip)
        if mac_address is not None and hostname is not None:
            print(ip + " - "+ mac_address +" - " + hostname) 
            arquivo.write(ip + " - "+ mac_address +" - " + hostname+"\n")
        else:
            print(ip + "- Vago")  
            arquivo.write(ip + " - Vago"+"\n")      
      


chrome_options = Options()
#chrome_options.add_argument("--headless")
chrome_options.add_argument("--start-maximized--window-position=0,0")
driver = webdriver.Chrome(chrome_options)

driver.get("http://192.168.0.1:14000/")
elemento = driver.find_element("name","usernamefld")
elemento.send_keys("giovane.adm")
elemento = driver.find_element("name","passwordfld")
elemento.send_keys("DarknessX23X")
elemento.send_keys(Keys.RETURN)
driver.get("http://192.168.0.1:14000/services_dhcp.php")
elemento = driver.find_elements(By.CLASS_NAME,"panel-title")

cont_max = int(extrair_numeros(elemento[6].text))
#cont_max = int(cont_max) -1

verificar_e_deletar_arquivo('X:\\TI\\Giovane\\Automações\\.TXTS\\MACS.txt')


for i in range(cont_max):
    driver.get("http://192.168.0.1:14000/services_dhcp_edit.php?if=lan&id="+str(i))
    mac = driver.find_element(By.NAME,"mac")
    cid = driver.find_element(By.NAME,"cid")
    ip = driver.find_element(By.NAME,"ipaddr")
    hostname = driver.find_element(By.NAME,"hostname")
    with open('X:\\TI\\Giovane\\Automações\\.TXTS\\MACS.txt', 'a') as arquivo:
        arquivo.write(mac.get_attribute('value') + ";" + cid.get_attribute('value') + ";" + ip.get_attribute('value')+";"+hostname.get_attribute('value')   + '\n')


