#Faça um Programa que peça as quatro notas de 10 alunos,
#calcule e armazene num vetor a média de cada aluno,
#imprima o número de alunos com média maior ou igual a 7.0.


notas = []

for i in range(2):
    nota = 0
    print(f"\nAluno:{i+1}\n ")
    for i in range(4):
        nmr = float(input("Digite a nota {}: ".format(i+1)))
        nota += nmr
    notas.append(nota / 4)

print(notas)

qnt = 0

for i in notas:
    if i >= 7:
        qnt += 1

print(qnt)

