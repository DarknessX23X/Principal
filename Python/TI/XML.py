import os
import shutil

def copiar_arquivos_xml(origem, destino):
    for pasta_atual, sub_pastas, arquivos in os.walk(origem):
        for arquivo in arquivos:
            if arquivo.endswith('.xml'):
                caminho_completo_origem = os.path.join(pasta_atual, arquivo)
                caminho_completo_destino = os.path.join(destino, arquivo)
                
                if not os.path.exists(caminho_completo_destino):  # Verifica se o arquivo destino não existe
                    shutil.copy(caminho_completo_origem, caminho_completo_destino)
                    print(f"Arquivo copiado: {arquivo}")
                else:
                    print(f"Arquivo {arquivo} já existe no destino. Pulando para o próximo arquivo.")

origem = "X:\\FISCAL"
destino = "E:\\XML2"

copiar_arquivos_xml(origem, destino)