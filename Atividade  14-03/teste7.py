##Letra D
#programa que mostra os somatorios dos numeros pares de 1 ate 500 com while
cont=1
while cont<=500:
    if cont%2==0:
        i=1
        somatorio=0
        while i<=cont:
            somatorio+=i
            i+=1
        print("O somatorio do numero: ",cont,"e: ", somatorio)
    cont+=1
print("Fim do programa")