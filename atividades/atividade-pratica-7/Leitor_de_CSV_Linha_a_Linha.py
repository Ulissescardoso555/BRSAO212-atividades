import csv

print("--- Visualizador de Arquivo CSV ---")
nome_arquivo = input("Digite o nome do arquivo CSV que deseja ler: ")

try:
    with open(nome_arquivo, mode='r', encoding='utf-8') as arquivo:
        leitor = csv.reader(arquivo)
        
        print("\n--- Conteúdo do Arquivo ---")
        for linha in leitor:
            # Junta os itens da lista em uma única string separada por " | "
            print(" | ".join(linha))
            
except FileNotFoundError:
    print(f"\nErro: O arquivo '{nome_arquivo}' não foi encontrado. Verifique o nome e tente novamente.")
except Exception as erro:
    print(f"\nFalha inesperada durante a leitura do arquivo: {erro}")