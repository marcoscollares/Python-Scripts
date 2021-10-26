print('\033[1;4mDesafio 50 - Soma dos pares\033[m')
print('\033[1mDesenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.\33[m')
soma = 0
cont = 0
for n in range(1,7):
    num = int(input('Digite o {}º número: '.format(n)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Você digitou \033[1;31m{}\033[m números pares e a soma de todos eles é \033[1;35m{}\033[m.'.format(cont, soma))

