print('\033[1;4mAula 17 - Listas (Parte 1)\033[m')
print('\033[1mNessa aula, vamos aprender o que são LISTAS e como utilizar listas em Python. \nAs listas são variáveis compostas que permitem armazenar vários valores \nem uma mesma estrutura, acessíveis por chaves individuais.\033[m')
print('')
'''num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)
if 5 in num:
    num.remove(5)
else:
    print('Não achei o número 5.')
print(num)
print(f'Esta lista tem {len(num)} elementos.')'''

#-----------------------------------------

'''valores = list()
valores.append(5)
valores.append(9)
valores.append(4)

for v in valores:
    print(f'{v}...')

for c, v in enumerate(valores):
    print(f'Na posição {c+1} encontrei o valor {v}.')
print('Cheguei ao final da lista.')'''

#--------------------------------

valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
print('')
for c, v in enumerate(valores):
    print(f'Na posição {c+1} encontrei o valor {v}.')
print('')
print('Cheguei ao final da lista.')

#--------------------------------

'''a = [2, 3, 4, 7]
#b = a
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')'''