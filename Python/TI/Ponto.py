# Nome do arquivo original e do novo arquivo
input_file = 'X:\\ti\\teste.txt'
output_file = 'X:\\ti\\novo_arquivo.txt'

def remover_segundos(hora):
    if hora.endswith(':00'):
        nova_hora = hora[:-3]  # Remove os dois últimos caracteres
        return nova_hora
    return hora

def formatar_dados(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
    with open(output_file, 'w') as new_file:
        for line in lines:
            if 'Entrada - Cartão' in line:
                status = "011" 
            else:
                status = "011"

            if "Cartão:" in line:                
                codigo = line[-7:].strip()
            else:
                data_hora, _, _ = line.strip().split('|')
                dia, mes, ano_hora = data_hora.split()[0].split('/')
                ano = ano_hora.split()[0][-2:]
                if len(data_hora.split()) > 1:
                    hora = data_hora.split()[1]
                    hora = remover_segundos(hora)  # Remove os segundos se presentes
                else:
                    hora = "00:00"
                new_line = f"{status} {dia}/{mes}/{ano} {hora} {codigo} 15 1\n"
                new_file.write(new_line)

# Abre o arquivo para leitura
with open(input_file, 'r') as file:
    lines = file.readlines()

# Remove o trecho 'Relatório de marcações'
new_lines = [line for line in lines if 'Relatório de marcações' not in line 
                                        and 'Período:' not in line 
                                        and not line.startswith('Usuário:') 
                                        and 'Data/Hora|Inner|Tipo' not in line 
                                        and line.strip() != '' 
                                        and len(line) >= 5]

# Abre o arquivo para escrita e salva as novas linhas
with open(input_file, 'w') as file:
    file.writelines(new_lines)

formatar_dados(input_file)
