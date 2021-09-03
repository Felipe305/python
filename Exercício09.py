import math 
#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius#

graus_fahrenheit = int(input("Digite a temperatura em graus Fahrenheit:"))
temperatura = format((graus_fahrenheit-32)/1.8,".2f")
print(f"A temperatura é: {temperatura}°C")


