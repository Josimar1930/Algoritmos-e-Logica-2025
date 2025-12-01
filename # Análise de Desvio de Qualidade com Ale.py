# Análise de Desvio de Qualidade com Alerta de Risco

padrao_ideal = 50.0
limite_maximo_desvio = 10.0 
desvios_registrados = []
dias_consecutivos_baixo_padrao = 0

while True:
    medida_peca = float(input("Digite a Medida da Peça (0 para sair): "))
    if medida_peca == 0:
        motivo_parada = "Entrada de 0 pelo usuário."
        break
    desvio = abs(medida_peca - padrao_ideal)
    desvios_registrados.append(desvio)
    if desvio > limite_maximo_desvio:
        dias_consecutivos_baixo_padrao += 1
        if dias_consecutivos_baixo_padrao >= 3:
            print("ALERTA MÁXIMO! Produção Paralisada por Risco de Qualidade!")
            motivo_parada = "Produção paralisada por risco de qualidade."
            break
    else:
        dias_consecutivos_baixo_padrao = 0
media_desvio = sum(desvios_registrados) / len(desvios_registrados) if desvios_registrados else 0
print(f"Média de Desvio: {media_desvio:.2f}")
print(f"Motivo da Parada: {motivo_parada}")