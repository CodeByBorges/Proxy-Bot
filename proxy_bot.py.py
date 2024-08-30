import winreg
import time

def disable_proxy():
    try:
        # Abrindo a chave do registro para configurações de proxy
        registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Internet Settings', 0, winreg.KEY_WRITE)

        # Configurando o valor do proxy para 0 (desativado)
        winreg.SetValueEx(registry_key, 'ProxyEnable', 0, winreg.REG_DWORD, 0)

        # Fechando a chave do registro
        winreg.CloseKey(registry_key)
        print("Proxy desativado com sucesso.")
    except Exception as e:
        print(f"Erro ao desativar o proxy: {e}")

def check_and_disable_proxy():
    try:
        # Abrindo a chave do registro para leitura das configurações de proxy
        registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Internet Settings', 0, winreg.KEY_READ)

        # Obtendo o valor do proxy
        proxy_enable, _ = winreg.QueryValueEx(registry_key, 'ProxyEnable')

        # Fechando a chave do registro
        winreg.CloseKey(registry_key)

        # Verificando se o proxy está ativado
        if proxy_enable == 1:
            print("Proxy ativado. Desativando...")
            disable_proxy()
    except Exception as e:
        print(f"Erro ao verificar o proxy: {e}")

if __name__ == "__main__":
    while True:
        check_and_disable_proxy()
        # Intervalo de verificação de 60 segundos
        time.sleep(20)
