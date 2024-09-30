import os
import xml.etree.ElementTree as ET
from datetime import datetime
import shutil
from lxml import etree
import re

def extrair_numeros(string):
    numeros = re.findall(r'\d+', string)
    numeros_int = [int(numero) for numero in numeros]
    numeros_str = ', '.join(map(str, numeros_int))
    return numeros_str

def list_xml_files(directory):
    xml_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.xml'):
                xml_files.append(os.path.join(root, file))      
                #print(os.path.join(root, file))  
    return xml_files

def split_path(file_path):
    file_name = os.path.basename(file_path)
    directory = os.path.dirname(file_path)
    return file_name, directory

def remover_caracteres_invalidos(caminho):   
    with open(caminho, 'r') as file:
        xml_content = file.read()   
        xml_content = re.sub(r'[^\x20-\x7e]', '', xml_content) 
        xml_content = re.sub(r'\r\n|\n', '', xml_content)   
        with open(caminho, 'w') as file:
            file.write(xml_content)
    



caminhoinput = input("Informe o caminho do arquivo: ")
xml_files = list_xml_files(caminhoinput)


for xml_file in xml_files :
    try:
        caminho_arquivo_xml = xml_file
        #remover_caracteres_invalidos(caminho_arquivo_xml)
        parser = etree.XMLParser(recover=True)        
        tree = etree.parse(caminho_arquivo_xml, parser)
        root = tree.getroot()
     
            
        
        namespace = {"ns": "http://www.portalfiscal.inf.br/nfe"}
        try:
            CNPJ_tag = root.find(".//ns:emit/ns:CNPJ", namespace)        
            NfeId = root.find('.//ns:infNFe',namespace)
        
        except ET.ParseError:
                print("Erro ao ler o arquivo XML.")
        except AttributeError:
                print("Erro ao encontrar o elemento no XML.")    

        if NfeId is not None:
             try:
                NfeId = extrair_numeros(root.find('.//ns:infNFe',namespace).get('Id'))
             except ET.ParseError:
                print("Erro ao ler o arquivo XML.")
             except AttributeError:
                print("Erro ao encontrar o elemento no XML.")    
        else:
            NfeId = "0"

        if CNPJ_tag is not None:
            CNPJ_valor = CNPJ_tag.text
            #diretorio = os.path.dirname(caminhoinput)
            diretoriofinal = os.path.join(caminhoinput,CNPJ_valor)
            #print(diretoriofinal)
            if not os.path.exists(diretoriofinal):
                os.makedirs(diretoriofinal)
              
                #shutil.move(directory +"\\"+ NfeId +".xml", "E:\\ARQ2\\"+CNPJ_valor)
                
        else:            
            if not os.path.exists(diretorio+"Invalido"):
                print(caminho_arquivo_xml)
                #os.makedirs(diretorio+"Invalido")
                #shutil.move(caminho_arquivo_xml, "E:\\ARQ2\\Invalido")


    except ET.ParseError as e:
    # Imprima a mensagem de erro
     print(f"Erro ao analisar o XML: {str(e)}")            
    
    if CNPJ_tag is not None:
        CNPJ_valor = CNPJ_tag.text
        directory = os.path.dirname(caminho_arquivo_xml)
        file_name = os.path.basename(caminho_arquivo_xml)   
        caminho = caminho_arquivo_xml
        novo_nome = NfeId+".xml"
        diretorio = os.path.dirname(caminho)
        novo_caminho = os.path.join(diretorio, novo_nome)
        if os.path.exists(novo_caminho):
            print(novo_nome)
        else:
            os.rename(caminho, novo_caminho)
            #print(novo_nome)
           
        diretorio = os.path.dirname(diretorio)
        novo_caminho_d = os.path.join(diretorio, CNPJ_valor,novo_nome)    
        #print(NfeId)
        shutil.move(novo_caminho, novo_caminho_d) 
      
    else:
        diretorioinv =os.path.dirname(caminho)
        diretorioinvf = os.path.join(diretorioinv, "Invalido") 
        #shutil.move(caminho_arquivo_xml, diretorioinvf)
        #print(caminho_arquivo_xml)
   
    
