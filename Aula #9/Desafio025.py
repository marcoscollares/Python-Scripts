print('Desafio 25 - Procurando uma string dentro de outra')

print('Crie um programa que leia o nome de uma pessoa e digae ela tem "SILVA" no nome.')

nomecompleto = str(input('Digite o teu nome completo: ')).strip()
print('Teu nome tem Silva? {}'.format('SILVA' in nomecompleto.upper()))

#silva = 'Silva' in nomecompleto
#print('O resultado se o teu nome completo contém o nome Silva é {}.'.format(silva))