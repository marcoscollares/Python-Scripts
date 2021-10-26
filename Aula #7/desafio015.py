print('\033[1;4mDesafio 15 - Aluguel de carro\033[m')

print('Para saber o valor a ser pago pelo carro alugado, digite os valores abaixo:')

km = float(input('Digite a quantidade de quilômetros percorridos: '))
d = int(input('Digite a quantidade de dias de aluguel: '))
vf = (km * 0.15) + (d * 60)

print(('O valor final a ser pago pelo carro alugado será de R$ \033[34m{:.2f}\033[m.').format(vf))