#Letra B
#tabuada de multiplicação de um numero qualquer em while
while True:
    n = int(input("Digite um numero para ver a tabuada: "))
    print("Tabuada de multiplicação de um numero", n)
    i = 1
    while i <= 10:
        print(n, "x",i, "=", n*i)
        i+=1
    continuar=input("Deseja continuar? (sim/nao)")
    if continuar=="nao":
        break