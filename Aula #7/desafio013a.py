print('Para saber o valor final do reajuste salarial, apresente os valores abaixo: ')

n = input('Digite o nome do funcionário: ')
s = float(input('Digite o valor do salário do funcionário: R$ '))
a = int(input('Digite a porcentagem de aumento sem o sinal de porcentagem: '))
r = (s * a) / 100
f = s - r
print('O salário atual do funcionário {} é de R$ {:.2f}. O aumento será de {:.2f}. O reajuste salarial final será de R$ {:.2f}'.format(n, s, r, f))
