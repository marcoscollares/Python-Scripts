print('Desafio 22 - Analisador de Textos')

print("""Crie um programa que leia o nome completo de uma pessoa e mostre: 
- O nome com todas as letras maiúsculas e minúsculas. 
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome.""")

nomecompleto = str(input('Digite o teu nome completo: ')).strip()
arrumado = nomecompleto.replace(" ","")
letrasaotodo = len(arrumado)
dividirnome = nomecompleto.split()
letrasnome = len(dividirnome[0])

print('O teu nome completa é {}. '.format(nomecompleto))
print('O teu nome em maíúsculo fica {}.'.format(nomecompleto.upper()))
print('O teu nome em minúsculo fica {}.'.format(nomecompleto.lower()))
#print('O teu nome completo tem {} letras ao todo.'.format(letrasaotodo))
print('O teu nome completo tem {} letras ao todo.'.format(len(nomecompleto) - nomecompleto.count(' ')))
#print('O teu primeiro nome tem {} letras ao todo.'.format(letrasnome))
print('O teu primeiro nome tem {} letras.'.format(nomecompleto.find(' ')))
