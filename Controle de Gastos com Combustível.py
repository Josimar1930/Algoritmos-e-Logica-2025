# Controle de Gastos com Combustível

dias_viagem = int(input("Digite a quantidade de dias em que houve viagem: "))
total_km_percorridos = 0.0

for dia in range(dias_viagem):
    km_dia = float(input(f"Digite os KM percorridos no dia {dia + 1}: "))
    total_km_percorridos += km_dia
total_litros = total_km_percorridos / 12
custo_total = total_litros * 4.80
if custo_total > 500.00:
    print("Alerta de Gastos: O custo total com combustível foi alto (Acima de R$ 500,00).")
else:
    print("Gastos sob controle: O custo total com combustível foi baixo ou moderado.")
print(f"Total de KM percorridos: {total_km_percorridos:.2f} km")
print(f"Custo total com combustível: R$ {custo_total:.2f}")