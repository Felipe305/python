#Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

vetor = []
vogais = ["A","E","I","O","U"]

for i in range(0,10):
    vetor.append(input("Digite alguma coisa: ").upper())

totalConsoante = 0
consoantes = []

for i in range(0,10):
    if vetor[i] not in vogais:
        consoantes.append(vetor[i])
        totalConsoante += 1
    
print("Você digitou %d consoantes " % totalConsoante)
print(consoantes)
