#Classificadir de lucro de vendas

preco_custo = float(input("Digite o preço de compra do produto: "))
preco_venda = float(input("Digite o preço de venda do produto: "))

lucro = preco_venda - preco_custo

margem = (lucro/preco_custo) * 100

if margem > 30:
    print("Margem exelente")
elif margem > 10 and margem < 30:
    print("Margem satisfatória")
else:
    print("Margem baixa: Avaliar preço de venda.")