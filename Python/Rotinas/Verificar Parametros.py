import os
import pyautogui
from PIL import Image
import psutil
import time
import clipboard
import pyperclip
from tabulate import tabulate
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from bs4 import BeautifulSoup
import datetime




nome_atalho = "VirtualAge.lnk"
Empresas =["001","011","012","014","016","018","017","019","025","029","032","033","040","041","049","079"]
EmpresasNome =["KAZZO - MATRIZ","KAZZO MACATUBA","DOTCA","PICOLLI - BOTUCATU","PICOLLI - AVARÉ","NOVA JEANS - PIRACICABA","PICOLLI - MACATUBA","FULVIO - BOTUCATU","KARAMBA","FULVIO - SÃO PAULO","PICOLLI - BAURU","KAZZO - BRUSQUE","KABMADEIRA","KABMADEIRA - SÃO PAULO","FULVIO - BAURU","FULVIO - ECOMMERCE"]
Paramentro1=[]
Paramentro2=[]
def procurar_cor_na_imagem(imagem, cor):
    # Abrir a imagem
    img = Image.open(imagem)

    # Converter a imagem para o modo RGB
    img_rgb = img.convert("RGB")

    # Obter as dimensões da imagem
    largura, altura = img_rgb.size

    # Percorrer todos os pixels da imagem
    for x in range(largura):
        for y in range(altura):
            # Obter a cor do pixel na posição (x, y)
            pixel = img_rgb.getpixel((x, y))

            # Verificar se a cor do pixel corresponde à cor procurada
            if pixel == cor:
                return (x, y)  # Retornar a posição do pixel

    return None  # Retornar None se a cor não for encontrada

def verificar_processo(nome_processo):
    for processo in psutil.process_iter(['name']):
        if processo.info['name'] == nome_processo:
            return True
    return False

def fechar_processo(nome_processo):
    for processo in psutil.process_iter(['name']):
        if processo.info['name'] == nome_processo:
            processo.kill()



def abrir_atalho(caminho_atalho):
    try:
        caminho_area_trabalho = os.path.expandvars('%USERPROFILE%\\Desktop')
        caminho_completo = os.path.join(caminho_area_trabalho, caminho_atalho)
        print(caminho_completo)
        os.startfile(caminho_completo)
        print("Atalho aberto com sucesso!")
       
    except Exception as e:
        print("Erro ao abrir o atalho:", str(e))

nome_processo = "ua-client.exe"
if verificar_processo(nome_processo):
      fechar_processo(nome_processo)

abrir_atalho(nome_atalho)   

while True:
        imagem_tela = ".\\Rotinas\\screenshot\\screenshot.png"
        pyautogui.screenshot(imagem_tela)
        cor_procurada = (78, 63, 44)
        posicao_cor = procurar_cor_na_imagem(imagem_tela, cor_procurada)
        if posicao_cor is None:
            continue
        else:     
            break

pyautogui.typewrite("giovane")
pyautogui.press('tab')
pyautogui.typewrite("Darkness") 
pyautogui.press('enter')
time.sleep(0.75)
pyautogui.press('1',presses=2)
pyautogui.press('enter')
time.sleep(0.75)
pyautogui.press('tab')
pyautogui.press('enter')



while True:
        imagem_tela = ".\\Rotinas\\screenshot\\screenshot1.png"
        pyautogui.screenshot(imagem_tela)
        cor_procurada = (47, 47, 47)
        posicao_cor = procurar_cor_na_imagem(imagem_tela, cor_procurada)
        if posicao_cor is None:
            continue
        else:     
            break

pyautogui.press('esc')
time.sleep(1)
pyautogui.press('N')
pyautogui.hotkey('alt', 'F')
pyautogui.press('C')

 

while True:
        imagem_tela = ".\\Rotinas\\screenshot\\screenshot2.png"
        pyautogui.screenshot(imagem_tela)
        cor_procurada = (192, 255, 255)
        posicao_cor = procurar_cor_na_imagem(imagem_tela, cor_procurada)
        if posicao_cor is None:
            continue
        else:     
            break
    
pyautogui.write('ADMFL034',interval=0.1)
pyautogui.press('F12') 

while True:
        imagem_tela = ".\\Rotinas\\screenshot\\screenshot3.png"
        pyautogui.screenshot(imagem_tela)
        cor_procurada = (192, 255, 255)
        posicao_cor = procurar_cor_na_imagem(imagem_tela, cor_procurada)
        if posicao_cor is None:
            continue
        else:     
            break
time.sleep(0.75)        
pyautogui.write('IN_BLOQ_SALDO_NEG',interval=0.1)
pyautogui.press('F4')
time.sleep(1) 
pyautogui.press('tab',presses=2)
pyautogui.hotkey('shift', 'tab')

for i in range(len(Empresas)):
    try:
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(1)
        #conteudo_copiado = clipboard.paste()        
        Paramentro1.append(clipboard.paste())
        pyautogui.press('tab')
    except pyperclip.PyperclipWindowsException:
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(1)
        #conteudo_copiado = clipboard.paste()        
        Paramentro1.append(clipboard.paste())        
        pyautogui.press('tab')
        # Se ocorrer o erro PyperclipWindowsException, continue para a próxima iteração do loop
        continue

