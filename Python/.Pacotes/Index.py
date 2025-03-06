from flask import Flask, render_template, request
from xml.dom import minidom
import os
import requests
import json
from datetime import date
from dateutil import parser

app = Flask(__name__)
app.logger.disabled = False

urlpct = "https://www30.bhan.com.br:9443/api/v1/pacote/inclusao"

def consultar_api(url, headers=None):
    response = requests.post(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None
    
def envia_pacote(url, data,token):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None


    
urltk = "https://www30.bhan.com.br:9443/api/v1/autorizacao/token"
headers  = {
    "Content-Type": "application/json",
    "usuario": "kazzoconfeccoesws",
    "senha": "147258"
}


@app.route("/")
def index():
    return render_template("index.html")

@app.route('/cancelar')
def cancelar():
    return render_template('cancelar.html')

@app.route('/cancelar_notas', methods=["POST"])
def cancelar_notas():

    resultado = consultar_api(urltk, headers=headers )
    if resultado:
        token = resultado["cdToken"]
        print(token)
        
    else:
        print("Falha na consulta da API")    

    xml_files = request.files.getlist("xml_file")  
    for xml_file in xml_files:
        xml_doc = minidom.parse(xml_file)
        nNF_tags = xml_doc.getElementsByTagName('nNF')
        data_tags = xml_doc.getElementsByTagName('dhEmi')
        cnpj_tags = xml_doc.getElementsByTagName('emit')[0].getElementsByTagName('CNPJ')
        cliente_tags = xml_doc.getElementsByTagName('dest')[0].getElementsByTagName('xNome')
        cpf_tags = xml_doc.getElementsByTagName('dest')[0].getElementsByTagName('CPF')     
        logradouro_tags = xml_doc.getElementsByTagName('dest')[0].getElementsByTagName('xLgr')     
        numero_tags = xml_doc.getElementsByTagName('dest')[0].getElementsByTagName('nro')
        bairro_tags = xml_doc.getElementsByTagName('dest')[0].getElementsByTagName('xBairro')   
        cmunicipio_tags = xml_doc.getElementsByTagName('dest')[0].getElementsByTagName('cMun')      
        municipio_tags = xml_doc.getElementsByTagName('dest')[0].getElementsByTagName('xMun')  
        UF_tags = xml_doc.getElementsByTagName('dest')[0].getElementsByTagName('UF') 
        CEP_tags = xml_doc.getElementsByTagName('dest')[0].getElementsByTagName('CEP')
        cPais_tags = xml_doc.getElementsByTagName('dest')[0].getElementsByTagName('cPais')
        xPais_tags = xml_doc.getElementsByTagName('dest')[0].getElementsByTagName('xPais')        
        infNFe_tag = xml_doc.getElementsByTagName('infNFe')[0]
        id_attr = infNFe_tag.getAttribute('Id')    
        try:
            vencimento_tags = xml_doc.getElementsByTagName('dup')[0].getElementsByTagName('dVenc')
            fone_tags = xml_doc.getElementsByTagName('dest')[0].getElementsByTagName('fone')
        except:
            fone_tags='14329898'
            vencimento = date.today()
            vencimento = vencimento.strftime("%d/%m/%Y")  

        total_tags = xml_doc.getElementsByTagName('total')[0].getElementsByTagName('vNF')
        nNF = nNF_tags[0].firstChild.nodeValue
        dhEmi = data_tags[0].firstChild.nodeValue
        cnpj = cnpj_tags[0].firstChild.nodeValue
        cliente = cliente_tags[0].firstChild.nodeValue 
        cpf = cpf_tags[0].firstChild.nodeValue
        logadouro = logradouro_tags[0].firstChild.nodeValue
        numero = numero_tags[0].firstChild.nodeValue
        bairro = bairro_tags[0].firstChild.nodeValue
        cmunicipio = cmunicipio_tags[0].firstChild.nodeValue
        municipio = municipio_tags[0].firstChild.nodeValue
        CEP = CEP_tags[0].firstChild.nodeValue
        UF = UF_tags[0].firstChild.nodeValue
        cPais = cPais_tags[0].firstChild.nodeValue
        xPais = xPais_tags[0].firstChild.nodeValue
        try:
         fone = fone_tags[0].firstChild.nodeValue
        except:
         fone = '1432989898'   
        numeros = id_attr.split("NFe")[1]  

        

        try:
            vencimento =  vencimento_tags[0].firstChild.nodeValue
            documento ="01" 
        except:
            vencimento = date.today()
            vencimento = vencimento.strftime("%d/%m/%Y") 
            documento ="20" 
        

        total = total_tags[0].firstChild.nodeValue    
        data_formatada = parser.parse(dhEmi)
        data_formatada_str = data_formatada.strftime("%d/%m/%Y")  
        venc_formatada = parser.parse(vencimento)
        venc_formatada_str = venc_formatada.strftime("%d/%m/%Y")  
        data_hora_atual = date.today()
        data_hora_formatada = data_hora_atual.strftime('%d/%m/%Y %H:%M:%S')

       
        data ={
        "cdModPac": 4003,
        "cdOrigem": cnpj,
        "cdDestino": cnpj,
        "dtMovimento": data_formatada_str,
        "dsPacote": "Bling 1.0",
        "nrPrioridade": 9999,
        "inConteudoBase64": 9,
        "dsConteudo": "<dados><documentoFiscal>"
        "<tpModDctoFiscal>35</tpModDctoFiscal>"
        "<dsChaveAcesso>"f"{numeros}</dsChaveAcesso>"
        "<nrCupomFiscal>1</nrCupomFiscal>"
        "<nrNF>"f"{nNF}</nrNF><cdSerieNF>0</cdSerieNF>"
        "<dtCancelamento>"f"{data_formatada}</dtCancelamento>"
        "<nProt>1</nProt>"
        "<dsChaveAcessoCanc>"f"{numeros}</dsChaveAcessoCanc>"
        "<dsMotivoCanc>CANCELADO PELO CLIENTE</dsMotivoCanc><cdUsuarioGeracaoPacote>0</cdUsuarioGeracaoPacote>"
        "<cdUsuario>003</cdUsuario>"
        "<tpProcessamento>N</tpProcessamento></documentoFiscal></dados>"
        }

       
        resultado = envia_pacote(urlpct, data, token)
       
        if resultado:
            print(resultado["nrPacote"])
        else:
            print("Falha na consulta da API")

    return render_template('cancelar.html')



@app.route("/import_xml", methods=["POST"])
def import_xml():  
    opcoes = request.form.get('opcoes')  # Obter a opção selecionada do formulário    
    parte_texto = opcoes.split('-')[0].strip()
    #print(parte_texto)

    resultado = consultar_api(urltk, headers=headers )
    if resultado:
        token = resultado["cdToken"]
    else:
        print("Falha na consulta da API")


    xml_files = request.files.getlist("xml_file")     
    for xml_file in xml_files:
        xml_doc = minidom.parse(xml_file)
        nNF_tags = xml_doc.getElementsByTagName('nNF')
        data_tags = xml_doc.getElementsByTagName('dhEmi')
        try:
            cnpj_tags = xml_doc.getElementsByTagName('emit')[0].getElementsByTagName('CNPJ')
    # Resto do código que depende de cnpj_tags
        except IndexError:
            cnpj_tags = '00000000000000'
        cliente_tags = xml_doc.getElementsByTagName('dest')[0].getElementsByTagName('xNome')
        cpf_tags = xml_doc.getElementsByTagName('dest')[0].getElementsByTagName('CPF')     
        logradouro_tags = xml_doc.getElementsByTagName('dest')[0].getElementsByTagName('xLgr')     
        numero_tags = xml_doc.getElementsByTagName('dest')[0].getElementsByTagName('nro')
        bairro_tags = xml_doc.getElementsByTagName('dest')[0].getElementsByTagName('xBairro')   
        cmunicipio_tags = xml_doc.getElementsByTagName('dest')[0].getElementsByTagName('cMun')      
        municipio_tags = xml_doc.getElementsByTagName('dest')[0].getElementsByTagName('xMun')  
        UF_tags = xml_doc.getElementsByTagName('dest')[0].getElementsByTagName('UF') 
        CEP_tags = xml_doc.getElementsByTagName('dest')[0].getElementsByTagName('CEP')
        cPais_tags = xml_doc.getElementsByTagName('dest')[0].getElementsByTagName('cPais')
        xPais_tags = xml_doc.getElementsByTagName('dest')[0].getElementsByTagName('xPais')
        try:
         fone_tags = xml_doc.getElementsByTagName('dest')[0].getElementsByTagName('fone')
        except:
            fone_tags='1432989898'
        try:
            vencimento_tags = xml_doc.getElementsByTagName('dup')[0].getElementsByTagName('dVenc')
        except:
            vencimento = date.today()
            vencimento = vencimento.strftime("%d/%m/%Y")  

        total_tags = xml_doc.getElementsByTagName('total')[0].getElementsByTagName('vNF')
        nNF = nNF_tags[0].firstChild.nodeValue
        dhEmi = data_tags[0].firstChild.nodeValue
        cnpj = cnpj_tags[0].firstChild.nodeValue
        cliente = cliente_tags[0].firstChild.nodeValue 
        try:
            cpf = cpf_tags[0].firstChild.nodeValue
        except:
            cpf ="00000000000"

        logadouro = logradouro_tags[0].firstChild.nodeValue
        numero = numero_tags[0].firstChild.nodeValue
        bairro = bairro_tags[0].firstChild.nodeValue
        cmunicipio = cmunicipio_tags[0].firstChild.nodeValue
        municipio = municipio_tags[0].firstChild.nodeValue
        CEP = CEP_tags[0].firstChild.nodeValue
        UF = UF_tags[0].firstChild.nodeValue
        cPais = cPais_tags[0].firstChild.nodeValue
        xPais = xPais_tags[0].firstChild.nodeValue
        try:
            fone = fone_tags[0].firstChild.nodeValue  
        except:
            fone ="1432989898"

        try:
            vencimento =  vencimento_tags[0].firstChild.nodeValue
            if parte_texto == "523" or parte_texto == "3208" :
                documento ="20" 
            else:
                documento ="01"
        except:
            vencimento = date.today()
            vencimento = vencimento.strftime("%d/%m/%Y") 
            if parte_texto == "523" or parte_texto == "3208" :
                documento ="20" 
            else:
                documento ="01" 
        

        total = total_tags[0].firstChild.nodeValue    
        data_formatada = parser.parse(dhEmi)
        data_formatada_str = data_formatada.strftime("%d/%m/%Y")  
        venc_formatada = parser.parse(vencimento)
        venc_formatada_str = venc_formatada.strftime("%d/%m/%Y")  
        data={    
        "cdModPac": 2001,
        "cdOrigem": cnpj,
        "cdDestino": cnpj,
        "dtMovimento": data_formatada_str,
        "dsPacote": "Bling 1.0",
        "nrPrioridade": 9999,
        "inConteudoBase64": 9,
        "dsConteudo":"<dados><pessoa><nrCPFCNPJ>"f"{cpf}</nrCPFCNPJ>"
        "<dsNome>"f"{cliente}</dsNome><nrCNPJEmp>"f"{cnpj}</nrCNPJEmp>"
        "<nrDiasBaseVencto>0</nrDiasBaseVencto><nrDiasCarencia>0</nrDiasCarencia>"
        "<tpPessoa>F</tpPessoa><pessoaFisica><dtNascimento>06/02/1984</dtNascimento>"
        "<tpSexo>F</tpSexo><tpEstadoCivil>1</tpEstadoCivil>"
        "<tpTermoLGPD>0</tpTermoLGPD></pessoaFisica><inCliente>1</inCliente>"
        "<inFornecedor>0</inFornecedor><inFuncionario>0</inFuncionario>"
        "<inCNSRFinal>1</inCNSRFinal><inTransportadora>0</inTransportadora>"
        "<inAutorizacaoXmlNFe>0</inAutorizacaoXmlNFe><inClienteBloqueado>0</inClienteBloqueado>"
        "<inSocio>0</inSocio><inReceberEmail>0</inReceberEmail><inReceberSms>0</inReceberSms>"
        "<endereco><tpEndereco>2</tpEndereco><dsSiglaLograd>RUA</dsSiglaLograd>"
        "<dsLogradouro>"f"{logadouro}</dsLogradouro><nrLogradouro>"f"{numero}</nrLogradouro>"
        "<dsComplemento></dsComplemento><dsBairro>"f"{bairro}</dsBairro><cdMunicipio>"f"{cmunicipio}</cdMunicipio>"
        "<dsMunicipio>"f"{municipio}</dsMunicipio><cdUF>"f"{UF}</cdUF><cdCEP>"f"{CEP}</cdCEP><cdPais>"f"{cPais}</cdPais><dsPais>"f"{xPais}</dsPais>"
        "</endereco><telefone><dsTelefone>"f"{fone}</dsTelefone><inFonePadrao>1</inFonePadrao><cdTipoFonePessoa>1</cdTipoFonePessoa>"
        "<nrRamalFone>0</nrRamalFone></telefone></pessoa></dados>"
        }

        if cpf == "00000000000" :
           print('1')
        else: 
            resultado = envia_pacote(urlpct, data, token)
        if resultado:
            print(resultado)
            #print(resultado["nrPacote"])
        else:
            print("Falha na consulta da API")

        xml=xml_doc.toxml().replace('<?xml version="1.0" ?>', '')


        pagamento=""
        cprod_tags = xml_doc.getElementsByTagName('cProd')  
        qcom_tags = xml_doc.getElementsByTagName('qCom')         
        quantidade_cprod = len(cprod_tags)

        for i in range(quantidade_cprod):
            cprod = cprod_tags[i].firstChild.nodeValue 
            qcom = qcom_tags[i].firstChild.nodeValue 
            pagamento = pagamento + ("<itemAdicionalNF><nrItem>"f"{i+1}"
                                     "</nrItem><cdProduto>" + str(cprod) + 
                                     "</cdProduto><cdVendedor>1</cdVendedor>"
                                     "<qtItem>"f"{qcom}</qtItem></itemAdicionalNF>")   
        
        
        data={    
        "cdModPac": 4001,
        "cdOrigem": cnpj,
        "cdDestino": cnpj,
        "dtMovimento": data_formatada_str,
        "dsPacote": "Bling 1.0",
        "nrPrioridade": 9999,
        "inConteudoBase64": 9,
        "dsConteudo":"<dados><NFe>"f"{xml}</NFe><financeiroNF><dtMovimento>"f"{data_formatada_str}</dtMovimento>" 
        "<nrDocumento>"f"{nNF}</nrDocumento><nrParcela>1</nrParcela>"
        "<tpDocumento>"f"{documento}</tpDocumento>"
		"<vlDocumento>"f"{total}</vlDocumento>"
		"<dtVencimento>"+ 
        str(data_formatada_str) + "</dtVencimento>"
	    "</financeiroNF>"
        "<adicionalNF><dtMovimento>" + 
        str(data_formatada_str) + 
        "</dtMovimento><nrCPFCNPJCliente>" + str(cpf) + 
        "</nrCPFCNPJCliente><cdOperacao>" + str(parte_texto) + 
        "</cdOperacao><cdVendedor>1</cdVendedor>" f"{pagamento}</adicionalNF>"  
       "</dados>"
        }
    
        resultado = envia_pacote(urlpct, data, token)
        if resultado:
            print(resultado["nrPacote"])
        else:
            print("Falha na consulta da API")
        
        #print(data)


    return render_template("index.html")

@app.route("/operacoes.txt")
def opcoes():
    caminho_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_arquivo_opcoes = os.path.join(caminho_atual, "operacoes.txt")
    with open(caminho_arquivo_opcoes, "r") as arquivo:
          return arquivo.read()



if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080')