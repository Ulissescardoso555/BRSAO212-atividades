import json

print("--- Sistema de Configuração JSON ---")
nome_arquivo = "perfil_usuario.json"
dados_para_salvar = {
    "nome": "Lucas",
    "idade": 21,
    "cidade": "Manaus"
}

# PASSO 1: Escrever os dados no arquivo JSON
try:
    print("Salvando dados...")
    # ensure_ascii=False permite acentuação correta; indent=4 formata o texto para leitura humana
    with open(nome_arquivo, mode='w', encoding='utf-8') as arquivo:
        json.dump(dados_para_salvar, arquivo, ensure_ascii=False, indent=4)
    print("Dados salvos com sucesso!")
except Exception as erro:
    print(f"Falha ao salvar o arquivo JSON: {erro}")

# PASSO 2: Ler os dados do mesmo arquivo JSON
try:
    print("\nLendo dados do arquivo recém-criado...")
    with open(nome_arquivo, mode='r', encoding='utf-8') as arquivo:
        dados_lidos = json.load(arquivo)
        
    print("\n--- Dados Extraídos do JSON ---")
    print(f"Nome:   {dados_lidos['nome']}")
    print(f"Idade:  {dados_lidos['idade']}")
    print(f"Cidade: {dados_lidos['cidade']}")
    
except FileNotFoundError:
    print("\nErro: O arquivo JSON não foi encontrado para a leitura.")
except json.JSONDecodeError:
    print("\nErro: O arquivo encontrado não é um JSON válido e não pôde ser lido.")
except Exception as erro:
    print(f"\nFalha inesperada ao ler o arquivo JSON: {erro}")