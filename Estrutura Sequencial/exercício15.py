#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês,
# sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo:


valhora = float(input("Quantos você ganha por hora:"))
horas_trabalhada = int(input("Digite quantas horas trabalhou:"))
salario = valhora*horas_trabalhada

print(f"Seu salario total é: {salario}")

