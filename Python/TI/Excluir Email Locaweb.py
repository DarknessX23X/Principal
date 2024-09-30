from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import pyautogui

options = Options()
options.add_argument("--start-maximized")

url = "https://webmail-seguro.com.br/kazzo2.com.br/"
campo_id = "rcmloginuser"
senha_id = "rcmloginpwd"
checkbox_id ="lm-act-checkbox"
texto = "ti@kazzo2.com.br"
senha = "TI@Kazzo2019"
ultima_pagina ="rcmbtnnavlast"


driver = webdriver.Chrome(options=options)  # Certifique-se de que o Chrome WebDriver esteja instalado e o caminho seja configurado corretamente
driver.get(url)
campo_input = driver.find_element(By.ID, campo_id)
campo_input.send_keys(texto)
senha_input = driver.find_element(By.ID, senha_id)
senha_input.send_keys(senha)
time.sleep(30)
ultimo_input = driver.find_element(By.ID, ultima_pagina)
ultimo_input.click()
time.sleep(3)
num = int(input("Digite um número: "))

for i in range(1, num+1):
    time.sleep(6)
    pyautogui.click(234, 231)
    pyautogui.click(500, 226)

time.sleep(60)





