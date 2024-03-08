valor_hora_aula = float(input("digite o valor da hora aula: "))
horas_trabalhadas = float(input('digite o numero de horas trabalhadas no mês: '))
percentual_inss = float(input("digite o percentual de desconto do inss (em %): "))
salario_bruto = valor_hora_aula * horas_trabalhadas
desconto_inss = salario_bruto * (percentual_inss / 100)
salario_liquido = salario_bruto - desconto_inss
print("O salário líquido do professor é: R$", salario_liquido)