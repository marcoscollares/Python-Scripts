print('\033[1;4mDesafio 66 - Vários números com flag\033[m')
print('\033[1mCrie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. \nNo final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).\033[m')
from time import sleep
num = cont = soma = 0
while True:
    num = int(input('Digite um número inteiro: '))
    if num == 999:
        break
    soma += num
    cont += 1

print(f'O total de números digitados foi {cont} e a soma deles é {soma}.')
print('Encerrando',end='')
sleep(1)
print('.',end='')
sleep(1)
print('.',end='')
sleep(1)
print('.')
sleep(1)
print('Fim do programa.')
