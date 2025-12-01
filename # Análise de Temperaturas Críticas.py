# Análise de Temperaturas Críticas
registro_temperaturas = []
dias_criticos = 0
while True:
    temperatura = float(input("Digite a temperatura em Celsius (0 para sair): "))
    if temperatura == 0:
        break
    registro_temperaturas.append(temperatura)
for temp in registro_temperaturas:
    if temp > 30:
        print("Alerta Quente!")
        dias_criticos += 1
    elif temp < 10:
        print("Alerta Frio!")
        dias_criticos += 1
    else:
        print("Temperatura Agradável.")
print("Vetor Completo de Temperaturas:", registro_temperaturas)
print("Total de Dias Críticos:", dias_criticos)
