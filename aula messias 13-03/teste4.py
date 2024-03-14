#progra,a que calcule o fatorial de um numero que usuario digita usando whilw=true
while True:
    n = int(input("Digite um numero inteiro: "))
    fatorial = 1
    for i in range(1, n+1):
        fatorial = fatorial * i
    print(fatorial)
    continuar = input("Deseja continuar? (s/n)")
    if continuar == "n":
        break