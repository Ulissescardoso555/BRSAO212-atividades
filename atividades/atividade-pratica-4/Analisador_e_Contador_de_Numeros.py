pares = 0
impares = 0

print("--- Analisador de Números ---")
print("Digite os números inteiros que deseja analisar. Digite 'S' para encerrar.")

while True:
    entrada = input("Digite um número (ou 'S' para sair): ")
    
    if entrada.upper() == 'S':
        break
        
    try:
        numero = int(entrada)
        
        if numero % 2 == 0:
            print(f"O número {numero} é PAR.")
            pares += 1 # Atalho para pares = pares + 1
        else:
            print(f"O número {numero} é ÍMPAR.")
            impares += 1
            
    except ValueError:
        print("Erro: Por favor, digite um número inteiro válido.")

print("\n--- Resumo da Análise ---")
print(f"Total de números PARES digitados: {pares}")
print(f"Total de números ÍMPARES digitados: {impares}")
print(f"Total geral de números analisados: {pares + impares}")