from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
import os, re,time
from openpyxl import Workbook
from ping3 import ping
import subprocess
import re
from scapy.all import ARP, Ether, srp
import socket
import csv


with open('X:\\TI\\Giovane\\Automações\\.TXTS\\MACS.csv', 'r') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv, delimiter=';')


    coluna1 = []
    coluna2 = []

    for linha in leitor_csv:
        # Adicione os dados das colunas às listas correspondentes
        coluna1.append(linha[0])
        coluna2.append(linha[1])

#print(coluna1)
#print(coluna2)


chrome_options = Options()
#chrome_options.add_argument("--headless")
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(chrome_options)

driver.get("http://192.168.0.1:14000/")
elemento = driver.find_element("name","usernamefld")
elemento.send_keys("giovane.adm")
elemento = driver.find_element("name","passwordfld")
elemento.send_keys("DarknessX23X")
elemento.send_keys(Keys.RETURN)
for i in range(255):
    driver.get("http://192.168.0.1:14000/services_dnsmasq_edit.php?id="+str(i))
    elemento = driver.find_element(By.NAME,"host")
    elemento.clear()
    elemento.send_keys(coluna2[i])
    elemento = driver.find_element(By.NAME,"domain")
    elemento.clear()
    elemento.send_keys("KAZZO1.SYS")
    elemento = driver.find_element(By.NAME,"ip")
    elemento.clear()
    elemento.send_keys(coluna1[i])
    elemento = driver.find_element(By.NAME,"descr")
    elemento.clear()
    elemento.send_keys(coluna2[i])
    elemento = driver.find_element(By.NAME,"save")
    elemento.click()
    time.sleep(5)
    elemento = driver.find_element(By.NAME,"apply")
    elemento.click()


'''
driver.get("http://192.168.0.1:14000/")
elemento = driver.find_element("name","usernamefld")
elemento.send_keys("giovane.adm")
elemento = driver.find_element("name","passwordfld")
elemento.send_keys("DarknessX23X")
elemento.send_keys(Keys.RETURN)
for i in range(113):    
    driver.get("http://192.168.0.1:14000/services_dnsmasq.php")
    elemento = driver.find_element(By.CSS_SELECTOR,".fa.fa-trash")
    elemento.click()
    alert = Alert(driver)
    alert.accept()
    time.sleep(2)
    elemento = driver.find_element(By.NAME,"apply")
    elemento.click()
'''

time.sleep(100)