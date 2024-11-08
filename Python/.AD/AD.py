import subprocess

# Variáveis
displayName = "João Silva"
usuario = "jsilva"
senha = "Senha123!"
servidor = "192.168.0.53"
matricula = '123456'
nome, sobrenome = displayName.split(" ")

# Comando do PowerShell para criar o usuário
comando_criacao = f"""
New-ADUser -Server {servidor} -Name '{displayName}' -SamAccountName '{usuario}' -UserPrincipalName '{usuario}@KAZZO1.sys' -AccountPassword (ConvertTo-SecureString -AsPlainText '{senha}' -Force) -Enabled $true
"""

# Comando do PowerShell para adicionar atributos
comando_adiciona_atributos = f"""
Set-ADUser -Server {servidor} -Identity '{usuario}' -EmployeeID '{matricula}' -GivenName '{nome}' -Surname '{sobrenome}' -DisplayName '{displayName}' -L 'Local' -Company 'Empresa' -Department 'Departamento' -email '{usuario}@KAZZO1.sys' -OfficePhone '1234567890' 
"""

# Execute o comando de criação do usuário
processo_criacao = subprocess.Popen(["powershell", "-Command", comando_criacao], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
saida_criacao, erro_criacao = processo_criacao.communicate()

# Verifique se o comando de criação foi executado com sucesso
if processo_criacao.returncode == 0:
    print("Usuário criado com sucesso:", displayName)

    # Execute o comando para adicionar atributos
    processo_atributos = subprocess.Popen(["powershell", "-Command", comando_adiciona_atributos], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    saida_atributos, erro_atributos = processo_atributos.communicate()

    # Verifique se o comando de adição de atributos foi executado com sucesso
    if processo_atributos.returncode == 0:
        print("Atributos adicionados com sucesso.")
    else:
        print("Erro ao adicionar atributos:")
        print(erro_atributos.strip())
else:
    print("Erro ao criar o usuário:")
    print(erro_criacao.strip())