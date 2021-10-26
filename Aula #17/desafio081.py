print('Desafio 81 - Extraindo dados de uma lista')
print('''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.''')
print('')
lista = list()
cont = 0
num = 0
while True:
    lista.append(int(input('Digite um valor: ')))
    cont += 1
    if lista == 5:
        num += 1
    ask = input('Deseja continuar? [S/N] ')
    if ask in 'Ss':
        print('Muito bem...')
    if ask not in 'SsNn':
        print('Opção inválida. O programa será encerrado...')
        break
    if ask in 'Nn':
        break
print('')
lista.sort(reverse=True)
print(f'Um total de {cont} números foram digitados.')
print(f'A lista de valores em ordem de forma ordenada decrescente é {lista}.')
if 5 in lista:
    print(f'O número 5 está na lista e foi digitado {lista.count(5)} vez(es).')
else:
    print(f'O número 5 não está na lista.')