#Letra L
#programa que calcula a soma do fatorial de 15 numero com for
soma = 0
for cont in range(1, 16):
    fatorial = 1
    for i in range(1, cont + 1):
        fatorial *= i
    soma += fatorial
print("O somatório dos fatoriais de 1 a 15 é", soma)