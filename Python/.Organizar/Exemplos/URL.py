from urllib.parse import urlparse, parse_qs
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pdfkit
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains


options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Executar em modo headless (sem interface gráfica)
driver = webdriver.Chrome()

driver.get("https://totvscst.zendesk.com/hc/pt-br#autoatendimento")

elemento_referencia = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "username"))
)

username_field = driver.find_element(By.ID, "username")
username_field.send_keys("renata@kazzo.com.br")
password_field = driver.find_element(By.ID, "password")
password_field.send_keys("K@zzo3214")
password_field.send_keys(Keys.ENTER)

time.sleep(15)
link = "https://totvscst.zendesk.com/hc/pt-br/#/visualizadocumento?C_CLIENTE=TEVXU0&C_EMPRESA=00&C_FILIAL=00001003100&C_NUM=000008750&C_PARCELA=&C_PREFX=UNI&C_LOJA=00&C_TITULO=8750&DOC_TYPE=boleto"

driver.get(link)


elemento_referencia = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "boleto1"))
)

ActionChains(driver).context_click(elemento_referencia).perform()
ActionChains(driver).send_keys('p').perform()

driver.implicitly_wait(5)

select_element = driver.find_element(By.CLASS_NAME,"md-select")

select = Select(select_element)

select.select_by_value('pdf')

time.sleep(1000)

print("3")