import random
import time
print('Desafio 28 - Jogo da Adivinhação v.1.0')

print("""Escreva um programa que faça o computador "pensar" em um número inteiro 
entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido 
pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.""")

print('₪'*60)
print('Vou pensar em um número entre 0 e 5. Tenha adivinhar qual número é esse! ')
print('₪'*60)
num = int(random.randint(0,5)) #Geração de número randômico
guess = int(input('Adivinhe qual número o computador pensou: ')) #Tentativa de adivinhação
print('PROCESSANDO...')
time.sleep(1)
if guess == num:
    print('Você acertou! Parabéns!!!')
else:
    print('Que pena! Você errou! Eu pensei no número {} e não no {}.'.format(num, guess))
print('Vamos jogar novamente?')



