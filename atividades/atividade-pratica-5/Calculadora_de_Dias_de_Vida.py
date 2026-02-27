# 4- Calculadora de Dias de Vida
from datetime import datetime

print("--- Descubra Quantos Dias Você Já Viveu ---")
data_nascimento_str = input("Digite sua data de nascimento (DD/MM/AAAA): ")

try:
    # Converte a string (texto) digitada pelo usuário para um formato de Data real
    # O "%d/%m/%Y" ensina ao Python qual é o dia, mês e ano no texto digitado
    data_nascimento = datetime.strptime(data_nascimento_str, "%d/%m/%Y").date()
    
    # Pega a data exata de hoje através do sistema
    hoje = datetime.now().date()
    
    # Validação para não permitir datas no futuro
    if data_nascimento > hoje:
        print("Erro: A data de nascimento não pode estar no futuro!")
    else:
        # Quando subtraímos duas datas, o Python gera um objeto que contém os dias
        diferenca = hoje - data_nascimento
        dias_vividos = diferenca.days
        
        print("\n--- Resultado ---")
        print(f"Hoje é dia: {hoje.strftime('%d/%m/%Y')}")
        print(f"Você já viveu exatamente {dias_vividos} dias na Terra!")

except ValueError:
    print("Erro: Formato de data inválido. Por favor, certifique-se de usar DD/MM/AAAA.")