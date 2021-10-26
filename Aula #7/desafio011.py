print('\033[1;4mDesafio 11 - Pintando Parede\033[m')

print('\033[35mPara calcular a área da parede, introduza os valores abaixo:\033[m ')

alt = float(input('\033[34mDigite a altura:\033[m '))
larg = float(input('\033[34mDigite a largura:\033[m '))
area = alt * larg
tinta = area / 2

print('A área da parede é \033[36m{:.1f}m²\033[m. Pensando que cada litro de tinta pinta 2m², serão necessários \033[36m{:.1f}\033[m litros para pintar a parede toda.'.format(area, tinta))
