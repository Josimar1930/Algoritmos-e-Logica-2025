# Cálculo de Imposto e Taxas sobre Vendas

dias_analisados = int(input("Digite a quantidade de dias que serão analisados: "))
vendas_totais = 0.0


for dia in range(dias_analisados):
    venda_diaria = float(input(f"Digite o valor das vendas do dia {dia + 1}: R$ "))
    vendas_totais += venda_diaria  
    dias_analisados > 0
    media_diaria = vendas_totais / dias_analisados 
if media_diaria > 1500:
    imposto_fixo = 200.0
else:
    imposto_fixo = 50.0
if vendas_totais > 10000:
    taxa_servico_percentual = 0.08
else:
    taxa_servico_percentual = 0.05
valor_taxa_servico = vendas_totais * taxa_servico_percentual
valor_liquido_final = vendas_totais - valor_taxa_servico - imposto_fixo
print(f"\nValor Total das Vendas: R$ {vendas_totais:.2f}")
print(f"Imposto Fixo Aplicado: R$ {imposto_fixo:.2f}")
print(f"Percentual da Taxa de Serviço: {taxa_servico_percentual * 100:.0f}%")
print(f"Valor Líquido Final da Empresa: R$ {valor_liquido_final:.2f}")