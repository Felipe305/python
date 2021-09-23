#Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.

inicial = int(input("Digite um numero: "))
final = inicial

while final <= inicial:
    final = int(input("Digite um numero: "))
    if final <= inicial:
        print("O numero final deve ser maior que eo número inicial")

for i in range(inicial,final + 1):
    print(i)





