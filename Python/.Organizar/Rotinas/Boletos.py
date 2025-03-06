from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import os
from urllib.parse import urlparse, parse_qs
import pdfkit



import requests

chrome_options = Options()
chrome_options.add_argument("--headless")
# Inicializar o driver do Selenium
driver = webdriver.Chrome()
driver.maximize_window()

# Abrir o site
driver.get("https://totvscst.zendesk.com/hc/pt-br#autoatendimento")

elemento_referencia = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "username"))
)

username_field = driver.find_element(By.ID, "username")
username_field.send_keys("renata@kazzo.com.br")
password_field = driver.find_element(By.ID, "password")
password_field.send_keys("K@zzo3214")
password_field.send_keys(Keys.ENTER)

time.sleep(20)

driver.get("https://totvscst.zendesk.com/hc/pt-br/#/consultaimpressao")   

time.sleep(25)


div_elements = driver.find_elements(By.XPATH, "//div[@title='Imprimir']")
script = "$('#opcoes-impressao').fadeOut('fast');"
quantidade_elementos = len(div_elements)
print("Quantidade de elementos encontrados:", quantidade_elementos)



for div in div_elements:
    # Clicar no elemento 
    driver.execute_script(script)   
    actions = ActionChains(driver)
    actions.move_to_element(div).click().perform()
    time.sleep(10)    
    li = driver.find_element(By.XPATH, "//div[contains(@class, 'cst-modal')]//li[@id='print-nfe']")
    actions = ActionChains(driver)
    actions.move_to_element(li).click().perform()
    time.sleep(2)
    tab_handles = driver.window_handles
    num_tabs = len(driver.window_handles)    
    driver.switch_to.window(tab_handles[0]) 
    li = driver.find_element(By.XPATH, "//div[contains(@class, 'cst-modal')]//li[@id='print-boleto']")
    actions = ActionChains(driver)
    actions.move_to_element(li).click().perform()
    time.sleep(2)
    driver.switch_to.window(tab_handles[0]) 
    driver.execute_script(script)

num_tabs = num_tabs-1
x=1
for i in range(num_tabs) :    
    
    driver.switch_to.window(tab_handles[x]) 
    pdf_url=driver.current_url
    
    response = requests.get(pdf_url)

    caminho = "X:\\TI\\Boletos\\TOTVS"


    if response.status_code == 200:
    # Extrair o nome do arquivo do URL        
        
        parsed_link = urlparse(pdf_url)
        query_params = parse_qs(parsed_link.fragment)
        c_titulo = query_params.get("C_TITULO", [None])[0]

        if c_titulo is None:
            parts = pdf_url.split("/")
            valor = parts[4]
            file_name = "Nota_"+valor
        else:
            file_name = "Boleto_" + c_titulo          
            
        caminho_completo = os.path.join(caminho, f"{file_name}.pdf")    

    # Salvar o arquivo PDF
        if "Nota" in caminho_completo: 
         with open(caminho_completo, "wb") as file:
            file.write(response.content) 
            print(f"O arquivo PDF '{file_name}.pdf' foi salvo com sucesso.")
            x += 1
        else:
           pdfkit.from_url(pdf_url, caminho_completo,configuration=pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin'))
           print(f"O arquivo PDF '{file_name}.pdf' foi salvo com sucesso.")
           x += 1     

    else:
     print("Não foi possível obter o arquivo PDF.")
   
driver.quit()  
