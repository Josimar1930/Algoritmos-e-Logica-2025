# Média de notas de alunos

quantidade = int(input("Informe a quantidade de alunos na sala: "))

soma_das_notas = 0

for n in range (1,quantidade):
    nota = float(input(f"Informe a nota do aluno {n}: "))
    soma_das_notas=soma_das_notas + nota
media = soma_das_notas/quantidade

print(f"O valor da media dos alunos é: {media:.2f} ")
