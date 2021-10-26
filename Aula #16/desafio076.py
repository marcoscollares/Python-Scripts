print('\033[1;4mDesafio 76 - Lista de Preços em Tuplas\033[m')
print('')
print('\033[1mCrie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. \nNo final, mostre uma listagem de preços, organizando os dados em forma tabular.\033[m')
print('')
print('\033[1m-\033[m'*51)
print(f'\033[1;33m{"LISTA DE PREÇOS":^50}\033[m')
print('\033[1m-\033[m'*51)
cont = 0
#tupla = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
tupla = ('Lápis', 'Borracha', 'Caderno', 'Estojo', 'Transferidor', 'Compasso', 'Mochila', 'Canetas', 'Livro',
         1.75, 2.00, 15.90, 25.00, 4.20, 9.99, 120.32, 22.30, 34.90)
for lista in tupla:
    print(f' {tupla[cont]:.<12}............................R$ {tupla[cont+9]:>6.2f}')
    cont += 1
    if cont == 9:
        break
print('-'*51)

#for pos in range (0, len(tupla)):
    #if pos % 2 ==:
        #print(f'{tupla[pos]}')


