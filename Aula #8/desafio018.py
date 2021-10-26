'''print('Desafio 18 - Seno, Cosseno, Tangente')
import math
ang = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(ang))
cosseno = math.cos(math.radians(ang))
tangente = math.tan(math.radians(ang))

print('O ângulo {} tem os valores de seno {:.2f}, cosseno {:.2f} e tangente {:.2f}.'.format(ang, seno, cosseno, tangente))

print('='*40)'''

#==============================
print('\033[1;4mDesafio 18 - Seno, Cosseno, Tangente\033[m')

from math import sin, cos, tan, radians

angulo = float(input('Digite o valor do ângulo: '))
rad = radians(angulo)

print("""O valor do ângulo  é de \033[35m{:.2f}\033[m, o seu seno é \033[36m{:.2f}\033[m, o cosseno \033[36m{:.2f}\033[m 
e a tangente \033[35m{:.2f}\033[m.""".format(angulo, sin(rad), cos(rad), tan(rad)))