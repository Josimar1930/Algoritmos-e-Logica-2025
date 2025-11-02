# Análise de Produtividade e Bônus


numero_de_dias = int(input("Digite o número de dias da análise: "))

producao_total = 0
dias_acima_da_meta = 0

meta_diaria = 50

for dia in range(1, numero_de_dias + 1):
    producao_dia = int(input(f"Digite a produção do dia {dia}: "))
    producao_total += producao_dia

    if producao_dia >= meta_diaria:
        dias_acima_da_meta += 1

media_diaria = producao_total / numero_de_dias

if media_diaria > 60 and dias_acima_da_meta >= 4:
    print("BÔNUS MÁXIMO! (15% sobre a produção total).")
    bonus = producao_total * 0.15
elif media_diaria > 50 or dias_acima_da_meta >= 3:
    print("BÔNUS PARCIAL! (5% sobre a produção total).")
    bonus = producao_total * 0.05
else:
    print("Sem Bônus. Metas de produtividade não foram atingidas.")
    bonus = 0.0

print(f"Produção Total: {producao_total} unidades")
print(f"Média Diária de Produção: {media_diaria:.2f} unidades/dia")
print(f"Dias com meta atingida: {dias_acima_da_meta}")
print(f"Valor Final do Bônus: R$ {bonus:.2f}")
