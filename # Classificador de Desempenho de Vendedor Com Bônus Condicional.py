# Classificador de Desempenho de Vendedores com Bônus Condicional

numero_vendedores = int(input("Digite o número total de vendedores a serem avaliados: "))
valor_base_bonus = 500
pontuacao_total_equipe = 0.0
vendedores_acima_meta = 0      
botoes_alerta_ativados = 0

for _ in range(numero_vendedores):
    pontuacao_vendedor = int(input("Digite a Pontuação Final de Vendas do vendedor (0-100): "))
    pontuacao_total_equipe += pontuacao_vendedor

    if pontuacao_vendedor >= 90:
        vendedores_acima_meta += 1
    elif pontuacao_vendedor < 50:
        botoes_alerta_ativados += 1
media_equipe = pontuacao_total_equipe / numero_vendedores
bonus_base_total = numero_vendedores * 500.00
if media_equipe > 80 and botoes_alerta_ativados == 0:
    FMB = 1.20  
elif vendedores_acima_meta > (numero_vendedores / 2) or (70 <= media_equipe <= 80):
    FMB = 1.05
elif botoes_alerta_ativados > 1:
    FMB = 0.80
else:
    FMB = 1.00
Valor_Final_Total = bonus_base_total * FMB
print(f"Média de Pontuação da Equipe: {media_equipe:.2f}")
print(f"Número de Alertas: {botoes_alerta_ativados}")
print(f"Valor Final Total a Pagar: R$ {Valor_Final_Total:.2f}")