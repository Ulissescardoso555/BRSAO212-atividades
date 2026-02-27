def calcular_gorjeta(valor_conta: float, porcentagem_gorjeta: float) -> float:
    # Calcula a gorjeta multiplicando o valor pela porcentagem dividida por 100
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return float(gorjeta)

# Testando a função
conta = 150.00
porcentagem = 10.0
resultado_gorjeta = calcular_gorjeta(conta, porcentagem)

print("--- Fechamento da Conta ---")
print(f"Valor do consumo: R$ {conta:.2f}")
print(f"Gorjeta sugerida ({porcentagem}%): R$ {resultado_gorjeta:.2f}")
print(f"Total a pagar: R$ {(conta + resultado_gorjeta):.2f}")