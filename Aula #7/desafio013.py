print('\033[1;4mDesafio 13 - Aumento de Salário\033[m')

print('Para saber o valor final do reajuste salarial, apresente os valores abaixo:')

nome = input('Digite o nome do funcionário: ')
salario = float(input('Digite o valor do salário do funcionário: R$ '))
aumento = 15
reajuste = (salario * aumento) / 100
final = salario + reajuste

print('O salário atual do funcionário \033[35m{}\033[m é o valor \033[36mR$ {:.2f}\033[m. O aumento será de R$ \033[36m{:.2f}\033[m. Portanto, o reajuste salarial final será no valor de \033[36mR$ {:.2f}\033[m.'.format(nome, salario, reajuste, final))

print('='*40)

print('Para saber o valor final do reajuste salarial, apresente os valores abaixo: ')

n = input('Digite o nome do funcionário: ')
s = float(input('Digite o valor do salário do funcionário: R$ '))
a = int(input('Digite a porcentagem de aumento sem o sinal de porcentagem: '))
r = (s * a) / 100
f = s + r
print('O salário atual do funcionário \033[35m{}\033[m é de \033[36mR$ {:.2f}\033[m. O aumento será de \033[36m{:.2f}\033[m. O reajuste salarial final será de \033[36mR$ {:.2f}\033[m.'.format(n, s, r, f))
