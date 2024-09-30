from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pyautogui
import time
# Inicializa o driver do Selenium (certifique-se de ter o driver do navegador instalado)
driver = webdriver.Chrome()

# Abre uma página da web
driver.get('http://192.168.3.1:14000/webpages/login.html')
element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID,"login-username")))
element.click();
element.send_keys("admin")
element.send_keys(Keys.TAB)
#pyautogui.press('tab')
#time.sleep(1)
pyautogui.write("K@3,14colli")
element.send_keys(Keys.RETURN)
#element.submit()
time.sleep(4)
element = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.ID,"menu-advanced-basic-setting-li")))
element.click()
time.sleep(4)
element = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.NAME,"lan-settings")))
element.click()
time.sleep(4)
element = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH,"//span[text()='DHCP Client List']")))
element.click()
time.sleep(2)
elemento = driver.find_elements(By.CLASS_NAME,"grid-content-data")
valores = []
valores_filtro=[]
sublistas  = []

for tag in elemento:
    valor = tag.text
    valores.append(valor)
   

#valores_filtro= list(filter(lambda x: x !="",valores))

for i in range(0, len(valores), 4):
    sublista = valores[i:i+4]
    sublistas.append(sublista)
    
    
delimitador = " "  
substrings = sublistas[i][0].split(delimitador)
valores_filtro =[]

for substring in substrings:
    valores_filtro.append(substring)

for i in range(0, len(valores_filtro), 5):
    sublista = valores_filtro[i:i+5]
    sublistas.append(sublista)


#exit()

#print(valores_filtro[0])
for i in range(len(valores_filtro)):
    with open("C:\\config\\teste.txt", "a") as arquivo:
        arquivo.write(str(valores_filtro[i])+' ')     
        #arquivo.write(str(valores_filtro[i+4])+'\n') 
       # arquivo.write(str(sublistas[i][2]))
        #arquivo.write(str(sublistas[i][3])+'\n')
time.sleep(100)


# Fecha o navegador
driver.quit()