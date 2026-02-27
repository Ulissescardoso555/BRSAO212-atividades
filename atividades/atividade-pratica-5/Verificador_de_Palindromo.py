def verificar_palindromo(texto):
    # Transforma em minúsculas para padronizar
    texto = texto.lower()
    
    # Cria uma nova string guardando apenas letras e números (ignorando espaços e pontuação)
    texto_limpo = ""
    for caractere in texto:
        if caractere.isalnum():
            texto_limpo += caractere
            
    # Compara o texto limpo com ele mesmo invertido
    if texto_limpo == texto_limpo[::-1]:
        return "Sim"
    else:
        return "Não"

# Testando a função
frase = input("Digite uma palavra ou frase para testar: ")
resultado = verificar_palindromo(frase)

print(f"É um palíndromo? {resultado}")