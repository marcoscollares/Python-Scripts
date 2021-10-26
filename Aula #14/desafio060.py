#COPIAR NO CADERNO
print('\033[1;4mDesafio 60 - Cálculo do Fatorial\033[m')
print("""\033[1mFaça um programa que leia um número qualquer e mostre o seu fatorial.
Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120\033[1m""")
from math import factorial
print('')
n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
#--------
'''n = int(input('Digite um número: '))
f = factorial(n)
print('O fatorial de {} é {}.'.format(n, f))'''

#-------------
'''fat = 1
i = 2
while i <= num:
    fat = fat*i
    i = i + 1
print("O valor de {} é = {}".format(num, fat))'''
