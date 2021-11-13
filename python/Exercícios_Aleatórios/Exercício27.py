from time import sleep
#Função que descobre o maior.

def maior(* num):
    cont = maior = 0
    print("\nAnalisando os valores passados... ")
    for valor in num:
        print(f"{valor}", end=" ", flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor 
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f"Foram informados {cont} valores ao todo ")
    print(f"O maior valor informado foi {maior}. ")


maior(2,7,8,6,9,0,1)
maior(1,5,6,7,8)
maior(1,2)
maior(3,0,4)
maior()