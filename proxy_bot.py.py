import subprocess

# Lista de softwares a serem instalados
softwares = [
    "Microsoft Office 2010",
    "Driver Booster",
    "UltraVNC",
    "WinRAR",
    "Revo Uninstaller",
    "Google Chrome"
]

# Comandos de instalação específicos para cada software (exemplo para Windows usando arquivos executáveis)
install_commands = {
    "Microsoft Office 2010": ["D:\Aplicativos\Microsoft Office 2010 - ST (Grupo JLJ)\setup.exe", "/quiet", "/norestart"],
    "Driver Booster": ["path_to_installer.exe", "/S"],
    "UltraVNC": ["path_to_installer.exe", "/silent"],
    "WinRAR": ["path_to_installer.exe", "/S"],
    "Revo Uninstaller": ["path_to_installer.exe", "/VERYSILENT", "/NORESTART"],
    "Google Chrome": ["path_to_installer.exe", "/silent", "/install"]
}

# Loop para instalar cada software
for software in softwares:
    print(f"Instalando {software}...")
    
    # Verifica se há um comando de instalação definido para o software
    if software in install_commands:
        install_command = install_commands[software]
        
        try:
            subprocess.check_call(install_command)
            print(f"{software} instalado com sucesso.")
        except subprocess.CalledProcessError as e:
            print(f"Erro ao instalar {software}: {e}")
    else:
        print(f"Comando de instalação não especificado para {software}. Pule este software.")

print("Instalação em massa concluída.")
