print('Desafio 67 - Tabuada v3.0')
print('Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. \nO programa será interrompido quando o número solicitado for negativo. ')
num = tabuada = result = 0
from time import sleep
while True:
    num = int(input('Digite um número: '))
    if num < 0:
        break
    print('=' * 20)
    for tab in range(1,11):
        tabuada = tab
        print(f'| {num}  x  {tabuada:2}  =  {num*tabuada:2} |')
    print('=' * 20)
sleep(1)
print('.', end='')
sleep(1)
print('.', end='')
sleep(1)
print('.')
sleep(1)
print('Programa finalizado. Até mais!')

'''ask = str(input('Você quer repetir? [S/N] ')).upper().strip()[0]
    if ask in 'Ss':
        print('-='*13)
    elif ask in 'Nn':
        print('Programa encerrando', end='')
        break
    else:
        print('Opção Inválida. Tente novamente!')
        print('Programa encerrando', end='')
        break'''