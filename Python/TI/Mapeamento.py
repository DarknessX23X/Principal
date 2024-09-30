import win32wnet

# Substitua 'caminho_da_pasta' pelo caminho da pasta que deseja mapear
caminho_da_pasta = r'\\192.168.0.53\Aplicativos'

# Substitua 'X:' pela letra que deseja atribuir ao mapeamento
letra_mapeada = 'Z:'

# Mapeia a pasta da rede com a letra escolhida
try:
    win32wnet.WNetAddConnection2(0, None, caminho_da_pasta, letra_mapeada)
    print(f'Mapeamento bem-sucedido! A pasta da rede foi mapeada para a letra {letra_mapeada}.')
except Exception as e:
    print(f'Erro ao mapear a pasta da rede: {e}')