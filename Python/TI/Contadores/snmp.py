from pysnmp.hlapi import *

# Dados da impressora (IP, comunidade)
ip_address = '192.168.1.10'  # Substitua pelo IP da sua impressora
community = 'public'  # Substitua pela comunidade SNMP da sua impressora

# OIDs para obter informações (exemplos)
oids = [
    '1.3.6.1.2.1.1.5.0',  # sysName
    '1.3.6.1.2.1.1.1.0',  # sysDescr
]

# Função para enviar a requisição SNMP
def send_snmp_request(ip_address, community, oids):
  errorIndication, errorStatus, errorIndex, varBinds = next(
    getBulkCmd(SnmpEngine(),
               CommunityData(community),
               UdpTransportTarget((ip_address, 161)),
               ContextData(),
               0,
               10,  # Non-repeaters, max-repetitions
               * [ObjectType(ObjectIdentity(oid)) for oid in oids]
              )
  )

  # Verifica erros
  if errorIndication:
    print(f'Erro de indicação: {errorIndication}')
  elif errorStatus:
    print(f'Erro na resposta: {errorStatus}')
  else:
    # Imprime o valor do OID
    for varBind in varBinds:
      print(f'{varBind[0]} = {varBind[1]}')

# Executa a requisição
send_snmp_request(ip_address, community, oids)