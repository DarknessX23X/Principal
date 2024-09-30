from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re
import numpy as np
from openpyxl import Workbook
from openpyxl import load_workbook
#Variaveis
valores = []
numerosl = []
numerosa = []
textoe = []
textop = []
textoa=[]
textob=[]
remover ='Linha 1 inativa'
remover2 = '1 linhas em uso'
remover3 = "'0'"


# Inicializa o driver do Chrome
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
#options.add_argument('--start-maximized')
#options.add_argument('--headless')
driver = webdriver.Chrome(options)

# Abre o Chrome
driver.get("https://192.168.0.40/fop2/?exten=500&pass=500")
time.sleep(5)
elemento = driver.find_elements(By.CLASS_NAME,'labelname')

for tag in elemento:
        valores.append(tag.text)
        

novo_array = [x for x in valores if x != remover]   


for i in range(len(novo_array)):
    # Substitui a letra pelo vazio em cada elemento
    novo_array[i] = novo_array[i].replace('√\n', '')
    novo_array[i] = novo_array[i].replace(' (', '(')
    novo_array[i] = novo_array[i].replace(' /', '/')
    novo_array[i] = novo_array[i].replace('/ ', '/')



  
textoe=np.array(novo_array)



for i in range(len(textoe)):
      numerosl.append (re.findall(r'\d+', novo_array[i]))
      textop.append (re.findall(r'[A-Za-z/(.*?)\s*ç*]+', textoe[i]))


comprimento_maximo = max(len(sublista) for sublista in numerosl)
lista_corrigida = [sublista + [0] * (comprimento_maximo - len(sublista)) for sublista in numerosl]
numerosa = [x for x in lista_corrigida if x != remover3]   
numerosa=np.array(numerosa)
numerosa = np.array([sublista[0] for sublista in numerosa])
numerosa = list(filter(lambda x: x != '0', numerosa))
numerosa = np.delete(numerosa, np.char.startswith(numerosa, "5000"))
numerosa = np.delete(numerosa, np.char.startswith(numerosa, "5001"))
numerosa = np.delete(numerosa, np.char.startswith(numerosa, "8000"))
numerosa = np.delete(numerosa, np.char.startswith(numerosa, "0"))
numerosa = np.delete(numerosa, np.where((numerosa == "1") | (numerosa == "2")))



comprimento_maximo = max(len(sublista) for sublista in textop)
lista_corrigida = [sublista + [0] * (comprimento_maximo - len(sublista)) for sublista in textop]
textoa = np.array(lista_corrigida)
textoa = np.char.strip(textoa)
#textoa = np.char.replace(textoa ,'0','')
textoa = np.char.strip(textoa)
primeiros_itens = np.array([sublista[0] for sublista in textoa])
primeiros_itens = list(filter(lambda x: x != '0', primeiros_itens))


primeiros_itens = np.delete(primeiros_itens, np.char.startswith(primeiros_itens, "s"))
primeiros_itens = np.delete(primeiros_itens, np.char.startswith(primeiros_itens, "SIP"))
primeiros_itens = np.delete(primeiros_itens, np.char.startswith(primeiros_itens, "GERAL"))
primeiros_itens = np.delete(primeiros_itens, np.char.startswith(primeiros_itens, "Telefonista"))
primeiros_itens = np.delete(primeiros_itens, np.char.startswith(primeiros_itens, "Portaria"))
primeiros_itens = np.delete(primeiros_itens, np.char.startswith(primeiros_itens, "linhas"))

for i in range(len(primeiros_itens)):
      numerosl.append (re.findall(r'\d+', primeiros_itens[i]))



workbook = load_workbook("X:\\TI\\Giovane\\ramais.xlsx")
sheet = workbook.active

for i in range(len(numerosa)):
        sheet["A"+str(i+2)] = numerosa[i]
        sheet["D"+str(i+2)] = numerosa[i]
        sheet["G"+str(i+2)] = numerosa[i]
for i in range(len(primeiros_itens)):
        sheet["B"+str(i+2)] = primeiros_itens[i]
        sheet["E"+str(i+2)] = primeiros_itens[i]
        sheet["H"+str(i+2)] = primeiros_itens[i]
        



workbook.save("X:\\TI\\Giovane\\ramais_final.xlsx")

#print(numerosa)
#print(primeiros_itens)



#print(numerosl)

exit()
    
#textoe=np.array(textoe)

print(numeros)
print(textoe)


#time.sleep(20)


# Fecha o navegador
driver.quit()