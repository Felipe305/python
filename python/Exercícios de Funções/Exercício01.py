# Faça um programa para imprimir:

# 1
#    2   2
#    3   3   3
#    .....
#    n   n   n   n   n   n  ... n

# para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.

def imprime(n):
    for i in range(n):
            print(n, end= " ")
    print("\n")

cont  = 0
while cont < 5:
    cont += 1
    numero = int(input("Digite o número de usúario: "))
    imprime(numero)