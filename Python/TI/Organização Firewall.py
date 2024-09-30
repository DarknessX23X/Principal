from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from openpyxl import Workbook
import csv

with open('C:\\config\\Firewall.csv', 'r') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv, delimiter=';')


    coluna1 = []
    coluna2 = []
    coluna3 = []
    coluna4 = []

    for linha in leitor_csv:
        # Adicione os dados das colunas às listas correspondentes
        coluna1.append(linha[0])
        coluna2.append(linha[1])
        coluna3.append(linha[2])
        coluna4.append(linha[3])

qtde = len(coluna1) + 1

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(chrome_options)
driver.get("http://192.168.0.1:14000/")
elemento = driver.find_element("name","usernamefld")
elemento.send_keys("giovane.adm")
elemento = driver.find_element("name","passwordfld")
elemento.send_keys("DarknessX23X")
elemento.send_keys(Keys.RETURN)
driver.get("http://192.168.0.1:14000/services_dhcp.php")
elemento = driver.find_elements(By.TAG_NAME,"td")


for i in range(qtde) :   
    driver.get("http://192.168.0.1:14000/services_dhcp_edit.php?if=lan&id="+str(i))
    elemento = driver.find_element(By.NAME,"ipaddr") 
    print(elemento.get_attribute("value"))   
    posicao = coluna2.index(elemento.get_attribute("value")) 
    elemento = driver.find_element(By.NAME,"cid")  
    elemento.clear()
    elemento.send_keys(coluna1[posicao])
    elemento = driver.find_element(By.NAME,"hostname")  
    elemento.clear()
    elemento.send_keys(coluna3[posicao])
    elemento = driver.find_element(By.NAME,"descr")  
    elemento.clear()
    elemento.send_keys(coluna4[posicao])
    elemento = driver.find_element(By.NAME,"save")
    elemento.click()
    time.sleep(0.5)
    elemento = driver.find_element(By.NAME,"apply")
    elemento.click()
    #print(coluna1[posicao] + coluna2[posicao]+coluna3[posicao]+coluna4[posicao])
    

#time.sleep(100)
