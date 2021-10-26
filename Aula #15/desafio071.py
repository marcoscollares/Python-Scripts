print('Desafio 71 - Simulador de Caixa Eletrônico')
print('''Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o \nvalor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.''')

print('-='*20)
print('{:^40}'.format('CAIXA ELETRÔNICO - BANCO MHSC'))
print('=-'*20)
print('')
print('Olá, seja bem-vindo(a) ao nosso serviço de saque. Atualmente, o caixa eletrônico \ndispõe de cédulas de R$ 50, R$ 20, R$ 10, R$ 1.')
cont = 0
valor = int(input('Digite o valor a ser sacado: R$ '))
total = valor
ced = 50
while True:
    if total >= ced:
        total -= ced
        cont += 1
    else:
        if cont != 0:
            print(f'Total de {cont} cédulas de R$ {ced}.')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        cont = 0
        if total == 0:
            break
print('Volte sempre ao Banco MHSC. Até mais!')