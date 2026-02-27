import requests

print("--- Consulta de Endereço via CEP ---")
cep = input("Digite o CEP (apenas números, sem traço): ")

# Validação básica para garantir que o usuário digitou 8 números
if len(cep) != 8 or not cep.isdigit():
    print("Erro: O CEP deve conter exatamente 8 números.")
else:
    url = f"https://viacep.com.br/ws/{cep}/json/"
    
    try:
        resposta = requests.get(url, timeout=5)
        resposta.raise_for_status()
        dados = resposta.json()
        
        # Verifica se a API retornou a flag de erro (CEP inexistente)
        if "erro" in dados:
            print("\nErro: O CEP digitado não existe na base de dados.")
        else:
            print("\n[Endereço Encontrado]")
            print(f"Logradouro: {dados.get('logradouro')}")
            print(f"Bairro: {dados.get('bairro')}")
            print(f"Cidade: {dados.get('localidade')}")
            print(f"Estado: {dados.get('uf')}")
            
    except requests.exceptions.RequestException:
        print("Erro: Falha na requisição. Verifique sua conexão com a internet.")