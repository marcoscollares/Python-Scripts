print('Desafio 33 - Maior e menor valores')

print('Faça um programa que leia três números e mostre qual é o maior e qual é o menor.')

a = float(input('Digite o primeiro número: '))
b = float(input('Digite o segundo número: '))
c = float(input('Digite o terceiro número: '))
#Verificando quem é o maior
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
#Verificando quem é o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor digitado foi {}.'.format(menor))
print('O maior valor digitado foi {}.'.format(maior))


#if (n1 > n2 and n1 > n3):
 #   print('O número {} é o maior.'.format(n1))
#if (n2 > n1 and n2 > n3):
 #   print('O número {} é o maior.'.format(n2))
#if (n3 > n1 and n3 > n2):
 #   print('O número {} é o maior.'.format(n3))
#if (n3 < n1 and n3 < n2):
 #   print('O número {} é o menor.'.format(n3))
#if (n2 < n1 and n2 < n3):
 #   print('O número {} é o menor.'.format(n2))
#if (n1 < n2 and n1 < n3):
 #   print('O número {} é o menor.'.format(n1))''' MEU EXERCÍCIO

