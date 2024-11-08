from pyad import *

# Configurações do AD
ldap_server = '192.168.0.53'
domain = 'kazzo1.sys'
username = 'administrador@kazzo1.sys'
password = 'Tec2024K@3,14colli'

# Conecta ao AD
pyad.set_defaults(ldap_server=ldap_server, domain=domain, username=username, password=password)

# Cria um objeto ADContainer para a unidade organizacional "Usuarios"
container = pyad.adcontainer.ADContainer.from_dn('ou=Admin,dc=kazzo1,dc=sys')

# Lista os usuários do AD
usuarios = container.get_children()

# Imprime a lista de usuários
for user in usuarios:
    print(user.get_attribute('sAMAccountName'))