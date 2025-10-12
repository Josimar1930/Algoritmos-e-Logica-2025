# Repetição de simbolo

simbolo = input("Digite um símbolo (ex: #, *, @): ")

quantidade = int(input("Digite a quantidade de repetições desejada: "))

print("\n----- Padrão Gerado -----")

for i in range(quantidade):
  print(simbolo)

print("-------------------------------")