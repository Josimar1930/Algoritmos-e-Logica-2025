# Verificador de paridade de números de 1 a 10

print("--- Classificador de Paridade de 1 a 10 ---")

for numero in range(1, 11):

    if numero % 2 == 0:
        print(f"{numero} é PAR.")
    else:
        print(f"{numero} é ÍMPAR.")

print("-------------FIM-----------------------")
