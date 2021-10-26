print('Desafio 006')

print('\033[34mQual número você quer inserir?\033[m')

n1 = int(input('Digite o número aqui: '))

dobro = n1*2
triplo = n1*3
raiz = n1*(1/2)

print('O número digitado foi \033[1;35m{}\033[m, o seu dobro é \033[1;31m{}\033[m, o triplo \033[1;33m{}\033[m e a raiz \033[1;34m{}\033[m.'.format(n1, dobro, triplo, raiz))