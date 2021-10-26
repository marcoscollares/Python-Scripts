print('\033[1;4mDesafio 47 - Contagem dos Pares\033[m')
print('\033[1mCrie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.\033[m')
from time import sleep
for pares in range(2, 51, 2):
    print(pares, end=' ')
    sleep(0.2)
print('FIM')