#Sorteando um número na lista.
import random

lista = []

for i in range(5):
    while True:
        val = (input("Digit eum número: "))
        if val.isdigit():
            lista.append(val)
            break
        else:
            print("Digite um número meu brother! ")

print(random.choice(lista))