#COPIAR NO CADERNO
print('Desafio 74 - Maior e menor valores em Tupla')
print('Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem \nde números gerados e também indique o menor e o maior valor que estão na tupla.')

from random import randint
num = (randint(1,10), randint(1,10), randint(1,10), randint(1, 10), randint(1, 10))
print(f'Os números gerados foram: \033[1;35m{num}\033[m.')
print(f'O menor valor é \033[1;36m{min(num)}\033[m.')
print(f'O maior valor é \033[1;33m{max(num)}\033[m.')
