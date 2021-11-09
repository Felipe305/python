#Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

quantidade = 0

while quantidade <= 0:
    quantidade = int(input("Digite um número: "))
    if quantidade <= 0:
        print("Quantidade deve ser positiva:")

soma = 0 
for i in range(0, quantidade):
    numero = int(input("Digite um número:"))
    if "maior" not in vars() or numero > maior:
        maior = numero

    if "menor" not in vars() or numero < menor:
        menor = numero 

    soma += numero 

print("Menor numero", menor)
print("Maior numero", maior)
print("Soma dos numeros", soma)