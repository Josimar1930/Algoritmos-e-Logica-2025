# Calculadora de total de compras

qtdade_produtos = int(input("Informe a quantidade de produtos comprados: "))

acumuladora = 0.0

for n in range (qtdade_produtos):
    preco = float(input(f"Informe o preço do produto {n + 1}: "))
    acumuladora += preco
print(f"O total a pagar e: R${acumuladora:.2f}")