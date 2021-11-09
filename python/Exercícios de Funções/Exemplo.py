# Dobrar uma lista     
def dobra(lst):
    pos=0 
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [1, 2, 5, 7, 9, 8]
dobra(valores)
print(valores)