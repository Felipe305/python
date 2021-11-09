#Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd'; 

nome = ""

while(len(nome)<=3):
    nome = input("Digite seu nome: ")
    if(len(nome) <=3):
        print("O nome deve ter mais de 3 letras: ")

idade = -1
while idade < 0 or idade > 150:
    idade = int(input("Digite sua idade: "))
    if(idade < 0) or (idade > 150):
        print("Idade deve ser entre 0 e 150")

salario = 0 
while salario < 0:
    salario = float(input("Digite se salario: "))
    if (salario < 0 ):
        print("Seu salario deve ser maior que zero: ")
    
sexo = ""
while(sexo != "F") and (sexo != "M"):
    sexo = input("Digite seu sexo F - Feminino or M - Masculino: ").upper()
    if (sexo != "F") and (sexo != "M"):
        print("Você digitou uma letra errada que não é compativel com o genero!")

estado_civil = "A"
while("scvd".find(estado_civil)):
    estado_civil = input("Digite seu estado civil: ")
    if("scvd".find(estado_civil)<0):
        print("Estado civil deve ser informado como S (solteiro), C (casado),"\
            " V (viuvo) ou D (divorciado)")