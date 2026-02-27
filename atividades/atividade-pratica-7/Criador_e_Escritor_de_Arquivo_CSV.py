import csv

print("--- Criador de Tabela de Usuários ---")
nome_arquivo = input("Digite o nome do arquivo que deseja salvar (ex: usuarios.csv): ")

# Matriz com os cabeçalhos e as linhas de dados
dados = [
    ["Nome", "Idade", "Cidade"],
    ["Ana Silva", 28, "São Paulo"],
    ["Carlos Moura", 35, "Rio de Janeiro"],
    ["Beatriz Costa", 22, "Curitiba"]
]

try:
    # Abre o arquivo no modo 'w' (write/escrever)
    with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerows(dados) # Escreve todas as linhas de uma vez
        
    print(f"\nSucesso! Os dados foram salvos no formato tabular no arquivo '{nome_arquivo}'.")

except Exception as erro:
    print(f"\nFalha crítica ao tentar salvar o arquivo: {erro}")