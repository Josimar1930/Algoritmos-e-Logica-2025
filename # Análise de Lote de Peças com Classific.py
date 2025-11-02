# Análise de Lote de Peças com Classificação de Erros

numero_total_pecas = int(input("Digite o número total de peças do lote: "))
custo_fixo_inpecao = 150.00
custo_retrabalho = 25.00
erros_criticos = 0
erros_leves = 0
custo_variavel_rejeicao = 0.0

for i in range (1,numero_total_pecas +1):
    nivel_defeito_pecas = int(input(f"Qual o nível de Defeito da peça {i} (0 - 10): "))

    if nivel_defeito_pecas > 8:
        erros_criticos += 1
        custo_variavel_rejeicao += custo_retrabalho
    elif 3 <= nivel_defeito_pecas <= 8:
        erros_leves =+ 1
    else:
        print("Peça aprovada.") 

taxa_rejeicao = (erros_criticos / numero_total_pecas) * 100
custo_final_total = custo_fixo_inpecao + custo_variavel_rejeicao

if taxa_rejeicao > 10 and erros_leves > 5:
    print("LOTE REPROVADO! Alta taxa de defeito e muitos erros leves.")
elif erros_criticos > 2 or taxa_rejeicao > 20:
    print("LOTE CRÍTICO! Necessário reavaliação total.")
else:
    print("LOTE APROVADO! Custos sob controle.")
print(f"Taxa de rejeição : {taxa_rejeicao}")
print(f"Custo Final Total: {custo_final_total}")