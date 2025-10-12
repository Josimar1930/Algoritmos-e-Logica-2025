# Tabuada 

numero = int(input("Digite o número inteiro para ver a tabuada de 1 a 9: "))

print(f"\n--- Tabuada do {numero} ---")

for i in range(1, 11):
  resultado = numero * i
  print(f"{numero} x {i} = {resultado}")

print("--------------------------")