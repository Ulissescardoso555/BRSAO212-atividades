import sys
import subprocess

# Tenta importar a biblioteca requests, se não conseguir, instala automaticamente
try:
    import requests
except ModuleNotFoundError:
    print("Opa! A biblioteca 'requests' não foi encontrada.")
    print("Iniciando a instalação automática, por favor aguarde...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
    print("Instalação concluída com sucesso!\n")
    import requests 

def buscar_usuario_ficticio():
    """
    Faz a requisição para a API Random User Generator.
    Retorna um dicionário com os dados extraídos ou None em caso de falha.
    """
    url = "https://randomuser.me/api/"

    try:
        resposta = requests.get(url, timeout=5)
        resposta.raise_for_status() 
        
        dados = resposta.json()
        
        # VERIFICAÇÃO DE SEGURANÇA ADICIONADA AQUI:
        # Confirma se a chave 'results' existe no JSON e se a lista não está vazia
        if 'results' in dados and len(dados['results']) > 0:
            usuario = dados['results'][0]
            
            perfil = {
                "nome": f"{usuario['name']['first']} {usuario['name']['last']}",
                "email": usuario['email'],
                "pais": usuario['location']['country']
            }
            
            return perfil
        else:
            print("Erro: A API respondeu, mas não enviou nenhum dado de usuário.")
            return None

    except requests.exceptions.Timeout:
        print("Erro: A conexão demorou muito para responder (Timeout).")
        return None
    except requests.exceptions.ConnectionError:
        print("Erro: Falha na conexão. Verifique sua rede.")
        return None
    except requests.exceptions.RequestException as erro:
        print(f"Erro inesperado na requisição: {erro}")
        return None

if __name__ == "__main__":
    print("--- Gerador de Usuário Fictício ---")
    print("Conectando à API...\n")
    
    usuario_encontrado = buscar_usuario_ficticio()
    
    if usuario_encontrado:
        print("[Perfil Encontrado]")
        print(f"Nome: {usuario_encontrado['nome']}")
        print(f"E-mail: {usuario_encontrado['email']}")
        print(f"País: {usuario_encontrado['pais']}")
    else:
        print("\nOperação finalizada sem sucesso.")