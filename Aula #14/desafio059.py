#COPIAR NO CADERNO
print('\033[1;4mDesafio 59 - Criando um Menu de Opções\033[m')
print("""\033[1mCrie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.\033[m""")

print('=-'*20)
print('            Menu Matemático')
print('-='*20)

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
menu = 0
maior = 0
while menu != 5:
    print('''=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
            Menu Matemático
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa''')
    menu = int(input('Digite uma das opções: '))
    if menu == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}.'.format(n1, n2, soma))
    elif menu == 2:
        mult = n1 * n2
        print('A multiplicação entre {} e {} é {}.'.format(n1, n2, mult))
    elif menu == 3:
        if n1 > n2:
            print('O maior número é {}.'.format(n1))
        elif n1 == n2:
            print('Não há valor maior. Os dois números são iguais!')
        elif n2 > n1:
            print('O maior número é {}.'.format(n2))
    elif menu == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif menu == 5:
        print('Até mais!')
        break
    else:
        print('Opção inválida. Tente novamente!')
print('...')
