import re
import xml.etree.ElementTree as ET
from datetime import datetime
import os
from openpyxl import Workbook
import tkinter as tk
from tkinter import filedialog

def prompt_escolher_pasta():
    root = tk.Tk()
    root.withdraw()

    pasta = filedialog.askdirectory()
    return pasta

def list_xml_files(directory):
    xml_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.xml'):
                xml_files.append(os.path.join(root, file))        
    return xml_files

pasta = prompt_escolher_pasta()
xml_files=list_xml_files(pasta)

def extract_numbers(string):
    numbers = re.findall(r'\d+', string)
    return [int(num) for num in numbers]

def remover_caracteres_invalidos(arquivo_xml):   
    with open(arquivo_xml, 'r') as file:
        xml_content = file.read()   
        xml_content = re.sub(r'[^\x20-\x7e]', '', xml_content)    
        with open(arquivo_xml, 'w') as file:
            file.write(xml_content)
    #print("Caracteres inválidos removidos com sucesso!")

workbook = Workbook()
sheet = workbook.active

sheet["A1"] = "Data emissao"
sheet["B1"] = "NF"
sheet["C1"] = "CFOP"
sheet["D1"] = "Natureza Operação"
sheet["E1"] = "CNPJ Emitente"
sheet["F1"] = "Razão Emitente"
sheet["G1"] = "Valor Total"
sheet["H1"] = "Nome do Arquivo"
sheet["I1"] = "DANFE"

def write_xml_files_to_txt(xml_files, txt_file):
        x=2
        for xml_file in xml_files:  
        
            caminho_arquivo_xml = xml_file        
            print(caminho_arquivo_xml)
            
            #remover_caracteres_invalidos(caminho_arquivo_xml)

            def ler_xml(arquivo_xml):
        # Faz o parsing do arquivo XML
                tree = ET.parse(arquivo_xml)
                root = tree.getroot()

    # Extrai os dados do XML
                dados = {}
                for elemento in root.iter():
                    dados[elemento.tag] = elemento.text

                return dados



            dados_xml = ET.parse(caminho_arquivo_xml)
            root = dados_xml.getroot()
            namespace = {"ns": "http://www.portalfiscal.inf.br/nfe"}
      
            dhEmi_tag = root.find(".//ns:dhEmi", namespace)
            if dhEmi_tag is not None:
                dhEmi_valor = dhEmi_tag.text
                dhEmi_data = datetime.strptime(dhEmi_valor, "%Y-%m-%dT%H:%M:%S%z")
                dia = dhEmi_data.day
                mes = dhEmi_data.month
                ano = dhEmi_data.year                    
            else : 
                dia = "0"
                mes = "0"
                ano = "0" 

   
            #print("Valor da tag dhEmi:", str(dia) +'/'+str(mes) +'/'+str(ano))
            sheet["A" + str(x)] = str(dia) +'/'+str(mes) +'/'+str(ano)
            namespace = {"ns": "http://www.portalfiscal.inf.br/nfe"}
            NF_tag = root.find(".//ns:nNF", namespace)
            if NF_tag is not None:
                NF_valor = NF_tag.text
            else:
                NF_valor = "0"    

            sheet["B" + str(x)] = NF_valor
             #print("Valor da NF :", NF_valor)

            namespace = {"ns": "http://www.portalfiscal.inf.br/nfe"}
            CFOP_tag = root.find(".//ns:CFOP", namespace)
            if CFOP_tag is not None:
                CFOP_valor = CFOP_tag.text
            else:
                CFOP_valor = 0
            #print("Valor do CFOP :", NF_valor)
            sheet["C" + str(x)] = CFOP_valor
            namespace = {"ns": "http://www.portalfiscal.inf.br/nfe"}
            CNPJ_tag= root.find(".//ns:emit/ns:CNPJ", namespace)
            if CNPJ_tag is not None:
                CNPJ_Valor = CNPJ_tag.text
            else:
                CNPJ_Valor = 0
    
            sheet["E" + str(x)] = CNPJ_Valor
            namespace = {"ns": "http://www.portalfiscal.inf.br/nfe"}
            Natop_tag= root.find(".//ns:natOp", namespace)
            if Natop_tag is not None:
                Natop_Valor = Natop_tag.text
            else:
                Natop_Valor = 0   

            sheet["D" + str(x)] = Natop_Valor    

    #print("Valor do CNPJ :", CNPJ_valor)
    
            namespace = {"ns": "http://www.portalfiscal.inf.br/nfe"}
            xNome_tag = root.find(".//ns:emit/ns:xNome", namespace)
            if xNome_tag is not None:
                xNome_valor = xNome_tag.text
            else:
                xNome_valor=0

            sheet["F" + str(x)] = xNome_valor
        #print("Valor do xNome :", xNome_valor)

            namespace = {"ns": "http://www.portalfiscal.inf.br/nfe"}
            vNF_tag = root.find(".//ns:vNF", namespace)
            if vNF_tag is not None:
                vNF_valor = vNF_tag.text
            else:
                vNF_valor= 0
            sheet["G" + str(x)] = vNF_valor
            sheet["H" + str(x)] = os.path.basename(xml_file)
            chave_nfe = str(extract_numbers(os.path.basename(xml_file))).replace('[', '').replace(']', '')
            caminho_danfe = 'D:\\DANFE\\CONVERTIDO\\' + chave_nfe+'.pdf'
            sheet["I" + str(x)].hyperlink = caminho_danfe
            sheet["I" + str(x)].value = NF_valor
            
            #sheet["I" + str(x)].value = '@hiperlink("'+caminho_danfe+'";'+NF_valor+')'
            

            # str(extract_numbers(os.path.basename(xml_file))).replace('[', '').replace(']', '')
            
    #print("Valor do vPag :", vPag_valor)

    
            x=x+1

write_xml_files_to_txt(xml_files, 'D:\\XML\\KAZZO\\XML.txt')
pasta = prompt_escolher_pasta()
workbook.save(pasta +"\\XML.xlsx")