print('\033[1;4mDesafio 16 - Quebrando um número\033[m')

import math
num = float(input('Digite o número real aqui: '))
inteiro = math.trunc(num)

print('O número real digitado foi \033[35m{}\033[m. A sua porção inteira é \033[36m{}\033[m.'.format(num, inteiro))

print('\033[31m=\033[m'*30)

#=========================================

from math import trunc

n = float(input('Digite um número real aqui: '))

print('O valor digitado foi {} e a sua porção inteira é {}.'.format(num, math.trunc(n)))

print('='*30)

#=========================================

numero = float(input('Digite um valor a seguir: '))

print('O valor digitado foi {} e a sua porção inteira é {}.'.format(numero, int(numero)))


