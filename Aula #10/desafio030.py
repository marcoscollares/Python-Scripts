print('Desafio 30 - Par ou ímpar?')

print('Crie um programa que eia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.')

num = int(input('Digite um número: '))
resultado = num%2
if resultado == 0:
    print('O número {} é PAR!'.format(num))
else:
    print('O número {} é ÍMPAR!'.format(num))
