#COPIAR NO CADERNO
print('Desafio 77 - Contando Vogais em Tuplas')
print('Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, \npara cada palavra, quais são as suas vogais.')

print('~'*40)
print(f'\033[1m{"Vowels Finder":^40}\033[m')
print('~'*40)

palavras = ('Carro', 'Aviao', 'Caminhao', 'Computador', 'Parede', 'Internet', 'Igreja', 'Amanha', 'Ontem', 'Hoje')
for p in palavras:
    print(f'\nNa palavra \033[1;35m{p}\033[m temos ',end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(f'\033[1;34m{letra}\033[m',end=' ')