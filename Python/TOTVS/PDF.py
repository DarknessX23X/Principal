import pdfplumber
import pyocr
import pyocr.builders
from PIL import Image
from openpyxl import Workbook

# Definir o caminho do arquivo PDF
pdf_path = "C:\\config\\DESK065.pdf"

# Definir o caminho do arquivo Excel
excel_path = "C:\\config\\arquivo.xlsx"

# Inicializar um objeto Workbook
workbook = Workbook()
sheet = workbook.active

# Inicializar o OCR com a engine desejada (neste exemplo, usaremos o Tesseract)
ocr_tool = pyocr.get_available_tools()[0]
ocr_lang = ocr_tool.get_available_languages()[0]

# Abrir o arquivo PDF
with pdfplumber.open(pdf_path) as pdf:
    # Percorrer todas as páginas do PDF
    for page in pdf.pages:
        # Extrair as imagens da página
        images = page.images
        
        # Percorrer todas as imagens e realizar o OCR
        for i, img in enumerate(images):
            # Extrair a imagem como arquivo temporário
            img_path = f"temp_image_{i}.png"
            img_obj = page.to_image(resolution=150)
            img_obj.save(img_path, format="PNG")
            
            # Carregar a imagem e realizar o OCR
            img = Image.open(img_path)
            text = ocr_tool.image_to_string(img, lang=ocr_lang, builder=pyocr.builders.TextBuilder())
            
           
            
            # Adicionar o texto extraído ao arquivo Excel
            sheet.append([text])
            
# Salvar o arquivo Excel
workbook.save(excel_path)

# Fechar o arquivo Excel
workbook.close()