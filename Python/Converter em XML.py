import csv
import os

def csv_to_xml(input_csv, output_folder):
    with open(input_csv, 'r') as file:
        reader = csv.DictReader(file, delimiter=';')
        for idx, row in enumerate(reader):
            xml_content = ""
            for key, value in row.items():
                xml_content += f"<{key}>{value}</{key}>\n"

            xml_filename = os.path.join(output_folder, f"output_{idx}.xml")
            with open(xml_filename, 'w') as xml_file:
                xml_file.write(xml_content)

if __name__ == "__main__":
    input_csv = "C:\\CONFIG\\CTE.CSV"
    output_folder = "C:\\CONFIG\\XML"
    os.makedirs(output_folder, exist_ok=True)
    csv_to_xml(input_csv, output_folder)