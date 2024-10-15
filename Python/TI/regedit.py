import winreg

def verificar_chave_registro(chave_registro):
  """Verifica se uma chave de registro existe.

  Args:
      chave_registro (str): O caminho completo da chave de registro a ser verificada.

  Returns:
      bool: True se a chave de registro existe, False caso contrário.
  """

  try:
    winreg.OpenKey(winreg.HKEY_CURRENT_USER, chave_registro, 0, winreg.KEY_READ)
    return True
  except FileNotFoundError:
    return False
  except Exception as e:
    print(f"Erro ao verificar a chave de registro: {e}")
    return False

# Exemplo de uso:
chave = r"Network\M"
existe = verificar_chave_registro(chave)
print(f"A chave '{chave}' existe: {existe}")