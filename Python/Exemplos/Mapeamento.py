import subprocess

def map_network_drive(drive_letter, network_path):
    command = f"net use {drive_letter} {network_path}"
    subprocess.run(command, shell=True)

# Exemplo de uso
drive_letter = "Z:"
network_path = r"\\192.168.0.53\\Arquivos"

map_network_drive(drive_letter, network_path)