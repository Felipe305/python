#Sorteando um número na lista.
import random

lista = []

for i in range(5):
    while True:
        val = input("Digite um número: ")
        if val.isdigit():
            lista.append(val)
            break
        else:
            print("Digite um número camarada!")
print(random.choice(lista))
