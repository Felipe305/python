#Tabuada

tabuada = int(input("Digite um número: "))

print("A tabuada de {} ".format(tabuada))

for i in range(1,11):
    print(tabuada, "X", i, "=", (tabuada*i))
