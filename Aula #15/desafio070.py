print('Desafio 70 - Estatísticas em Produtos')
print('''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.''')
print('='*20)
print('REGISTRO DE PRODUTOS')
print('='*20)
total = preco = totmil = barato = menor = cont = 0
while True:
    nome = str(input('Nome do produto: ')).strip().upper()
    preco = float(input('Preço: R$ '))
    total += preco
    cont += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = nome
    if preco > 1000:
        totmil += 1
    ask = ' '
    while ask not in 'SsNn':
        ask = str(input('Deseja continuar? [S/N] '))
    if ask in 'Nn':
            break
print(f'''Total de gastos R$ {total:.2f}.
Nº de produtos acima de R$ 1000: {totmil}
O produto mais barato é {barato} e custa R$ {menor:.2f}''')

# EM CASOS DE TER QUE IDENTIFICAR/COMPARAR O MENOR E/OU MAIOR VALOR COM O WHILE LOOP, É NECESSÁRIO USAR UMA VARIANTE DE CONTAGEM!!!


'''if ask in 'Nn':
    break
if ask not in 'SsNn':
    print('Opção inválida. Programa encerrando')
    break'''
