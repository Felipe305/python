#Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
#Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.


numeros = []
pares = []
impares = []

for i in range(0, 20):
    numero = int(input('Informe um numero: '))
    numeros.append(numero)
    if (numero % 2 == 0):
        pares.append(numero)
    else:
        impares.append(numero)

print(numeros)
print(pares)
print(impares)