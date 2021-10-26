#COPIAR NO CADERNO

print('\033[1;4mDesafio 58 - Jogo da Adivinhação 2.0\033[m')
print('\033[1mMelhore o jogo do DESAFIO 28 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador \nvai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.\033[m')

print('\033[1;35m=-\033[m'*20)
print('        \033[1;36mJogo da Adivinhação 2.0\033[m')
print('\033[1;35m-=\033[m'*20)

from random import randint
print('Vamos brincar? Irei pensar em um número entre 0 e 10. Tente adivinhar qual número eu pensei!')
computador = int(randint(0,10))
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('Parabéns! Eu pensei no número \033[1;31m{}\033[m e você digitou \033[1;33m{}\033[m.'.format(computador, jogador))
print('Você acertou com \033[1;34m{}\033[m tentativas.'.format(palpites))

#--------------------------

"""print('Vamos brincar? Irei pensar em um número entre 0 e 10. Tente adivinhar qual número eu pensei!')
num = int(randint(0,10))
tentativas = 1
guess = int(input('Digite um número: '))
while guess != num:
    guess = int(input('Tente novamente! Digite um número: '))
    tentativas += 1
print('Parabéns! Eu pensei no número \033[1;31m{}\033[m e você digitou \033[1;33m{}\033[m.'.format(num, guess))
print('Você acertou com \033[1;34m{}\033[m tentativas.'.format(tentativas))
print('FIM')"""