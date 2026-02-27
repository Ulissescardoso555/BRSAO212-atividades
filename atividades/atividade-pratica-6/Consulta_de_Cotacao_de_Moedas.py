import requests

print("--- Consulta de Cotação de Moedas ---")
moeda = input("Digite a sigla da moeda que deseja consultar (ex: USD, EUR, BTC): ").upper()

url = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"

try:
    resposta = requests.get(url, timeout=5)
    
    # A AwesomeAPI retorna o código 404 quando a moeda não existe
    if resposta.status_code == 404:
        print(f"\nErro: A moeda '{moeda}' não existe ou não é suportada pela API.")
    else:
        resposta.raise_for_status()
        dados = resposta.json()
        
        # A chave no JSON retornado tem o formato "USDBRL", "EURBRL", etc.
        chave_moeda = f"{moeda}BRL"
        info = dados[chave_moeda]
        
        print(f"\n[Cotação Atual: {moeda} para BRL]")
        print(f"Valor Atual: R$ {float(info['bid']):.4f}")
        print(f"Máxima: R$ {float(info['high']):.4f}")
        print(f"Mínima: R$ {float(info['low']):.4f}")
        print(f"Data/Hora: {info['create_date']}")

except requests.exceptions.RequestException:
    print("\nErro: Falha na conexão com a API de cotações.")
except KeyError:
    print("\nErro: Falha ao ler os dados da moeda informada.")