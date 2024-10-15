import subprocess
import tkinter as tk
from tkinter import ttk
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import Entry
from tkinter import PhotoImage
import winreg

def map_network_drive(drive_letter, network_path, username=None, password=None): 

  command = f"net use {drive_letter}: \\{network_path}"
  if username and password:
    command += f" /user:{username}  {password}"

  try:
    subprocess.run(command, shell=True, check=True)
    print(f"A pasta de rede '{network_path}' foi mapeada como '{drive_letter}:'.")
  except subprocess.CalledProcessError as e:
    print(f"Erro ao mapear a pasta de rede: {e}")

def map_network_drive_2(drive_letter, network_path): 

  command = f"net use {drive_letter}: \\{network_path}"
  try:
    subprocess.run(command, shell=True, check=True)
    print(f"A pasta de rede '{network_path}' foi mapeada como '{drive_letter}:'.")
  except subprocess.CalledProcessError as e:
    print(f"Erro ao mapear a pasta de rede: {e}")    

def remove_map_network_drive(drive_letter): 
  command = f"net use {drive_letter}: /delete /y"
  try:
    subprocess.run(command, shell=True, check=True)
    print(f"{drive_letter} Foi Removido '.")
  except subprocess.CalledProcessError as e:
    print(f"Erro ao remover a pasta de rede: {e}")

def verificar_mapeamento_letras(letras):
  mapeamento = {}
  chave = None
  for letra in letras:
    try:      
      chave = winreg.OpenKey(winreg.HKEY_CURRENT_USER,r"Network\\"f"{letra}", 0, winreg.KEY_READ)
      mapeamento[letra] = True
    except FileNotFoundError:
      mapeamento[letra] = False
    except Exception as e:
      print(f"Erro ao verificar o mapeamento da letra '{letra}': {e}")
      mapeamento[letra] = False
    finally:
      winreg.CloseKey(chave)

  return mapeamento





def get_domain():
    domain = subprocess.run(["powershell.exe", "(Get-CimInstance Win32_ComputerSystem).Domain"], stdout=subprocess.PIPE, text=True)
    domain = domain.stdout.strip()
    user_input = simpledialog.askstring("Usuario", "Digite o Usuario:")
    user_input = "kazzo1\\"+user_input
    pass_input = simpledialog.askstring("Senha", "Digite a Senha:")
    remove_map_network_drive('M')
    remove_map_network_drive('N')
    remove_map_network_drive('X')    
    map_network_drive('M', '\\192.168.0.53\\Aplicativos\\Strategies', username=user_input, password=pass_input)
    map_network_drive('N', '\\192.168.0.53\\Aplicativos\\Karamba\\Strategies', username=user_input, password=pass_input)
    map_network_drive('X', '\\192.168.0.53\\Arquivos', username=user_input, password=pass_input)
    letras = ['M', 'N', 'X']   
    resultado = verificar_mapeamento_letras(letras)    
    if all(valor for valor in resultado.values()):
     messagebox.showinfo("Sucesso","Mapeamento Executado Com Sucesso")

remove_map_network_drive('M')
remove_map_network_drive('N')
remove_map_network_drive('X')
domain = subprocess.run(["powershell.exe", "(Get-CimInstance Win32_ComputerSystem).Domain"], stdout=subprocess.PIPE, text=True)
domain = domain.stdout.strip()

if domain not in ("KAZZO1.sys", "Kazzo1.sys"):
    #print(domain)
    get_domain()
else:
    map_network_drive_2('M', '\\192.168.0.53\\Aplicativos\\Strategies')
    map_network_drive_2('N', '\\192.168.0.53\\Aplicativos\\Karamba\\Strategies')
    map_network_drive_2('X', '\\192.168.0.53\\Arquivos')
    letras = ['M', 'N', 'X']   
    resultado = verificar_mapeamento_letras(letras)
    #if all(valor for valor in resultado.values()):
    # messagebox.showinfo("Sucesso","Mapeamento Executado Com Sucesso")
    