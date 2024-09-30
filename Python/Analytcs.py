from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

tempo_de_espera_para_encontrar_elementos = 10

btnLogin = '//*[text()="Login"]'

# Inicializa o driver do Chrome
driver = webdriver.Chrome()

# Abre o site
driver.get("https://analytics.totvs.com.br/admin/load/#/workspaces/agzqh2czew4la2t38vkqeoqtx5n50qwt")
time.sleep(3)


# Encontra o campo chamado "email" pelo atributo "name"
email_field = driver.find_element(By.NAME, "email")
email_field.send_keys("renata@kazzo.com.br")
email_field = driver.find_element(By.NAME, "password")
email_field.send_keys("K@zzo3214")
WebDriverWait(driver, tempo_de_espera_para_encontrar_elementos).until(EC.element_to_be_clickable((By.XPATH, btnLogin))).click()


time.sleep(1000)
# Fecha o navegador
driver.quit()