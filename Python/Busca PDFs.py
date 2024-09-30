import os
import shutil

def procurar_arquivos(nome_arquivo_txt, pasta_origem, pasta_destino):
      contador = 1
      with open(nome_arquivo_txt, 'r') as file:
            for line in file:
                nome_arquivo = line.strip() + '.pdf'
                if os.path.exists(os.path.join(pasta_origem, nome_arquivo)):
                    novo_nome = f'1 - Remessa SC para Macatuba - Nota {contador}.pdf'
                    shutil.copy(os.path.join(pasta_origem, nome_arquivo), os.path.join(pasta_destino, novo_nome))
                    print(f'Arquivo {nome_arquivo} renomeado para {novo_nome}')                 
                    contador += 1

def procurar_arquivos2(nome_arquivo_txt, pasta_origem, pasta_destino):
      contador = 1
      with open(nome_arquivo_txt, 'r') as file:
            for line in file:
                nome_arquivo = line.strip() + '.pdf'
                if os.path.exists(os.path.join(pasta_origem, nome_arquivo)):
                    novo_nome = f'2 - Remessa Macatuba para Faccao - Nota {contador}.pdf'
                    shutil.copy(os.path.join(pasta_origem, nome_arquivo), os.path.join(pasta_destino, novo_nome))
                    print(f'Arquivo {nome_arquivo} renomeado para {novo_nome}')                 
                    contador += 1

def procurar_arquivos3(nome_arquivo_txt, pasta_origem, pasta_destino):
      contador = 1
      with open(nome_arquivo_txt, 'r') as file:
            for line in file:
                nome_arquivo = line.strip() + '.pdf'
                if os.path.exists(os.path.join(pasta_origem, nome_arquivo)):
                    novo_nome = f'3 - Remessa Faccao para Macatuba - Nota {contador}.pdf'
                    shutil.copy(os.path.join(pasta_origem, nome_arquivo), os.path.join(pasta_destino, novo_nome))
                    print(f'Arquivo {nome_arquivo} renomeado para {novo_nome}')                 
                    contador += 1

def procurar_arquivos4(nome_arquivo_txt, pasta_origem, pasta_destino):
      contador = 1
      with open(nome_arquivo_txt, 'r') as file:
            for line in file:
                nome_arquivo = line.strip() + '.pdf'
                if os.path.exists(os.path.join(pasta_origem, nome_arquivo)):
                    novo_nome = f'4 - Retorno de Macatuba para SC - Venda {contador}.pdf'
                    shutil.copy(os.path.join(pasta_origem, nome_arquivo), os.path.join(pasta_destino, novo_nome))
                    print(f'Arquivo {nome_arquivo} renomeado para {novo_nome}')                 
                    contador += 1          

def procurar_arquivos5(nome_arquivo_txt, pasta_origem, pasta_destino):
      contador = 1
      with open(nome_arquivo_txt, 'r') as file:
            for line in file:
                nome_arquivo = line.strip() + '.pdf'
                if os.path.exists(os.path.join(pasta_origem, nome_arquivo)):
                    novo_nome = f'5 - Matriz para Magazine - CTE.pdf'
                    shutil.copy(os.path.join(pasta_origem, nome_arquivo), os.path.join(pasta_destino, novo_nome))
                    print(f'Arquivo {nome_arquivo} renomeado para {novo_nome}')                 
                    contador += 1                    
          



# Exemplo de uso
nome_arquivo_txt = 'NOTAS3.txt'
pasta_origem = 'X:\\Fiscal\\98 - Fiscal\\PDF'
pasta_destino = 'C:\\Config\\XML'

procurar_arquivos2(nome_arquivo_txt, pasta_origem, pasta_destino)
#procurar_arquivos5(nome_arquivo_txt, pasta_origem, pasta_destino)