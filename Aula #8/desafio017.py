print('\033[1;4mDesafio 17 - Catetos e Hipotenusa\033[m')
import math
co = float(input('Digite o cumprimento do cateto oposto: '))
ca = float(input('Digite o cumprimento do cateto adjacente: '))
hipo = math.hypot(co, ca)

print('O comprimento da hipotenusa do triângulo retângulo é de \033[35m{:.2f}.\033[m'.format(hipo))

print('\033[36m=\033[m'*40)

#=============================

from math import hypot

oposto = float(input('Digite o cumprimento do cateto oposto: '))
adjacente = float(input('Digite o cumprimento do cateto adjacente: '))

print('O comprimento da hipotenusa do triângulo retângulo é de {:.2f}.'.format(math.hypot(oposto, adjacente)))

print('='*40)

#============================

op = float(input('Digite o valor do cateto oposto: '))
ad = float(input('Digite o valor do cateto adjacente: '))
hi = (op ** 2 + ad ** 2) ** (1/2)

print('O valor da hipotenusa é de {:.2f}.'.format(hi))

