import wmi

# Conectar ao computador local
c = wmi.WMI()

# Verificar se o dispositivo ROOT\JUNGO\0000 está instalado
device = c.Win32_PnPEntity(DeviceID='ROOT\\JUNGO\\0000')
if device:
    print("O dispositivo ROOT\\JUNGO\\0000 foi encontrado.")
else:
    print("O dispositivo ROOT\\JUNGO\\0000 não foi encontrado.")