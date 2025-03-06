from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
import time
import pandas as pd

chrome_options = Options()
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(chrome_options)
driver.get("http://192.168.0.209/glpi/front/user.form.php")
elemento = driver.find_element("id","login_name")
elemento.send_keys("glpi")
elemento = driver.find_element("id","login_password")
elemento.send_keys("Gerente1@")
elemento.send_keys(Keys.RETURN)


df = pd.read_csv("X:\\TI\\TI - Usuarios - Chamados.csv", delimiter=";")

for index, row in enumerate(df.iterrows()):
    time.sleep(10)
    coluna1 = row[1][0]  # acessa a primeira coluna
    coluna2 = row[1][1]  # acessa a segunda coluna
    coluna3 = row[1][2]  # acessa a terceira coluna

    elemento = driver.find_element("id","name")
    elemento.send_keys(coluna1)
    elemento = driver.find_element("name","firstname")
    elemento.send_keys(coluna2)
    elemento = driver.find_element("name","password")
    elemento.send_keys("123")
    elemento = driver.find_element("name","password2")
    elemento.send_keys("123")
    elemento = driver.find_element("name","_useremails[-1]")
    elemento.send_keys(coluna3)
    elemento = driver.find_element("name","add")
    elemento.click()   


    print(f"Registro {index+1}: {coluna1}, {coluna2}, {coluna3}")



#elemento = WebDriverWait(driver, 10).until(driver.find_element("id","name"))




time.sleep(100)