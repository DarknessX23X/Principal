import configparser

def ler_config_ini(caminho_arquivo):
    config = configparser.ConfigParser()
    config.read(caminho_arquivo)

    # Acessando valores
    secao = 'caminho' # Nome da seção
    host = config.get(secao, 'leitura')
    porta = config.get(secao, 'salvamento') # Converte para inteiro
    

    print(f"Host: {host}, Porta: {porta}")
    return host, porta

#Exemplo de uso:
caminho = 'E:\\Git\\Principal\\Python\\.Amostra\\config\\config.ini' # Substitua pelo caminho do seu arquivo
host, porta= ler_config_ini(caminho)