print('\033[1;4mDesafio 55 - Maior e Menor da Sequência\033[m')
print('\033[1mFaça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.\033[m')

maior = 0
menor = 0
for p in range(1,6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso é \033[1;35m{}\033[m.'.format(maior))
print('O menor peso é \033[1;36m{}\033[m.'.format(menor))