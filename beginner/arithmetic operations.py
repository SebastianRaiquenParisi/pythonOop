from math import *

print(8/3)  # float op
print(8//3)  # int op
print(10**3)  # power
x = 10
x -= 4
print(x)
x += 4
print(x)
x -= 11.3
print(abs(x))
print(round(x))
x = 2
print(f'{pow(x, 5)} (x ** 5)')
print(f'{min(x, 6)} minimo')
print(f'{max(x, 6)} maximo')
x = 3.4
print(f'{round(x)} redondeo')

# a partir de aca hay cosas de math
print(f'{floor(x)} redondeo abajo')
print(f'{ceil(x)} redondeo arriba')
print(f'{sqrt(x)} square root \n')

num1 = float(input('por favor ingrese el primer numero: '))
operador = input('por favor ingrese el operador (* / - + %): ')
num2 = float(input('por favor ingrese el segundo numero: '))

resultado = -1;
if operador == '/':
    resultado = num1/num2
elif operador == '*':
    resultado = num1*num2
elif operador == '+':
    resultado = num1+num2
elif operador == '%':
    resultado = num1%num2
elif operador == '-':
    resultado = num1-num2
print(f'{resultado}')



