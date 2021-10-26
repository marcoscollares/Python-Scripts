print('Desafio 27 - Primeiro e último nome de uma pessoa')

print('Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.')

nomecompleto = input('Digite o teu nome completo: ').upper().strip().title()
nome = nomecompleto.split()
primeiro = nome[0].capitalize()
ultimo = nome[len(nome)-1]
#ultimo = nome[-1].capitalize()

print('O teu nome completo é {}.'.format(nomecompleto))
print('O teu primeiro nome é {}.'.format(primeiro))
print('O teu último nome é {}.'.format(ultimo))