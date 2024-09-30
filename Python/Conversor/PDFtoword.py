import tabula
import pandas as pd
import openpyxl
from tkinter import Tk
from tkinter import filedialog
import os



def convert_pdf_to_xlsx(input_pdf_path, output_xlsx_path):
    dfs = tabula.read_pdf(input_pdf_path, pages='all')
    writer = pd.ExcelWriter(output_xlsx_path, engine='xlsxwriter')

    for i, df in enumerate(dfs):
        df.to_excel(writer, sheet_name=f'Page{i+1}', index=False)

    writer._save()


root = Tk()
root.withdraw()

# Abre o diálogo para seleção da pasta
folder_selected = filedialog.askdirectory(title="Selecione a pasta onde estão os arquivos PDF")

# Caminho do arquivo PDF de entrada
pdf_files = [file for file in os.listdir(folder_selected) if file.endswith(".pdf")]

# Chamada da função para converter o PDF em CSV
if folder_selected:
    # Lista de arquivos PDF na pasta selecionada
    pdf_files = [file for file in os.listdir(folder_selected) if file.endswith(".pdf")]

    if not pdf_files:
        print("Nenhum arquivo PDF encontrado na pasta selecionada.")
    else:
        # Itera sobre os arquivos PDF
        for pdf_file in pdf_files:
            input_pdf_path = os.path.join(folder_selected, pdf_file)
            output_xlsx_path = os.path.join(folder_selected, os.path.splitext(pdf_file)[0] + ".xlsx")

            # Chamada da função para converter o PDF em XLSX
            convert_pdf_to_xlsx(input_pdf_path, output_xlsx_path)
else:
    print("Nenhuma pasta selecionada.")