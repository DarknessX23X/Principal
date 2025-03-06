import pandas as pd

# Caminho do arquivo Excel
input_file = 'Planilha.xlsx'

# Caminho do arquivo de texto de saída
output_file = 'saida.txt'

# Ler o arquivo Excel usando openpyxl como engine
try:
    df = pd.read_excel(input_file, engine='openpyxl')
except Exception as e:
    print(f"Erro ao ler o arquivo Excel: {e}")
    exit()

# Adicionar uma coluna vazia no início do DataFrame
df.insert(0, 'Lote Cliente', '')
df.insert(1, 'Lote Fornecedor', '')
df.insert(2, 'Tonalidade', '')
colunas_selecionadas = df.iloc[:, [0,1,2,8,12,0,9,9,0,15,15,0,0,13]]

# Exportar para um arquivo de texto, delimitado por ;
try:
    colunas_selecionadas.to_csv(output_file, index=False, header=False, sep=';')
    print(f"Arquivo exportado com sucesso para {output_file}")
except Exception as e:
    print(f"Erro ao exportar o arquivo: {e}")