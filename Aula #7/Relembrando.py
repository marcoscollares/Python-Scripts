#Exercício 1

print('Olá, mundo. Seja bem-vindo ao meu programa. ')
print('Abaixo, irei perguntar algumas informações sobre você:')

nome = input('Qual é o teu nome? ')
idade = input('Qual é a tua idade? ')
lugar = input('De onde você é? ')

print('Muito prazer em te conhecer, {} da idade de {} anos e morador de {}. '.format(nome, idade, lugar))

estudo = input('O que você estuda? ')
sonho = input('Qual profissão você almeja ter? ')

print('Você estuda {} e planeja ser {}. Meus parabéns. Espero que você chegue lá!'.format(estudo, sonho))

print('='*40)
#=========================================================

print('Quais cálculos você planeja realizar?')

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
s = n1 + n2
sub = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
p = n1 ** n2
mod = n1 % n2

print('O resultado da soma é {}, da subtração {}, da multiplicação {}, da divisão {}, da divisão inteira {}, da potenciação {} e do módulo {}.'.format(s, sub, m, d, di, p, mod))

