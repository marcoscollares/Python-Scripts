print('Desafio 84 - Lista composta e análise de dados')
print('''Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.''')
print('')
dado = list()
grupo = list()
num = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append((int(input('Peso: '))))
    grupo.append(dado[:])
    dado.clear()
    num += 1
    ask = str(input('Deseja continuar? [S/N] '))
    if ask in 'Ss':
        print('')
    else:
        break
'''for p in grupo:
    if p[1] >= max(grupo):
        print(f'O maior peso foi {p[1]}.')
    elif p[1] <= min(grupo):
        print(f'O menor peso foi {p[1]}.')'''
print(f'Ao todo, você cadastrou {num} pessoas.')
print(f'O maior peso foi de {max(grupo[::2])} Kg. Peso de .')
print(f'O menor peso foi {min(grupo[::2])}.')
