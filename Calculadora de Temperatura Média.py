# Calculadora de Temperatura Média

total_dias = int(input("Digite a quantidade total de dias que serão analisados: "))
soma_das_temperaturas = 0.0
for dia in range(total_dias):
    temperatura = float(input(f"Digite a temperatura do dia {dia + 1} em graus Celsius: "))
    soma_das_temperaturas += temperatura
media_temperatura = soma_das_temperaturas / total_dias 
if media_temperatura > 28:
    classificacao = "Clima Quente."
elif 18 <= media_temperatura <= 28:
    classificacao = "Clima Agradável."
else:
    classificacao = "Clima Frio."
print(f"Média de temperatura: {media_temperatura:.2f}°C - {classificacao}")