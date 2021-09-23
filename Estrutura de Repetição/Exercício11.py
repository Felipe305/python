#Altere o programa anterior para mostrar no final a soma dos números.

inicial = int(input("Digite um numúmero: "))
final = inicial

while final <= inicial:
    final = int(input("Digite um número: "))
    if final <= inicial:
        print("O número final deve ser maior que o número inicial: ")

soma = 0
for i in range(inicial,final + 1):
    soma += i
    print(i)
    
print("A soma dos números é: {}10".format(soma))