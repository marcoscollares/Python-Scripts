print('Desafio 24 - Verificando as primeiras letras de um texto')

print('Crie um programa que leia o nome de uma cidade e diga se ele começa ou não o nome "SANTO".')

cidade = str(input('Digite o nome da cidade em que você mora: ')).strip()
print(cidade[:5].upper() == 'SANTO')

#dividido = cidade.split()
#resposta = 'SANTO' in dividido[0].upper()
#print('O resultado se a cidade digitada tem o nome Santo no começo é {}.'.format(resposta))