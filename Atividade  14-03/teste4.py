#Letra B
#tabuada de multiplicação de um numero qualquer em for
while True:
    n = int(input("Digite um numero para ver a tabuada: "))
    print("Tabuada de multiplicação de um numero", n)
    for i in range(1,11):
        print(i, "x",n,"=", i*n)
    continuar=input("Deseja continuar? (sim/nao)")
    if continuar=="nao":
        break