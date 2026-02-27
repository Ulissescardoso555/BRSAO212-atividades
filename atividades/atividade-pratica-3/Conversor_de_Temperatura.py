# Conversor de Temperatura com Laço de Repetição e Tratamento de Erros

print("Bem-vindo ao Conversor de Temperatura!")
print("Dica: Digite 'S' na temperatura a qualquer momento para sair.")

while True:
    print("\n" + "-"*30)
    entrada = input("Digite a temperatura (ou 'S' para sair): ")

    # Verifica se o usuário quer encerrar o programa
    if entrada.upper() == 'S':
        print("Encerrando o conversor. Até mais!")
        break # O 'break' interrompe o laço while

    # Tenta converter a entrada para número decimal (float)
    try:
        temp = float(entrada)
    except ValueError:
        print("Erro: Por favor, digite um número válido para a temperatura.")
        continue # O 'continue' pula para o início do laço while

    origem = input("Unidade de origem (C, F ou K): ").upper()
    destino = input("Unidade de destino (C, F ou K): ").upper()

    # Validação rápida das unidades
    if origem not in ['C', 'F', 'K'] or destino not in ['C', 'F', 'K']:
        print("Erro: Unidade inválida! Use apenas C, F ou K.")
        continue

    resultado = None

    # Lógica de conversão
    if origem == destino:
        resultado = temp # Se as unidades forem iguais, não há o que converter
    elif origem == 'C' and destino == 'F':
        resultado = temp * 9/5 + 32
    elif origem == 'C' and destino == 'K':
        resultado = temp + 273.15
    elif origem == 'F' and destino == 'C':
        resultado = (temp - 32) * 5/9
    elif origem == 'F' and destino == 'K':
        resultado = (temp - 32) * 5/9 + 273.15
    elif origem == 'K' and destino == 'C':
        resultado = temp - 273.15
    elif origem == 'K' and destino == 'F':
        resultado = (temp - 273.15) * 9/5 + 32

    # Exibe o resultado final
    print(f"\n=> Resultado: {temp}°{origem} equivale a {resultado:.2f}°{destino}")