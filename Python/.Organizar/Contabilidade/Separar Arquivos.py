import os
import shutil

def separate_xml_files(source_directory, destination_directory, files_per_folder):
    file_count = 0
    folder_count = 1
    folder_path = os.path.join(destination_directory, f'Folder_{folder_count}')
    os.makedirs(folder_path, exist_ok=True)

    for root, dirs, files in os.walk(source_directory):
        for file_name in files:
            if file_name.endswith('.xml'):
                source_file = os.path.join(root, file_name)
                destination_file = os.path.join(folder_path, file_name)
                shutil.move(source_file, destination_file)

                file_count += 1
                if file_count == files_per_folder:
                    folder_count += 1
                    folder_path = os.path.join(destination_directory, f'Folder_{folder_count}')
                    os.makedirs(folder_path, exist_ok=True)
                    file_count = 0

# Exemplo de uso
source_directory = 'X:\\Fiscal\\98 - Fiscal\\XML2'
destination_directory = 'X:\\Fiscal\\98 - Fiscal\\XML3'
files_per_folder = 100

separate_xml_files(source_directory, destination_directory, files_per_folder)