pyautogui.press('F2') 
pyautogui.write('NR_HORA_CANCEL_NFE',interval=0.1)
pyautogui.press('F4')
time.sleep(1) 
pyautogui.press('tab',presses=2)
pyautogui.hotkey('shift', 'tab')

for i in range(len(Empresas)):
    try:
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(1)
        #conteudo_copiado = clipboard.paste()        
        Paramentro2.append(clipboard.paste())
        pyautogui.press('tab')
    except pyperclip.PyperclipWindowsException:
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(1)
        #conteudo_copiado = clipboard.paste()        
        Paramentro2.append(clipboard.paste())        
        pyautogui.press('tab')
        # Se ocorrer o erro PyperclipWindowsException, continue para a próxima iteração do loop
        continue    

#print(Empresas)
#print(Paramentro1)
#print(Paramentro2)

cabecalho = ["EMPRESA","NOME", "SALDO NEGATIVO","HORAS NFE"]

lista_unida = [list(row) for row in zip(Empresas,EmpresasNome,Paramentro1,Paramentro2)]

tabela = tabulate(lista_unida , headers=cabecalho, tablefmt="html")

tabela_com_bordas_e_linhas = f"<table style='border-collapse: collapse;'>{tabela}</table>"
tabela_com_bordas_e_linhas = tabela_com_bordas_e_linhas.replace("<tr>", "<tr style='border-bottom: 1px solid black;'>")
tabela_com_bordas_e_linhas = tabela_com_bordas_e_linhas.replace("<th>", "<th style='border: 1px solid black; padding: 8px;'>")
tabela_com_bordas_e_linhas = tabela_com_bordas_e_linhas.replace("<td>", "<td style='border: 1px solid black; padding: 8px;'>")
tabela_com_bordas_e_linhas = f"<div style='text-align: center;'><table style='width:100%;'><style>table tr:nth-child(even) {{background-color: #f2f2f2;}}</style>{tabela_com_bordas_e_linhas}</table></div>"

# Obter a data e hora atual
data_hora_atual = datetime.datetime.now()

# Converter a data e hora em uma string formatada
data_hora_formatada = data_hora_atual.strftime("%d/%m/%Y %H:%M:%S")

# Configurar o e-mail
de = "robozinho@kazzo2.com.br"
para = "suporte@kazzo.com.br"
assunto = "Parametros - " + data_hora_formatada
mensagem = f"""
<html>
<head></head>
<body>
    {tabela_com_bordas_e_linhas}
    <style>
         th {{
            background-color: red;
        }}
<b style="color: #ea0d14; font-size: 20px">Robozinho</b> <br>
<a href="http://www.kazzo.com.br/Views/"><img src="https://i.imgur.com/oJthMrZ.png" alt="Configurado no Servidor" width="129" height="40"/></a><br>
Tel.: +55 14 32989898 Ramal: 191<br>
Endereço: Rua Pedro Monte 185 <br>
Macatuba - SP <br>
<a href="https://www.instagram.com/kazzoconfeccoes/"><img src="https://i.imgur.com/AYsKYWf.png" alt="Kazzo Confecções" width="330" height="50"/></a><br>
<i style="color: #7f7f7f; font-size: 12px; text-align: justify;">Antes de imprimir, pense em sua responsabilidade e compromisso com o Meio Ambiente. Este documento pode incluir informação confidencial e de propriedade restrita da Kazzo Confecções e apenas pode ser lido por aquele(s) a qual o mesmo tenha sido endereçado. Se você recebeu essa mensagem de e-mail indevidamente, por favor, avise-nos imediatamente. Quaisquer opiniões ou informações expressadas neste e-mail pertencem ao seu remetente e não necessariamente coincidem com aquelas da Kazzo Confecções. Este documento não pode ser reproduzido, copiado, distribuído, publicado ou modificado por terceiros, sem a prévia autorização por escrito da Kazzo Confecções.</i>        
</body>
</html>
"""

# Criar o objeto MIMEMultipart
email = MIMEMultipart()
nome_remetente = "Robozinho - Kazzo"

# Configurar os campos do e-mail
email["From"] =  f"{nome_remetente} <{de}>"
email["To"] = para
email["Subject"] = assunto

# Adicionar a mensagem como texto HTML
email.attach(MIMEText(mensagem, "html"))

# Enviar o e-mail usando um servidor SMTP
servidor_smtp = "smtp.kazzo2.com.br"
porta_smtp = 587
usuario_smtp = "robozinho@kazzo2.com.br"
senha_smtp = "TI@Kazzo2024"

with smtplib.SMTP(servidor_smtp, porta_smtp) as servidor:
    servidor.starttls()
    servidor.login(usuario_smtp, senha_smtp)
    servidor.send_message(email)

print("E-mail enviado com sucesso!")
nome_processo = "ua-client.exe"
if verificar_processo(nome_processo):
      fechar_processo(nome_processo)
