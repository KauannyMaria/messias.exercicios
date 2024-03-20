#Letra K
#calcule o somatorio dos graos de trigo de um tabuleiro de xadres em while
cont=1
soma=0
while cont<=64:
    soma=(2**cont)-1
    print(soma)
    cont+=1
print("O total de graos de trigo é", soma)