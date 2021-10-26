print('\033[1;4mDesafio 72 - Número por Extenso\033[m')
print('\033[1mCrie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. \nSeu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.\033[m]')

print('*'*30)
print(f'{"NÚMEROS POR EXTENSO":^30}')
print('*'*30)

numex = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
         'seis', 'sete', 'oito', 'nove', 'dez',
         'onze', 'doze', 'treze', 'catorze', 'quinze',
         'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    user = int(input('Digite um número entre 0 e 20: '))
    if 0 > user > 20:
        print('Tente novamente!')
    elif 0 <= user <= 20:
        print(f'Você digitou o número \033[1;33m{numex[user]}\033[m.')
        ask = input('Deseja continuar? (S/N) ')
        if ask in 'Nn':
            break
        while ask not in 'SsNn':
            ask = input('Tente novamente! Deseja continuar? (S/N) ')



'''while True:
    user = int(input('Digite um número entre 0 e 20: '))
    if 0 <= user <= 20:
        break
    print('Tente novamente!')
print(f'Você digitou o número {numex[user]}.')'''