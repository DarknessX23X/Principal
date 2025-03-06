import subprocess

def executar_comando_remoto(computador_alvo, comando):
    """Executa um comando remotamente usando psexec.

    Args:
        computador_alvo: O nome ou endereço IP do computador alvo.
        comando: O comando a ser executado remotamente.
    """
    try:
        # Comando psexec com o comando a ser executado
        comando_psexec = ["psexec", "\\\\" + computador_alvo, comando]
        print(comando_psexec)
        
        # Executa o comando e captura a saída
        resultado = subprocess.run(comando_psexec, capture_output=True, text=True, check=True)
        print(f"Saída do comando em {computador_alvo}:\n{resultado.stdout}")

    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar o comando em {computador_alvo}: {e}")
    except FileNotFoundError:
        print("O psexec não foi encontrado. Certifique-se de que ele esteja no PATH.")


# Exemplo de uso:
computador_alvo = "192.168.0.10" # Substitua pelo IP ou nome do computador
comando_remoto = "cmd" # Substitua pelo comando desejado

executar_comando_remoto(computador_alvo, comando_remoto)