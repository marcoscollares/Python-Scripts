from random import randint
import time
print('\033[1;4mDesafio 45 - GAME: Pedra, Papel e Tesoura\033[m')
print("""\033[1mCrie um programa que faça o computador jogar Jokenpô com você.\033[m""")
print('\033[1;35m♣\033[m'*60)
print('                        \033[1;4mPEDRA, PAPEL E TESOURA\033[m')
print('\033[1;35m♣\033[m'*60)
print("""Vamos jogar Pedra, Papel e Tesoura? Escolha entre as opções abaixo:
\033[1m0 - Pedra
1 - Papel
2 - Tesoura\033[m""")
item = ('Pedra', 'Papel', 'Tesoura')
jogador = int(input('Digite a opção desejada: '))
ia = randint(0,2)
print('\033[1;31mJOKEEEENNNPÔ!!! \033[m')
time.sleep(2)
print('\033[1;36m-=\033[m' * 13)
print('\033[1mO Computador jogou {}.\033[m'.format(item[ia]))
print('\033[1mO Jogador jogou {}.\033[m'.format(item[jogador]))
print('\033[1;36m-=\033[m' * 13)
if ia == 0:
    if jogador == 0:
        print('Temos um empate!')
    elif jogador == 1:
        print('O Jogador ganhou!')
    elif jogador == 2:
        print('O Computador ganhou!')
    elif jogador > 2:
        print('Jogada Inválida!')
elif ia == 1:
    if jogador == 0:
        print('O Computador ganhou!')
    elif jogador == 1:
        print('Temos um empate!')
    elif jogador == 2:
        print('O Jogador venceu!')
    elif jogador > 2:
        print('Jogada Inválida!')
elif ia == 2:
    if jogador == 0:
        print('O Jogador ganhou!')
    elif jogador == 1:
        print('O Computador ganhou!')
    elif jogador == 2:
        print('Temos um empate!')
    elif jogador > 2:
        print('Jogada Inválida!')