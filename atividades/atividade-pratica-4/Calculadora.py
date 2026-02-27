def calcular(num1, num2, operacao):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
    elif operacao == '*':
        return num1 * num2
    elif operacao == '/':
        if num2 == 0:
            return "Erro: Não é possível dividir por zero."
        return num1 / num2
    else:
        return "Operação inválida."

print("--- Calculadora ---")
n1 = float(input("Digite o primeiro número: "))
op = input("Digite a operação (+, -, *, /): ")
n2 = float(input("Digite o segundo número: "))

resultado = calcular(n1, n2, op)
print(f"Resultado: {resultado}")