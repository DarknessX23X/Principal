import os
import re
from concurrent.futures import ThreadPoolExecutor, as_completed

# Função para verificar e extrair o CID de um IP específico
def verificar_e_extrair_cid(ip):
    caminho_rede_A = fr'\\{ip}\c$\ProgramData\AnyDesk\Service.conf'
    caminho_rede_B = fr'\\{ip}\c$\ProgramData\AnyDesk\ad_msi\Service.conf'
    conteudo = None

    if os.path.exists(caminho_rede_A) or os.path.exists(caminho_rede_B):
        try:
            with open(caminho_rede_A, 'r') as arquivo:
                conteudo = arquivo.read()
                matches = re.findall(r"ad\.telemetry\.last_cid=(\d+)", conteudo)
                numero = matches[-1] if matches else None
                return f"IP: {ip} - CID encontrado: {numero}"
        except Exception as e:
            try:
                with open(caminho_rede_B, 'r') as arquivo:
                    conteudo = arquivo.read()
                    matches = re.findall(r"ad\.telemetry\.last_cid=(\d+)", conteudo)
                    numero = matches[-1] if matches else None
                    return f"IP: {ip} - CID encontrado: {numero}"
            except Exception as e:
                return f"IP: {ip} - Erro ao ler o arquivo: {e}"
    else:
        return f"IP: {ip} - Arquivo não encontrado."

# Lista de IPs a serem verificados
ips = [f"192.168.0.{i}" for i in range(1, 255)]

# Usando ThreadPoolExecutor para processamento paralelo
with ThreadPoolExecutor(max_workers=50) as executor:  # Ajuste max_workers conforme necessário
    futures = [executor.submit(verificar_e_extrair_cid, ip) for ip in ips]

    # Exibe os resultados conforme as tarefas são concluídas
    for future in as_completed(futures):
        print(future.result())

print("Verificação concluída.")