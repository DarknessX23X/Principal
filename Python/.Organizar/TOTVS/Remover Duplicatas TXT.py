# Caminho do arquivo de origem e destino
arquivo_origem = 'NOTAS.txt'
arquivo_destino = 'NOTAS1.txt'

# Cria um conjunto para armazenar as linhas únicas
linhas_unicas = set()

# Abre o arquivo de origem em modo de leitura
with open(arquivo_origem, 'r') as origem:
    # Lê cada linha do arquivo de origem
    for linha in origem:
        # Adiciona a linha ao conjunto de linhas únicas
        linhas_unicas.add(linha)

# Abre o arquivo de destino em modo de escrita
with open(arquivo_destino, 'w') as destino:
    # Escreve as linhas únicas no arquivo de destino
    for linha in linhas_unicas:
        destino.write(linha)

print("Linhas duplicadas removidas com sucesso!")