print('Desafio 26 - Primeira e última ocorrência de uma string')

print("""Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece 
a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.""")
frase = str(input('Digite uma frase: ')).upper().strip()
num = frase.count('A')
começa = frase.find('A')+1
termina = frase.rfind('A')+1

print('A string "a" apareceu {} vezes na frase digitada.'.format(num))
print('A primeira letra começa na posição {} da string.'.format(começa))
print('A ultima letra aparece na posição {}.'.format(termina))