#Calculo do custo de envio com taxas variáveis

peso = float(input("Digite o peso da encomenda: "))
distancia = float(input("Digite a distância: "))

custo_base = (peso * 1.5) + (distancia * 0.25)
print(f"Custo base: {custo_base}")

if custo_base > 200:
    print(f"Preço da encomenda com desconto: {custo_base - (custo_base * 0.1)}")
elif custo_base >= 50 and custo_base <= 200:
    print(f"Preço da encomenda sem desconto: {custo_base}")
else:
    print(f"Custo de encomenda com taxa: {custo_base+(custo_base + 5)}")