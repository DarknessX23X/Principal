import requests
import json

def consultar_api(url, headers=None):
    response = requests.post(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

def envia_pessoa(url, data,token):
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


# Exemplo de uso
url = "https://www30.bhan.com.br:9443/api/v1/autorizacao/token"
headers  = {
    "Content-Type": "application/json",
    "usuario": "kazzoconfeccoesws",
    "senha": "147258"
}

data={    
    "cdModPac": 2001,
    "cdOrigem": "29846739000109",
    "cdDestino": "29846739000109",
    "dtMovimento": "12/02/2024",
    "dsPacote": "Bling 1.0 - PACOTE IMPORTADO POR : GIOVANE DE CARVALHO FERREIRA - 620638",
    "nrPrioridade": 9999,
    "inConteudoBase64": 9,
    "dsConteudo": "<dados><pessoa><nrCPFCNPJ>32193437831</nrCPFCNPJ><dsNome>ROSALINA MAXIMO DA CRUZ</dsNome><nrCNPJEmp>09041289000161</nrCNPJEmp><nrDiasBaseVencto>0</nrDiasBaseVencto><nrDiasCarencia>0</nrDiasCarencia><tpPessoa>F</tpPessoa><pessoaFisica><dtNascimento>06/02/1984</dtNascimento><tpSexo>F</tpSexo><tpEstadoCivil>1</tpEstadoCivil><tpTermoLGPD>0</tpTermoLGPD></pessoaFisica><inCliente>1</inCliente><inFornecedor>0</inFornecedor><inFuncionario>0</inFuncionario><inCNSRFinal>1</inCNSRFinal><inTransportadora>0</inTransportadora><inAutorizacaoXmlNFe>0</inAutorizacaoXmlNFe><inClienteBloqueado>0</inClienteBloqueado><inSocio>0</inSocio><inReceberEmail>0</inReceberEmail><inReceberSms>0</inReceberSms><endereco><tpEndereco>2</tpEndereco><dsSiglaLograd>RUA</dsSiglaLograd><dsLogradouro>RAFAEL LOPES</dsLogradouro><nrLogradouro>170</nrLogradouro><dsComplemento>- DE 82/83 AO FIM</dsComplemento><dsBairro>JARDIM PEABIRU</dsBairro><cdMunicipio>3507506</cdMunicipio><dsMunicipio>BOTUCATU</dsMunicipio><cdUF>SP</cdUF><cdCEP>18604690</cdCEP><cdPais>1058</cdPais><dsPais>BRASIL</dsPais></endereco><telefone><dsTelefone>991049649</dsTelefone><inFonePadrao>1</inFonePadrao><cdTipoFonePessoa>1</cdTipoFonePessoa><nrRamalFone>0</nrRamalFone></telefone></pessoa></dados>"
}



resultado = consultar_api(url, headers=headers )
if resultado:
    print(resultado["cdToken"])
    token = resultado["cdToken"]
else:
    print("Falha na consulta da API")

url = "https://www30.bhan.com.br:9443/api/v1/pacote/inclusao"



resultado = envia_pessoa(url, data, token)
if resultado:
    print(resultado["nrPacote"])
else:
    print("Falha na consulta da API")