nome_produto = "Cadeira Infantil"
preco_unitario = 12.40
quantidade = 3

preco_total = preco_unitario * quantidade

print("--- Detalhes da Compra ---")
print(f"Produto: {nome_produto}")
# O :.2f formata o número para ter exatamente 2 casas decimais
print(f"Preço Unitário: R$ {preco_unitario:.2f}") 
print(f"Quantidade: {quantidade}")
print(f"Preço Total: R$ {preco_total:.2f}")