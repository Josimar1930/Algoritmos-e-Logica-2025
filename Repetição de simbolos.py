# Repetição de simbolo
simbol = input("Digite um símbolo (ex: #, *, @): ")

quantidade = int(input("Digite a quantidade de repetições desejada: "))

print("\n----- Padrão Gerado -----")

for i in range(quantidade):
  print(simbol)

print("-------------------------------")