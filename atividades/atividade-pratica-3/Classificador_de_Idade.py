idade_texto = input("Digite a sua idade: ")
idade = int(idade_texto)

print("--- Resultado da Classificação ---")
if 0 <= idade <= 12:
    print("Classificação: Criança")
elif 13 <= idade <= 17:
    print("Classificação: Adolescente")
elif 18 <= idade <= 59:
    print("Classificação: Adulto")
elif idade >= 60:
    print("Classificação: Idoso")
else:
    print("Idade inválida.")