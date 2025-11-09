caracter_simbolo = input("Digite um caracter ou símbolo: ")

repetir = "sim"

while repetir <= 20:
    while repetir.lower() == "sim":

        print(caracter_simbolo * 20)
    
   
    repetir = input("Deseja ver outra linha? (Digite SIM para continuar): ")


print("Gerador encerrado. Obrigado!")
