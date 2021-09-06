'''Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7'''

alt = float(input("Digite sua altura:"))
idealh = format((72.7*alt)-58, ".2f")
idealm = format((62.1*alt)-44.7, ".2f")
print(f"O peso ideal é:\n{idealh} para homens \n{idealm} para mulheres") 
