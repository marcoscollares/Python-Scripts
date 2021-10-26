print('Desafio 79 - Valores únicos em uma lista')
print('Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. \nCaso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, \nem ordem crescente. ')

numeros = list()
ask = 0
while True:
    num = int(input('Digite um número: '))
    if num not in numeros:
        numeros.append(num)
        print('Valor adicionado!')
    else:
        print('O valor já foi adicionado antes. Não irei adicionar!')
    ask = str(input('Deseja continuar? (S/N) '))
    if ask in 'Ss':
        print('...')
    elif ask in 'Nn':
        break
numeros.sort()
print(numeros)