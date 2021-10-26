print('Desafio 64 - Tratando vários valores v1.0')
print('Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. \nNo final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).')
num = cont = soma 0
#cont = 0
#soma = 0
while not num == 999:
    num = int(input('Digite um número inteiro: '))
    if num != 999:
        cont += 1
        soma += num
print('O total de números digitados foi {} e a soma deles é {}.'.format(cont, soma))