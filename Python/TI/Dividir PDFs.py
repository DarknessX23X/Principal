import pdfrw,os

def split_pdf(file_path):
    max_file_size = 8 * 1024 * 1024  # 9 MB em bytes
    file_counter = 1

    input_pdf = pdfrw.PdfReader(file_path)
    total_pages = len(input_pdf.pages)

    current_file_size = 0
    output_pdf = pdfrw.PdfWriter()

    for page_number, page in enumerate(input_pdf.pages):
        print(page_number)
        output_pdf.addpage(page)

        output_file_path = "E:\\PDF\\split_file_"+str(file_counter)+".pdf"
        output_pdf.write(output_file_path)

        current_file_size = os.path.getsize(output_file_path)

        if current_file_size >= max_file_size or page_number == total_pages - 1:
            file_counter += 1
            output_pdf = pdfrw.PdfWriter()

    return file_counter - 1

# Exemplo de uso
file_path = 'E:\\PDF\\06209148000893.pdf'
total_split_files = split_pdf(file_path)
print(f"Total de arquivos divididos: {total_split_files}")