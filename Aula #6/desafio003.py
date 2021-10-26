print('Qual a subtração que você quer realizar? ')
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
s = n1 - n2
cor = {'limpa':'\033[m',
       }
print('O resultado da subtração entre {}{}{} e {}{} é {}{}.'.format('\033[31m', n1, '\033[m', '\033[34m', n2, s, '\033[m'))
