#Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:

numero = int(input("Digite o número que você quer ver a tabuada:"))

print("Tabuada de, {} :".format(numero))
for i in range(1, 11):
    print(numero, "X", i, "=", (numero * i))

