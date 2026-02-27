import random
import string

print("--- Gerador de Senhas Seguras ---")
try:
    tamanho = int(input("Digite o tamanho desejado para a senha (ex: 12): "))
    
    if tamanho <= 0:
        print("Erro: O tamanho deve ser maior que zero.")
    else:
        # Junta todas as letras (maiúsculas e minúsculas), números e pontuações
        caracteres = string.ascii_letters + string.digits + string.punctuation
        
        # Sorteia aleatoriamente os caracteres e os junta em uma string
        senha = "".join(random.choice(caracteres) for i in range(tamanho))
        
        print(f"\nSua nova senha é: {senha}")

except ValueError:
    print("Erro: Por favor, digite um número inteiro válido.")