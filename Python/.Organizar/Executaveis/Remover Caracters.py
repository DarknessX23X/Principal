import re
import sys
import xml.etree.ElementTree as ET
#args = sys.argv


#if len(args) != 2:
  #  print("Por favor, forneça o caminho do arquivo como argumento.")
   # sys.exit(1)

# Acessa o valor do argumento "caminho"
#caminho = args[1]
caminho = "C:\\Users\\Tecnologia\\Desktop\\XML\\Invalido"

# Exibe o valor do argumento "caminho"
#print(f'O caminho do arquivo é: {caminho}')



def remover_caracteres_invalidos(caminho):   
    with open(caminho, 'r') as file:
        xml_content = file.read()   
        xml_content = re.sub(r'[^\x20-\x7e]', '', xml_content) 
        xml_content = re.sub(r'\r\n|\n', '', xml_content)   
        with open(caminho, 'w') as file:
            file.write(xml_content)
    
remover_caracteres_invalidos(caminho)

dados_xml = ET.parse(caminho)
root = dados_xml.getroot()
namespace = {"ns": "http://www.portalfiscal.inf.br/nfe"}
infNFe_Id = root.find('.//ns:infNFe',namespace).get('Id')
print(infNFe_Id)
