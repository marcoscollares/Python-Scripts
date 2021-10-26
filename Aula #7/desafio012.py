print('\033[1;4mDesafio 12 - Preço com desconto\033[m')

print('Para saber o preço do produto com \033[35m5% de desconto\033[m, digite o valor abaixo:')

p = float(input('Digite o preço original do produto: R$ '))
d = p * 0.05
f = p - d
print('O preço original do produto é R$ \033[36m{:.2f}\033[m. O valor final com desconto de 5% aplicado é de R$ \033[36m{:.2f}\033[m.'.format(p, f))

print('\033[34m=\033[m'*40)

print('Para saber o valor do produto com desconto, digite os valores abaixo:')

prod = float(input('Digite o valor original do produto: R$ '))
desc = int(input('Digite o valor do desconto: '))
desc1 = prod * (desc/100)
final = prod - desc1
print('O valor original do produto é R$ \033[36m{:.2f}\033[m e o desconto aplicado é de \033[36m{}%\033[m. Portanto, o valor do produto com desconto será R$ \033[36m{:.2f}\033[m.'.format(prod, desc, final))