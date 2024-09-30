import subprocess
import re
import openpyxl
import shutil
from timeout_decorator import timeout
import platform

arquivo_excel = '../Informacoes.xlsx'
workbook = openpyxl.load_workbook(arquivo_excel)
planilha = workbook['Planilha1']

caminho_arquivo_origem = 'anydesk.bat'

tempo_maximo = 10

def teste_ping(host):
    resultado_ping = subprocess.run(['ping', '-n', '5', '-w', '5000', host], capture_output=True)
    sistema_operacional = platform.system()
    parametros = ['-n', '1'] if sistema_operacional.lower() == 'windows' else ['-c', '1']
    comando_ping = ['ping'] + parametros + [host]
    resultado_ping = subprocess.run(comando_ping, capture_output=True)
    print(resultado_ping)
    return resultado_ping.returncode == 0





for i in range(130, 133):
    ip = f"192.168.0.{i}"
    print(ip)
    cmd_user = "cmdkey /add:"f"{ip} /user:kazzo1\\administrador /pass: Tec2024K@3,14colli"
    resultado = subprocess.check_output(cmd_user, shell=True)
    print(resultado.decode('latin-1'))
    caminho_pasta_destino = "\\\\"f"{ip}\\c$\\config\\scripts\\anydesk.bat"
    if teste_ping(ip):
        cp_arquivos = "copy "f"{caminho_arquivo_origem} "f"{caminho_pasta_destino}" 
        resultado = subprocess.check_output(cp_arquivos, shell=True)

        print(resultado.decode('latin-1'))

X=2
for i in range(130,133):
    ip = f"192.168.0.{i}"
    cmd_hostname = "psexec \\\\"f"{ip} cmd /c hostname"
    cmd_mac = "getmac /s "f"{ip} /u kazzo1\\administrador /p Tec2024K@3,14colli"
    cmd_anydesk = "psexec \\\\"f"{ip} cmd /c c:\\config\\scripts\\anydesk.bat"
    try:
        resultado = subprocess.check_output(cmd_anydesk, shell=True)
        anydesk= (resultado.decode('utf-8'))
        resultado = subprocess.check_output(cmd_mac, shell=True)
        mac= (resultado.decode('latin-1'))
        terceira_linha = re.search(r'\b([\da-fA-F]{2}[:-]){5}[\da-fA-F]{2}\b', mac).group() 
        resultado = re.search(r'www.sysinternals.com\s+(.*)$', anydesk, re.M)   
        texto_extraido = resultado.group(0)
        anydesk = re.findall(r'\d+', texto_extraido) 
        resultado = subprocess.check_output(cmd_hostname, shell=True)
        hostname= (resultado.decode('latin-1'))
        hostname = re.search(r'www.sysinternals.com\s+(.*)$', hostname, re.M)
        hostname = hostname.group(0)
        hostname = hostname[20:35]

        planilha['A'+str(X)].value = ip
        planilha['B'+str(X)].value = hostname
        planilha['C'+str(X)].value = terceira_linha
        planilha['D'+str(X)].value = numeros_formatados = ''.join(anydesk).strip('[]')
        X=X+1

    

    except subprocess.CalledProcessError as erro:
        print(f"Ocorreu um erro ao executar o comando psexec: {erro}")
        


workbook.save(arquivo_excel)

for i in range(130, 133):
    ip = f"192.168.0.{i}"
    cmd_user = "cmdkey /delete:"f"{ip}"
    resultado = subprocess.check_output(cmd_user, shell=True)
    print(resultado.decode('latin-1'))
