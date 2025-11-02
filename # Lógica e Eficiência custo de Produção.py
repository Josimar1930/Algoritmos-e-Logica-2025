# Lógica e Eficiência custo de Produção

custo_fixo = 500.00
custo_materia_prima = float(input("Digite o custo da matéria-prima por item (R$): "))
custo_variavel_total = 0.0

for i in range(100):
    desperdicio = 0.05 * custo_materia_prima
    custo_variavel_total += custo_materia_prima + desperdicio

custo_total = custo_fixo + custo_variavel_total

if custo_total < 3000.00:
    margem = 0.35
elif custo_total >= 3000.00 and custo_total <= 5000.00:
    margem = 0.20
else:
    margem = 0.15

preco_minimo = (custo_total * (1 + margem)) / 100

print(f"Custo Total de Produção: R$ {custo_total:.2f}")
print(f"Margem de Lucro Aplicada: {margem * 100:.0f}%")
print(f"Preço Mínimo de Venda por Item: R$ {preco_minimo:.2f}")