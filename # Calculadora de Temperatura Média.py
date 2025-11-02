# Calculadora de Temperatura Média

quantidade_total_dias = int(input("Digite a quantidade total de dias que serão analisados: "))

soma_das_temperaturas = 0.0

for i in range (1,quantidade_total_dias + 1):
    temperatura_graus_celsius = float(input(f"Informe a temperatura do dia {i} (em C°): "))
    soma_das_temperaturas += temperatura_graus_celsius

temperatura_media = soma_das_temperaturas / quantidade_total_dias

if temperatura_media > 28:
    print("Média de temperatura: Clima Quente.")

elif 18 <= temperatura_media <= 28:
    print("Média de temperatura: Clima Agradável.")

else:
    print("Média de temperatura: Clima Frio.")
print(f"Média final da temperatura do período: {temperatura_media:.2f}")