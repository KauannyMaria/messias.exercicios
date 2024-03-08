#programa que testa se tres numeros formam um triangulo
#lendo os lados do triangulo
a=int(input("Digite o lado a: "))
b=int(input("Digite o lado b: "))
c=int(input("Digite o lado c: "))
#testando se os lados formam um triangulo
if a<b+c and b<a+c and c<a+b:
    if a==b==c:
        print("triangulo equilatero")
        
    elif a==b or a==c or b==c:
        print("triangulo isoceles")
    else:
        print("os lados nao foram um trangulo")