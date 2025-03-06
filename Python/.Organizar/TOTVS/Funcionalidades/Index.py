from flask import Flask, render_template,request
from selenium import webdriver
from selenium.webdriver import ActionChains
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


app = Flask(__name__)

def next_ip(ip):
    # Dividindo o IP em octetos
    octets = ip.split('.')
  
    # Convertendo cada octeto em um número inteiro
    octets = [int(octet) for octet in octets]

    # Incrementando o último octeto
    octets[-1] += 1

    # Verificando se o octeto excede 255 e tratando o overflow
    for i in range(3, 0, -1):
        if octets[i] > 255:
            octets[i] = 0
            octets[i-1] += 1

    # Convertendo os octetos de volta para strings e juntando-os com pontos
    next_ip = '.'.join(str(octet) for octet in octets)

    return next_ip

@app.route('/')
def home():
    return render_template('index.html', options=get_options())
def get_options():
    with open('teste.txt', 'r') as file:
        options = [line.strip() for line in file.readlines() if line.strip()]
    return options




@app.route('/open_program', methods=['POST'])


def open_program():
    nome = request.form['nome']
    mac = request.form['mac']
    desc = request.form['desc']
    opcoes = request.form.get('opcoes')
    print (nome)
    print (mac)
    print (opcoes)
    
    
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    #chrome_options.add_argument("--start-maximized--window-position=0,0--ignore-exceptions")
    driver = webdriver.Chrome(chrome_options)

    driver.get("http://192.168.0.27:14000/") 
    elemento = driver.find_element("name","usernamefld")
    elemento.send_keys("giovane")
    elemento = driver.find_element("name","passwordfld")
    elemento.send_keys("DarknessX23X")
    elemento.send_keys(Keys.RETURN)
    driver.get("http://192.168.0.27:14000/services_dhcp.php")
    elemento = driver.find_elements(By.CLASS_NAME,"panel-title")
    elements = driver.find_elements(By.CSS_SELECTOR,'[role="presentation"]')
    sorted_elements = sorted(elements, key=lambda e: e.text)
    file_path = "./teste.txt"
   

    with open(file_path, "w") as file:
        for element in sorted_elements:
            file.write(element.text + "\n")  

    text_to_find = "TI"    
    #element = driver.find_elements(By.XPATH, '//a[text()="{}"]'.format(text_to_find))  
    for element in elements:
         nested_elements = element.find_elements(By.TAG_NAME,'a')
         for nested_element in nested_elements:
                text = nested_element.text
                if text == opcoes:
                    print(nested_element.get_attribute('href'))
                    link = nested_element.get_attribute('href')
                    #driver.get(nested_element.get_attribute('href'))

    driver.get(link)

    elements = driver.find_elements(By.TAG_NAME,'tr')
    for i, element in enumerate(elements):
        ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
        ip_matches = re.findall(ip_pattern, element.text)
        if i == len(elements) - 1:
            ip_string = ', '.join(ip_matches)
            ip_string = ip_string.replace('[', '').replace(']', '').replace("'", "")
            substrings = ip_string.split(", ")
            substrings_unicas = []
            for substring in substrings:
                if substring not in substrings_unicas:
                    substrings_unicas.append(substring)

            string_unica = ", ".join(substrings_unicas)
            print(string_unica)
            


    ip = next_ip(string_unica)
    print(ip)        

    element = driver.find_element(By.CSS_SELECTOR,'a.btn.btn-sm.btn-success')
    element.click()

    elemento = driver.find_element("name","ipaddr")
    elemento.send_keys(ip)
    elemento = driver.find_element("name","mac")
    elemento.send_keys(mac)
    elemento = driver.find_element("name","cid")
    elemento.send_keys(nome)
    elemento = driver.find_element("name","hostname")
    elemento.send_keys(nome)
    elemento = driver.find_element("name","descr")
    elemento.send_keys(desc)
    elemento = driver.find_element("name","save")
    elemento.click()
    time.sleep(8)
    elemento = driver.find_element(By.NAME,"apply")
    elemento.click()
    time.sleep(8)

    driver.quit()  
   
    
    return render_template('index.html', options=get_options())
def get_options():
    with open('teste.txt', 'r') as file:
        options = [line.strip() for line in file.readlines() if line.strip()]
    return options
    


if __name__ == '__main__':
    app.run(host='0.0.0.0',port='8082')