print('\033[1;4mDesafio 46 - Contagem Regressiva\033[m')
print('\033[1mFaça um programa que mostre na tela uma contagem regressiva para o estouro de \nfogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.\033[m')

print('\033[1;35m=-\033[m'*24)
print('\033[1m CONTAGEM REGRESSIVA PARA OS FOGOS DE ARTIFÍCIO\033[m')
print('\033[1;35m=-\033[m'*24)
from time import sleep
from emoji import emojize
for contagem in range(10,0,-1):
    print(contagem)
    sleep(1)
print(emojize('BOOM!!! :fireworks: :boom:',use_aliases=True))
