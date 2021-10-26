print('\033[1;4mDesafio 75 - Análise de dados em uma Tupla\033[m')
print('''\033[1mDesenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.\033[m''')
print('')
num = (int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')))
tupla = num
print('')
if 9 in tupla:
    print(f'O número 9 apareceu \033[1;33m{tupla.count(9)}\033[m vez(es).')
else:
    print('O número 9 não foi digitado nenhuma vez.')
if 3 in tupla:
    print(f'O primeiro número três apareceu na \033[1;36m{tupla.index(3)+1}ª\033[m posição.')
else:
    print('O número 3 não foi digitado em nenhuma posição.')
print(f'A tupla tem o(s) número(s) como par(es):', end=' ')
for n in tupla:
    if n % 2 == 0:
        print(f'\033[1;35m{n}\033[1m', end=' ')

