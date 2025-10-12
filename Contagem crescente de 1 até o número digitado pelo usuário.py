# Contagem crescente de 1 até o número digitado pelo usuário

numero = int(input("Digite um numero para a contagem: "))
print("Iniciando contagem...")

for n in range(1,numero + 1):

    print(f"Número que estou trabalhando agora: {n}")
print("Contagem concluída! O laço foi finalizado.")