from pyad import aduser,adcontainer

# Configurar as informações do servidor AD
ad_server = '192.168.0.53'
ad_username = 'administrador'
ad_password = 'Tec2024K@3,14colli'
ad_domain = 'kazzo1.sys'

# Conectar ao servidor AD
aduser.set_defaults(ldap_server=ad_server, username=ad_username, password=ad_password, ldap_domain=ad_domain)
#container = adcontainer.ADContainer.from_dn('OU=Usuarios,DC=kazzo1,DC=sys')