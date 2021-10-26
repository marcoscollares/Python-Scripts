print('\033[1;4mDesafio 54 - Grupo da Maioridade\033[m')
print('\033[1mCrie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.\033[m')
from datetime import date
totmenor = 0
totmaior = 0
for id in range(0,7):
    ano = int(input('Digite o ano de nascimento: '))
    if (date.today().year - ano) < 21:
        totmenor += 1
    else:
        totmaior += 1
print('Número de pessoas menor de idade: \033[1;33m{}\033[m \nNúmero de pessoas maior de idade: \033[1;36m{}\033[m.'.format(totmenor, totmaior))
