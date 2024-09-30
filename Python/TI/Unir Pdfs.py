from PyPDF2 import PdfMerger,PdfReader, PdfWriter
import os
from tkinter import Tk
from tkinter.filedialog import askdirectory


# Abre uma janela de diálogo para selecionar a pasta de destino
Tk().withdraw()
pdf_folder_path = askdirectory(title='Selecione a pasta dos pdfs')

Tk().withdraw()
folder_path = askdirectory(title='Selecione a pasta de destino')

# Pasta onde estão os arquivos PDF


# Define o tamanho máximo do arquivo em bytes (9 MB)
max_file_size = 9 * 1024 * 1024

# Cria uma instância do objeto PdfFileMerger
merger = PdfMerger()

# Variável para controlar o número do arquivo
file_number = 1

# Loop para percorrer os arquivos na pasta
for filename in os.listdir(pdf_folder_path):
    if filename.endswith('.pdf'):
        # Caminho completo do arquivo PDF
        pdf_file = os.path.join(pdf_folder_path, filename)

        # Adiciona o arquivo PDF à instância do objeto PdfFileMerger
        merger.append(pdf_file)

        # Verifica o tamanho do arquivo resultante
        file_size = os.path.getsize(pdf_file)

        print(pdf_file)

        # Verifica se o tamanho do arquivo excede o tamanho máximo
        if file_size > max_file_size:
            # Define o nome do arquivo de saída
            output_file = os.path.join(folder_path, f'arquivo_unido_{file_number}.pdf')

            # Salva o arquivo atual e cria um novo arquivo
            merger.write(output_file)
            merger.close()

            # Cria uma nova instância do objeto PdfFileMerger
            merger = PdfMerger()

            # Incrementa o número do arquivo
            file_number += 1

# Define o nome do arquivo de saída final
output_file = os.path.join(folder_path, f'arquivo_unido_{file_number}.pdf')

# Salva o arquivo final
merger.write(output_file)

# Fecha a instância do objeto PdfFileMerger
merger.close()

print(f'A união dos arquivos PDF foi concluída. Foram criados {file_number} arquivos.')

