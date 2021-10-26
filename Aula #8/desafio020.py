import random

print('\033[1;4mDesafio 20 - Sorteando uma ordem na lista\033[m')
import math
print('Um professor quer sortear a ordem de apresentação de trabalhos dos alunos. \nFaça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.')

a1 = input('Digite o nome do primeiro aluno: ')
a2 = input('Digite o nome do segundo aluno: ')
a3 = input('Digite o nome do terceiro aluno: ')
a4 = input('Digite o nome do quarto aluno: ')
sorteio = [a1, a2, a3, a4]
random.shuffle(sorteio)

print('A ordem de apresentacao dos trabalhos sera: \033[35m{}\033[m.'.format(sorteio))

print('\033[36m=\033[m'*40)

#===========================

'''from random import shuffle
aluno1 = str(input('Digite o nome do aluno: '))
aluno2 = str(input('Digite o nome do aluno: '))
aluno3 = str(input('Digite o nome do aluno: '))
aluno4 = str(input('Digite o nome do aluno: '))
lista = [aluno1, aluno2, aluno3, aluno4]
print('A ordem escolhida é {}.'.format(shuffle(lista)))'''