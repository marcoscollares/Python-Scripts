print('Desafio 23 - Separando dígitos de um número')

print('Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.')

num = int(input('Digite um numero: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Analisando o numero {}...'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))

#num = str(input('Digite um número: '))
#print('O número digitado fica dividido em ')
#print('{} milhar(es) '.format(num[-4]))
#print('{} centena(s)'.format(num[-3]))
#print('{} dezena(s)'.format(num[-2]))
#print('{} unidade(s)'.format(num[-1]))
