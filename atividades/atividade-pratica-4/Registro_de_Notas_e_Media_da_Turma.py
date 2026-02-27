notas = [] # Cria uma lista vazia para armazenar as notas

print("--- Diário de Classe ---")
print("Digite as notas dos alunos. Digite 'S' para encerrar e calcular a média.")

while True:
    entrada = input("Digite a nota do aluno (ou 'S' para sair): ")
    
    if entrada.upper() == 'S':
        break
        
    try:
        nota = float(entrada)
        if 0 <= nota <= 10:
            notas.append(nota) # Adiciona a nota válida à lista
            print("Nota registrada!")
        else:
            print("Erro: A nota deve estar entre 0 e 10.")
    except ValueError:
        print("Erro: Por favor, digite um número válido.")

# Verifica se a lista não está vazia antes de calcular a média
if len(notas) > 0:
    media_turma = sum(notas) / len(notas)
    print("\n--- Resultado Final ---")
    print(f"Total de notas registradas: {len(notas)}")
    print(f"Média da turma: {media_turma:.2f}")
else:
    print("\nNenhuma nota foi registrada.")