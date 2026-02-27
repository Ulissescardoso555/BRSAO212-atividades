# 3- Calculadora de Preço Final com Desconto

print("--- Sistema de Caixa: Aplicar Desconto ---")

try:
    preco_original = float(input("Digite o preço do produto (ex: 120.50): "))
    porcentagem_desconto = float(input("Digite a porcentagem de desconto (ex: 15): "))
    
    # Cálculo do desconto
    valor_desconto = preco_original * (porcentagem_desconto / 100)
    
    # Preço final
    preco_final = preco_original - valor_desconto
    
    # Formatação e exibição
    print("\n--- Resumo da Operação ---")
    print(f"Preço original: R$ {preco_original:.2f}")
    print(f"Valor do desconto: R$ {valor_desconto:.2f}")
    print(f"Preço final com {porcentagem_desconto}% OFF: R$ {preco_final:.2f}")

except ValueError:
    print("Erro: Por favor, insira apenas números válidos e use o ponto para casas decimais.")