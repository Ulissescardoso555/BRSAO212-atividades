# 4- Verificador de Ano Bissexto
ano = int(input("Digite o ano para verificar se é bissexto: "))

# A condição verifica se (é divisível por 4 E não é divisível por 100) OU (é divisível por 400)
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"O ano {ano} É um ano bissexto.")
else:
    print(f"O ano {ano} NÃO é um ano bissexto.")