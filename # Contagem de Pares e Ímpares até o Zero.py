# Contagem de Pares e Ímpares até o Zero

contador_pares = 0
contador_impares = 0
numero_digitado = 1 

while numero_digitado != 0:
    numero_digitado = int(input("Digite um número inteiro (ou 0 para encerrar): "))
    if numero_digitado != 0:
        if numero_digitado % 2 == 0:
            contador_pares += 1
            print(f"Número {numero_digitado} é par. Contador de pares: {contador_pares}")
        else:
            contador_impares += 1
            print(f"Número {numero_digitado} é ímpar. Contador de ímpares: {contador_impares}")
print(f"\nO total de números pares digitados é: {contador_pares}")
print(f"O total de números ímpares digitados é: {contador_impares}")