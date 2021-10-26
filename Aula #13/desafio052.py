print('\033[1;4mDesafio 52 - Números Primos\033[m')
print('\033[1mFaça um programa que leia um número inteiro e diga se ele é ou não um número primo.\033[m')

num = int(input('Digite um número inteiro: '))
tot = 0
for primo in range(1, num+1):
    if num % primo == 0:
        print('\033[1;36m',end=' ')
        tot += 1
    else:
        print('\033[m\033[31m',end=' ')
    print('{}'.format(primo),end=' ')
print('\n\033[mO número {} é divisível {} vezes.'.format(num, tot))
if tot == 2:
    print('Portanto, ele é um \033[1;36mNÚMERO PRIMO!\033[m')
else:
    print('Portanto, ele \033[1;36mNÃO\033[m é um \033[1;36mNÚMERO PRIMO!\033[m')

