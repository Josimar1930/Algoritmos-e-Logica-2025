# Classificador de Lote Químico e Preço Variável
pureza = float(input("Digite a pureza do lote (%):  "))
massa_total = float(input("Digite a massa total (em Kg): "))
taxa_contaminacao = float(input("Digite a taxa de cotaminação (%): "))

FD = (pureza * 100) - (taxa_contaminacao * 50)

if massa_total > 10:
    P_base = 10
else:
    P_base = 12,50

if FD > 90 and pureza > 0.98:
    print( "Classificação: PREMIUM (Venda Imediata)")
elif FD >= 70 and FD <= 90 and taxa_contaminacao < 0.05:
    print("Classificação: Padrão (Venda normal)")
    P_final_kg = P_base * 1.10
elif FD < 70 or pureza < 0.90:
    print("Classificação: Reprovado (Descarte ou Re-processamento)")
    P_final_kg = P_base * 0.25
else:
    print("Classificação: ACEITÁVEL (Margem Mínima)")
    P_final_kg = P_base * 0.90

preco_total_final = P_final_kg * massa_total
print(f"Preço final: {P_final_kg}Kg")
print(f"Preço total por lote: {preco_total_final}")