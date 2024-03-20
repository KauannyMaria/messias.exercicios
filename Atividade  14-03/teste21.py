#Letra L
#programa que calcula a soma do fatorial de 15 numero com while
cont1=1
soma=0
while cont1 <=15:
    fatorial=1
    cont2=1
    while cont2<=cont1:
        fatorial*=cont2
        cont2+=1
    soma+=fatorial
    cont1+=1
print("O somatorio dos fatoriais de 1 a 15 é", soma)