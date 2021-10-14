#Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

vet1 = []

for i in range(5):
    vet1.append(int(input("Digite um número inteiro {}: ".format(i+1))))

soma = 0
for i in vet1:
    soma += i

print(vet1)
print(soma)