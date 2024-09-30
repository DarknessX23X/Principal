from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
import time

# Definir o caminho para o WebDriver
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(chrome_options)

# Abrir um site
driver.get('http://192.168.0.209/glpi')
elemento = driver.find_element("id","login_name")
elemento.send_keys("glpi")
elemento = driver.find_element("id","login_password")
elemento.send_keys("Gerente1@")
elemento.send_keys(Keys.RETURN)


for numero in range(16, 119):
    driver.get("http://192.168.0.209/glpi/front/computer.form.php?id="f"{numero}")
    time.sleep(30)
    input_element = driver.find_element(By.NAME, 'name')
    valor_input = input_element.get_attribute("value")
    input_element.clear()
    texto_em_maiusculo = valor_input.replace(".kazzo1.sys", "").upper()
    input_element.send_keys(texto_em_maiusculo) 
    input_element = driver.find_element(By.NAME, 'update')
    input_element.click()
    time.sleep(30)

'''
link = driver.find_element(By.PARTIAL_LINK_TEXT, 'Sistemas operativos')
link.click()
'''

time.sleep(100)