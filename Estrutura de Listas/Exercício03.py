#Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

notas = []

for i in range(0,4):
    notas.append(float(input("Digite uma nota:")))
    
soma = 0.0
print("Notas digitadas: ")
for i in range(0,4):
    print("Nota %d: %.2f" % (i, notas[i]))
    soma += notas[i]

    print("A média das notas é: % .2f" % (soma/4.0))