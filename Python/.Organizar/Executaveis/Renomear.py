import os

caminho = "E:\\ARQ2\\000003_9_nfe.xml"
novo_nome = "novo_nome.xml"

diretorio = os.path.dirname(caminho)
novo_caminho = os.path.join(diretorio, novo_nome)

os.rename(caminho, novo_caminho)