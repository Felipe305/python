#Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
#Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

inteiro = []
pares = []
impares = []

for i in range(0,20):
    numero = int(input("Digite um número: "))
    inteiro.append(numero)
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print(inteiro)
print(pares)
print(impares)