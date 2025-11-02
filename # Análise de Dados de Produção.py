# Análise de Dados de Produção

numero_total_pecas = int(input("Digite o número total de peças a serem inspecionadas: "))

TOLERANCIA = 0.5
TAMANHO_IDEAL = 15.0

soma_dos_tamanhos = 0.0
pecas_fora_tolerancia = 0

for i in range(1, numero_total_pecas + 1):
    tamanho_medido = float(input(f"Digite a medida da peça {i} em cm: "))
    soma_dos_tamanhos += tamanho_medido

    desvio = abs(tamanho_medido - TAMANHO_IDEAL)

    if desvio > TOLERANCIA:
        pecas_fora_tolerancia += 1

media_tamanho = soma_dos_tamanhos / numero_total_pecas

print(f"Média de tamanho das peças: {media_tamanho:.2f} cm")
print(f"Peças fora da tolerância: {pecas_fora_tolerancia}")

if pecas_fora_tolerancia == 0:
    print("Lote Aprovado: Qualidade Perfeita (0 peças fora da tolerância).")
elif pecas_fora_tolerancia <= 2:
    print("Lote Aceitável: Pequena correção necessária.")
else:
    print("Lote Reprovado: Alta taxa de defeito.")
