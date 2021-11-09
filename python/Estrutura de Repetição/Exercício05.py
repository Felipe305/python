#Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.

populacaoA = 0
crescimentoA = 0

while(populacaoA <= 0):
    populacaoA = float(input("Informe a populaçãoA: "))
    if populacaoA <= 0:
        print("PopulaçãoA deve ser um valor positivo!")
while(crescimentoA <= 0):
    crescimentoA = float(input("Informe o porcentual do crescimento do pais A "))
    if crescimentoA <= 0:
        print("O porcentual deve ser umm valor positivo! ") 
populacaoB = populacaoA
while populacaoB <= populacaoA:
    populacaoB = float(input("Informe a populaçãoB: "))
    if populacaoB <= populacaoA:
        print("A população deve ser um valor positivo: ")
crescimentoB = crescimentoA
while crescimentoB >= crescimentoA:
    crescimentoB = float(input("Informe o porcentual do crescimento do pais B: "))
    if crescimentoB >= crescimentoA:
        print("Percentual de crescimento do pais B deve ser menor que o do \n pais A")

crescimentoA = 1 + (crescimentoA/100)
crescimentoB = 1 + (crescimentoB/100)

ano = 1

while populacaoA <= populacaoB:
    populacaoA *= crescimentoA
    populacaoB *= crescimentoB
    ano += 1

print(f"Serão necessarios {ano} anos para que a população do pais A \n ultrapasse a população do pais B")