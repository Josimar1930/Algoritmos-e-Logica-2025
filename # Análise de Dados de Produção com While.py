# Análise de Dados de Produção

# Exercício: Análise de Dados de Produção (usando WHILE)

# Entrada de dados
numero_total_de_pecas = int(input("Informe o número total de peças a serem inspecionadas: "))

# Constantes
TOLERANCIA = 0.5
TAMANHO_IDEAL = 15.0

# Variáveis acumuladoras
soma_dos_tamanhos = 0.0
pecas_fora_tolerancia = 0

# Controle do laço
contador = 1

# Laço de repetição WHILE
while contador <= numero_total_de_pecas:
    tamanho_medido = float(input(f"Informe o tamanho medido da peça {contador}: "))
    soma_dos_tamanhos += tamanho_medido

    media_tamanho = tamanho_medido - TAMANHO_IDEAL

    if media_tamanho > TOLERANCIA:
        pecas_fora_tolerancia += 1

    contador += 1

media_tamanho = soma_dos_tamanhos / numero_total_de_pecas

print(f"Média de tamanho das peças: {media_tamanho:.2f} cm")
print(f"Peças fora da tolerância: {pecas_fora_tolerancia}")

if pecas_fora_tolerancia == 0:
    print("Lote Aprovado: Qualidade Perfeita (0 peças fora da tolerância).")
elif pecas_fora_tolerancia <= 2:
    print("Lote Aceitável: Pequena correção necessária.")
else:
    print("Lote Reprovado: Alta taxa de defeito.")