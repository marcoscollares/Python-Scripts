print('\033[1;4mDesafio 10 - Conversão de Real para Dólar\033[m')

real = int(input('\033[35mDigite o valor em real:\033[m '))

dolar = float(real / 3.27)

print('O valor em dólar que você terá é \033[34m{:.2f}\033[m.'.format(dolar))