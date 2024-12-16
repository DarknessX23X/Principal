from flask import Flask, render_template, request
import os

app = Flask(__name__)

diretorio = 'X:\\TI\\Giovane\\Amostra'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        arquivo_selecionado = request.form.get('arquivo')
        arquivos = os.listdir(diretorio)
        arquivos_csv = [arquivo for arquivo in arquivos if arquivo.lower().endswith(('.csv', '.CSV'))]
        arquivos_sem_extensao = [os.path.splitext(arquivo)[0] for arquivo in arquivos_csv]
        arquivos_ordenados = sorted(arquivos_sem_extensao)
        print(arquivo_selecionado)
        return render_template('index.html', arquivo_selecionado=arquivo_selecionado, arquivos=arquivos_ordenados)
    else:
        arquivos = os.listdir(diretorio)
        arquivos_csv = [arquivo for arquivo in arquivos if arquivo.lower().endswith(('.csv', '.CSV'))]
        arquivos_sem_extensao = [os.path.splitext(arquivo)[0] for arquivo in arquivos_csv]
        arquivos_ordenados = sorted(arquivos_sem_extensao)
        return render_template('index.html', arquivos=arquivos_ordenados)

if __name__ == '__main__':
    app.run(debug=True)