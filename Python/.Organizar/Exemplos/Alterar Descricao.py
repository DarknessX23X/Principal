from ldap3 import Server, Connection, MODIFY_REPLACE, MODIFY_ADD

# Configurar as credenciais de acesso
username = "administrador@kazzo1.sys"
password = "Tec2024K@3,14colli"
server_address = "192.168.0.53"
base_dn = "dc=kazzo1,dc=sys"

# Conectar ao servidor AD
server = Server(server_address)
conn = Connection(server, user=username, password=password)
conn.bind()

# Verificar se a conexão foi bem-sucedida
if conn.bind():
    print("Conexão ao Active Directory bem-sucedida")
else:
    print("Erro ao conectar ao Active Directory:", conn.result)

# Obter o computador pelo nome
computer_name = "DESK230"
search_filter = f'(cn={computer_name})'
attributes = ['description']
conn.search(base_dn, search_filter, attributes=attributes)
entry = conn.entries[0]

# Atualizar a descrição do computador
new_description = "Genildo - Manutenção"

if 'description' in entry:
    changes = { 'description': [(MODIFY_REPLACE, [new_description])] }
else:
    changes = { 'description': [(MODIFY_ADD, [new_description])] }
    
conn.modify(entry.entry_dn, changes)

# Confirmar que a descrição foi atualizada
conn.search(base_dn, search_filter, attributes=['description'])
updated_entry = conn.entries[0]

print("Descrição atualizada do computador:", updated_entry['description'])

# Fechar a conexão com o servidor AD
conn.unbind()