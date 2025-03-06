import os
import xml.etree.ElementTree as ET
from datetime import datetime
import shutil

def list_xml_files(directory):
    xml_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.xml'):
                xml_files.append(os.path.join(root, file))      
                print(os.path.join(root, file))  
    return xml_files

def split_path(file_path):
    file_name = os.path.basename(file_path)
    directory = os.path.dirname(file_path)
    return file_name, directory

def write_xml_files_to_txt(xml_files, txt_file):
    
        for xml_file in xml_files:            
           caminho_arquivo_xml = xml_file
           dados_xml = ET.parse(caminho_arquivo_xml)
           root = dados_xml.getroot()
           namespace = {"ns": "http://www.portalfiscal.inf.br/nfe"}
           CNPJ_tag = root.find(".//ns:emit/ns:CNPJ", namespace)
           dhEmi_tag = root.find(".//ns:dhEmi", namespace)

           

           if CNPJ_tag is not None:
            CNPJ_valor = CNPJ_tag.text
           else:
            CNPJ_valor = "0"

           
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

           file_name, directory = split_path(caminho_arquivo_xml)      
           #print(directory)
          
           '''
           if CNPJ_valor =="06209148000117" and ano ==2019 and mes==1:
            shutil.copy(caminho_arquivo_xml, "D:\\XML\\KAZZO\\2019\\01")         
            print(str(mes) + "-" + CNPJ_valor)

           if CNPJ_valor ==" 06209148000893" and ano ==2019 and mes==1:
            shutil.copy(caminho_arquivo_xml, "D:\\XML\\KAZZO 33\\2019\\01")         
            print(str(mes) + "-" + CNPJ_valor)

           if CNPJ_valor =="06209148000117" and ano ==2019 and mes==2:
            shutil.copy(caminho_arquivo_xml, "D:\\XML\\KAZZO\\2019\\02")         
            print(str(mes) + "-" + CNPJ_valor)

           if CNPJ_valor ==" 06209148000893" and ano ==2019 and mes==2:
            shutil.copy(caminho_arquivo_xml, "D:\\XML\\KAZZO 33\\2019\\02")         
            print(str(mes) + "-" + CNPJ_valor)  

           if CNPJ_valor =="06209148000117" and ano ==2019 and mes==3:
            shutil.copy(caminho_arquivo_xml, "D:\\XML\\KAZZO\\2019\\03")         
            print(str(mes) + "-" + CNPJ_valor)

            if CNPJ_valor ==" 06209148000893" and ano ==2019 and mes==3:
             shutil.copy(caminho_arquivo_xml, "D:\\XML\\KAZZO 33\\2019\\03")         
             print(str(mes) + "-" + CNPJ_valor)

           if CNPJ_valor =="06209148000117" and ano ==2019 and mes==4:
            shutil.copy(caminho_arquivo_xml, "D:\\XML\\KAZZO\\2019\\04")         
            print(str(mes) + "-" + CNPJ_valor)

           if CNPJ_valor ==" 06209148000893" and ano ==2019 and mes==4:
            shutil.copy(caminho_arquivo_xml, "D:\\XML\\KAZZO 33\\2019\\04")         
            print(str(mes) + "-" + CNPJ_valor)

           if CNPJ_valor =="06209148000117" and ano ==2019 and mes==5:
            shutil.copy(caminho_arquivo_xml, "D:\\XML\\KAZZO\\2019\\05")         
            print(str(mes) + "-" + CNPJ_valor)

           if CNPJ_valor ==" 06209148000893" and ano ==2019 and mes==5:
            shutil.copy(caminho_arquivo_xml, "D:\\XML\\KAZZO 33\\2019\\05")         
            print(str(mes) + "-" + CNPJ_valor)

           if CNPJ_valor =="06209148000117" and ano ==2019 and mes==6:
            shutil.copy(caminho_arquivo_xml, "D:\\XML\\KAZZO\\2019\\06")         
            print(str(mes) + "-" + CNPJ_valor)      
           
           if CNPJ_valor ==" 06209148000893" and ano ==2019 and mes==6:
            shutil.copy(caminho_arquivo_xml, "D:\\XML\\KAZZO 33\\2019\\06")         
            print(str(mes) + "-" + CNPJ_valor)

           if CNPJ_valor =="06209148000117" and ano ==2019 and mes==7:
            shutil.copy(caminho_arquivo_xml, "D:\\XML\\KAZZO\\2019\\07")         
            print(str(mes) + "-" + CNPJ_valor)

           if CNPJ_valor ==" 06209148000893" and ano ==2019 and mes==7:
            shutil.copy(caminho_arquivo_xml, "D:\\XML\\KAZZO 33\\2019\\07")         
            print(str(mes) + "-" + CNPJ_valor) 
            
           if CNPJ_valor =="06209148000117" and ano ==2019 and mes==8:
            shutil.copy(caminho_arquivo_xml, "D:\\XML\\KAZZO\\2019\\08")         
            print(str(mes) + "-" + CNPJ_valor)  

            if CNPJ_valor ==" 06209148000893" and ano ==2019 and mes==8:
             shutil.copy(caminho_arquivo_xml, "D:\\XML\\KAZZO 33\\2019\\08")         
             print(str(mes) + "-" + CNPJ_valor)

           if CNPJ_valor =="06209148000117" and ano ==2019 and mes==9:
            shutil.copy(caminho_arquivo_xml, "D:\\XML\\KAZZO\\2019\\09")         
            print(str(mes) + "-" + CNPJ_valor)

            if CNPJ_valor ==" 06209148000893" and ano ==2019 and mes==9:
             shutil.copy(caminho_arquivo_xml, "D:\\XML\\KAZZO 33\\2019\\09")         
             print(str(mes) + "-" + CNPJ_valor)
 

           if CNPJ_valor =="06209148000117" and ano ==2019 and mes==10:
            shutil.copy(caminho_arquivo_xml, "D:\\XML\\KAZZO\\2019\\10")         
            print(str(mes) + "-" + CNPJ_valor)

           if CNPJ_valor ==" 06209148000893" and ano ==2019 and mes==10:
            shutil.copy(caminho_arquivo_xml, "D:\\XML\\KAZZO 33\\2019\\10")         
            print(str(mes) + "-" + CNPJ_valor) 


           if CNPJ_valor =="06209148000117" and ano ==2019 and mes==11:
            shutil.copy(caminho_arquivo_xml, "D:\\XML\\KAZZO\\2019\\11")         
            print(str(mes) + "-" + CNPJ_valor) 

           if CNPJ_valor =="06209148000117" and ano ==2019 and mes==12:
            shutil.copy(caminho_arquivo_xml, "D:\\XML\\KAZZO\\2019\\12")         
            print(str(mes) + "-" + CNPJ_valor) 

           if CNPJ_valor ==" 06209148000893" and ano ==2019 and mes==11:
            shutil.copy(caminho_arquivo_xml, "D:\\XML\\KAZZO 33\\2019\\11")         
            print(str(mes) + "-" + CNPJ_valor)   

            if CNPJ_valor ==" 06209148000893" and ano ==2019 and mes==12:
             shutil.copy(caminho_arquivo_xml, "D:\\XML\\KAZZO 33\\2019\\12")         
             print(str(mes) + "-" + CNPJ_valor)  
 

           if CNPJ_valor =="06209148000117" and ano ==2020 and mes==1:
            shutil.copy(caminho_arquivo_xml, "D:\\XML\\KAZZO\\2020\\01")         
            print(str(mes) + "-" + CNPJ_valor)

           if CNPJ_valor =="06209148000117" and ano ==2020 and mes==2:
            shutil.copy(caminho_arquivo_xml, "D:\\XML\\KAZZO\\2020\\02")         
            print(str(mes) + "-" + CNPJ_valor)  

           if CNPJ_valor =="06209148000117" and ano ==2020 and mes==3:
            shutil.copy(caminho_arquivo_xml, "D:\\XML\\KAZZO\\2020\\03")         
            print(str(mes) + "-" + CNPJ_valor)

           if CNPJ_valor =="06209148000117" and ano ==2020 and mes==4:
            shutil.copy(caminho_arquivo_xml, "D:\\XML\\KAZZO\\2020\\04")         
            print(str(mes) + "-" + CNPJ_valor)

           if CNPJ_valor =="06209148000117" and ano ==2020 and mes==5:
            shutil.copy(caminho_arquivo_xml, "D:\\XML\\KAZZO\\2020\\05")         
            print(str(mes) + "-" + CNPJ_valor)

           if CNPJ_valor =="06209148000117" and ano ==2020 and mes==6:
            shutil.copy(caminho_arquivo_xml, "D:\\XML\\KAZZO\\2020\\06")         
            print(str(mes) + "-" + CNPJ_valor)      

           if CNPJ_valor =="06209148000117" and ano ==2020 and mes==7:
            shutil.copy(caminho_arquivo_xml, "D:\\XML\\KAZZO\\2020\\07")         
            print(str(mes) + "-" + CNPJ_valor)

           if CNPJ_valor =="06209148000117" and ano ==2020 and mes==8:
            shutil.copy(caminho_arquivo_xml, "D:\\XML\\KAZZO\\2020\\08")         
            print(str(mes) + "-" + CNPJ_valor)

           if CNPJ_valor =="06209148000117" and ano ==2020 and mes==9:
            shutil.copy(caminho_arquivo_xml, "D:\\XML\\KAZZO\\2020\\09")         
            print(str(mes) + "-" + CNPJ_valor)

           if CNPJ_valor =="06209148000117" and ano ==2020 and mes==10:
            shutil.copy(caminho_arquivo_xml, "D:\\XML\\KAZZO\\2020\\10")         
            print(str(mes) + "-" + CNPJ_valor)

           if CNPJ_valor =="06209148000117" and ano ==2020 and mes==11:
            shutil.copy(caminho_arquivo_xml, "D:\\XML\\KAZZO\\2020\\11")         
            print(str(mes) + "-" + CNPJ_valor)  

           if CNPJ_valor =="06209148000117" and ano ==2020 and mes==12:
            shutil.copy(caminho_arquivo_xml, "D:\\XML\\KAZZO\\2020\\12")         
            print(str(mes) + "-" + CNPJ_valor)   

           if CNPJ_valor =="06209148000893" and ano ==2020 and mes==1:
            shutil.copy(caminho_arquivo_xml, "D:\\XML\\KAZZO 33\\2020\\01")         
            print(str(mes) + "-" + CNPJ_valor)

           if CNPJ_valor =="06209148000893" and ano ==2020 and mes==2:
            shutil.copy(caminho_arquivo_xml, "D:\\XML\\KAZZO 33\\2020\\02")         
            print(str(mes) + "-" + CNPJ_valor)  

           if CNPJ_valor =="06209148000893" and ano ==2020 and mes==3:
            shutil.copy(caminho_arquivo_xml, "D:\\XML\\KAZZO 33\\2020\\03")         
            print(str(mes) + "-" + CNPJ_valor)

           if CNPJ_valor =="06209148000893" and ano ==2020 and mes==4:
            shutil.copy(caminho_arquivo_xml, "D:\\XML\\KAZZO 33\\2020\\04")         
            print(str(mes) + "-" + CNPJ_valor)

           if CNPJ_valor =="06209148000893" and ano ==2020 and mes==5:
            shutil.copy(caminho_arquivo_xml, "D:\\XML\\KAZZO 33\\2020\\05")         
            print(str(mes) + "-" + CNPJ_valor)

           if CNPJ_valor =="06209148000893" and ano ==2020 and mes==6:
            shutil.copy(caminho_arquivo_xml, "D:\\XML\\KAZZO 33\\2020\\06")         
            print(str(mes) + "-" + CNPJ_valor)      

           if CNPJ_valor =="06209148000893" and ano ==2020 and mes==7:
            shutil.copy(caminho_arquivo_xml, "D:\\XML\\KAZZO 33\\2020\\07")         
            print(str(mes) + "-" + CNPJ_valor)

           if CNPJ_valor =="06209148000893" and ano ==2020 and mes==8:
            shutil.copy(caminho_arquivo_xml, "D:\\XML\\KAZZO 33\\2020\\08")         
            print(str(mes) + "-" + CNPJ_valor)

           if CNPJ_valor =="06209148000893" and ano ==2020 and mes==9:
            shutil.copy(caminho_arquivo_xml, "D:\\XML\\KAZZO 33\\2020\\09")         
            print(str(mes) + "-" + CNPJ_valor)

           if CNPJ_valor =="06209148000893" and ano ==2020 and mes==10:
            shutil.copy(caminho_arquivo_xml, "D:\\XML\\KAZZO 33\\2020\\10")         
            print(str(mes) + "-" + CNPJ_valor)

           if CNPJ_valor =="06209148000893" and ano ==2020 and mes==11:
            shutil.copy(caminho_arquivo_xml, "D:\\XML\\KAZZO 33\\2020\\11")         
            print(str(mes) + "-" + CNPJ_valor)  

           if CNPJ_valor =="06209148000893" and ano ==2020 and mes==12:
            shutil.copy(caminho_arquivo_xml, "D:\\XML\\KAZZO 33\\2020\\12")         
            print(str(mes) + "-" + CNPJ_valor)     
          '''

           
            
           
# Exemplo de uso
xml_files = list_xml_files('X:\\Contabilidade')

#xml_files = list_xml_files('X:\\Fiscal\\Obrigações Kazzo Matriz\\Obrigações Kazzo\\XML SAIDA KAZZO\\07-2019\\Kazzo Matriz')
write_xml_files_to_txt(xml_files, 'D:\\XML\\KAZZO\\XML.txt')


