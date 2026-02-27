print("--- Criação de Senha ---")
print("Regras: Mínimo de 8 caracteres e pelo menos 1 número.")

senha = input("Digite a sua nova senha: ")

# Verifica se tem 8 ou mais caracteres
tamanho_valido = len(senha) >= 8

# Verifica se existe pelo menos um caractere numérico na string
tem_numero = any(caractere.isdigit() for caractere in senha)

if tamanho_valido and tem_numero:
    print("Sucesso: A senha atende aos critérios de segurança!")
elif not tamanho_valido:
    print("Erro: A senha é muito curta. Precisa ter pelo menos 8 caracteres.")
elif not tem_numero:
    print("Erro: A senha deve conter pelo menos um número.")