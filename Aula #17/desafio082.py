print('Desafio 82 - Dividindo valores em várias listas')
print('Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão \nconter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.')
print('')
num = 0
lista = list()
pares = list()
ímpares = list()
contimp = 0
contpar = 0
while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    if num % 2 == 0:
        pares.append(num)
        contpar += 1
    if num % 2 == 1:
        ímpares.append(num)
        contimp += 1
    ask = input('Deseja continuar? [S/N] ')
    if ask in 'Ss':
        print('Muito bem.')
    if ask in 'Nn':
        print('Obrigado!')
        break
    if ask not in 'SsNn':
        print('Opção inválida. O programa será encerrado. Obrigado!')
        break
print('')
print(f'A lista criada foi {lista}.')
if contpar == 0:
    print('Não há números pares.')
else:
    print(f'A lista de pares é {pares}.')
if contimp == 0:
    print('Não há números ímpares.')
else:
    print(f'A lista de pares é {ímpares}')