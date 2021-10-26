print('\033[1;4mDesafio 37 - Conversor de Bases\033[m')
print('\033[1mEscreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual \nserá a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.\033[m')
num = int(input('Digite um número inteiro: '))
print('''Escolha entre as opções abaixo:
[1] converter para BINÁRIO
[2] convertar para OCTAL
[3] converter para HEXADECIMAL''')
opcao = int(input('Digite a sua opção: '))
if opcao == 1:
    print('O número {} em Binário é {}.'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('O número {} em Octal é {}.'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('O número {} em Hexadecimal é {}.'.format(num, hex(num)[2:]))
else:
    print('Opção inválida. Tente novamente.')
