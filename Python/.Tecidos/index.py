from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from openpyxl import load_workbook
import os
import pandas as pd

app = Flask(__name__)
# Configuração para uploads (ajuste o caminho conforme necessário)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Cria a pasta se ela não existir
ALLOWED_EXTENSIONS = {'xlsx'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        info1 = request.form.get("info1")  # Use get() para lidar com campos opcionais
        info2 = request.form.get("info2")
        opcao = request.form.get("opcao")

        if opcao != 'Vicunha' :
            return render_template('construção.html')
        if 'file' not in request.files:
            return "Nenhum arquivo selecionado"
        file = request.files['file']
        if file.filename == '':
            return "Nenhum arquivo selecionado"
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            try:
                df = pd.read_excel(os.path.join(app.config['UPLOAD_FOLDER'],filename), engine='openpyxl')
                print('Exito')
            except Exception as e:
                print(f"Erro ao ler o arquivo Excel: {e}")
                exit()        
            df.insert(0, 'Lote Cliente', info1)
            df.insert(1, 'Lote Fornecedor','' )
            df.insert(2, 'Tonalidade', info2)
            colunas_selecionadas = df.iloc[:, [0,1,2,8,12,1,9,9,1,15,15,1,1,13]]

# Exportar para um arquivo de texto, delimitado por ;
            try:
                caminho_arquivo = os.path.join("X:\\Tecidos\\Exportação", f"{info1}.txt")
                colunas_selecionadas.to_csv(caminho_arquivo, index=False, header=False, sep=';')
                print(f"Arquivo exportado com sucesso para 1.txt")
            except Exception as e:
                print(f"Erro ao exportar o arquivo: {e}")    
    return render_template('index.html')  # Passa os dados para um template

    

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port="8100")