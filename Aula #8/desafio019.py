'''import random

print('Desafio 19 - Sorteando alunos')

print('Um professor quer sortear  um dos seus quatro alunos para apagar o quadro. \nFaça um programa que ajude ele, lendo o nome dos alunose escrevendo na tela o nome do escolhido.' )

a1 = input('Digite o nome do primeiro aluno: ')
a2 = input('Digite o nome do segundo aluno: ')
a3 = input('Digite o nome do terceiro aluno: ')
a4 = input('Digite o nome do quarto aluno: ')
sorteio = a1, a2, a3, a4

print('O aluno escolhido foi {}.'.format(random.choice(sorteio)))

print('='*40)'''

#================

print('\033[1;4mDesafio 19 - Sorteando alunos\033[m')

from random import choice
aluno1 = input('Digite o nome do aluno: ')
aluno2 = input('Digite o nome do aluno: ')
aluno3 = input('Digite o nome do aluno: ')
aluno4 = input('Digite o nome do aluno: ')
lista = [aluno1, aluno2, aluno3, aluno4]
print('O aluno escolhido foi \033[31m{}\033[m.'.format(choice(lista)))
