print('\033[1;4mDesafio 68 -  Jogo do Par ou Ímpar\033[m')
print('\033[1mFaça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, \nmostrando o total de vitórias consecutivas que ele conquistou no final do jogo.\033[m')
from random import randint
print('\033[1;35m~~\033[m'*20)
print('          \033[1;36mJogo do Par ou Ímpar\033[m')
print('\033[1;35m~~\033[m'*20)
print('Vamos brincar Par ou Ímpar? Escolha um número entre 0 e 10. \nQuando eu contar até três, veremos quem vai ganhar.')
ia = randint(0, 10)
choice = str(input('Qual você escolhe? [P/I] ')).strip().upper()[0]
while True:
    jogador = int(input('Escolha um número entre 0 e 10: '))
    soma = jogador + ia
    if choice in 'Ii':
        if soma % 2 == 1:
            print(f'Você escolheu \033[1;36m{jogador}\033[m, eu escolhi \033[1;33m{ia}\033[m. A soma deles é \033[1;35mÍmpar\033[m. Você ganhou!')
            break
        elif soma % 2 == 0:
            print(f'Você escolheu \033[1;36m{jogador}\033[m, eu escolhi \033[1;33m{ia}\033[m. A soma deles é \033[1;31mPar\033[m. Tente novamente!')
    elif choice in 'Pp':
        if soma % 2 == 0:
            print(f'Você escolheu \033[1;36m{jogador}\033[m, eu escolhi \033[1;33m{ia}\033[m. A soma deles é \033[1;31Par\033[m. Você ganhou!')
            break
        if soma % 2 == 1:
            print(f'Você escolheu \033[1;36m{jogador}\033[m, eu escolhi \033[1;33m{ia}\033[m. A soma deles é \033[1;35mÍmpar\033[m. Tente novamente!')


#print(f'Você escolheu {jogador}, eu escolhi {ia}. A soma deles é Par. Você ganhou!')
#and choice == 'Pp'