from datetime import date 

atual = date.today().year

nascimento = int(input("Digite o ano de nascimento: "))
idade = atual - nascimento 
print("O atleta tem {} anos ".format(idade))

if idade <= 9:
    print("Mirim")
elif idade <= 14:
    print("Infantil")
elif idade <= 19:
    print("Junior")
elif idade <= 25:
    print("Sênior")
else:
    print("Master")