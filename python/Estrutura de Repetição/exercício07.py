#Faça um programa que leia 5 números e informe o maior número.

maior = 0

for i in range(1,6):
    numero = float(input("Digite um numero:"))
    if numero > maior:
        maior = numero 

print("O maior numero é {:.2f}".format(maior))