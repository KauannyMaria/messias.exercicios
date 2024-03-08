def celsius_para_fahrenheit(celsius):
    fahrenheit = (9 * celsius + 160) / 5
    return fahrenheit
celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = celsius_para_fahrenheit(celsius)
print("A temperatura em Fahrenheit é:", fahrenheit)