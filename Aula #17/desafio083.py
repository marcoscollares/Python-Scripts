print('Desafio 83 - Validando Expressões Matemáticas')
print('Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar \nse a expressão passada está com os parênteses abertos e fechados na ordem correta.')

print('')
print('\033[1m=\033[m'*40)
print(f'\033[1;35m{"EXPRESSÕES MATEMÁTICAS":^40}\033[m')
print('\033[1m=\033[m'*40)
print('')
exp = str(input('Digite a expressão: '))
pilha = []
for simb in exp:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')

"""abre = 0
fecha = 0
exp = input('Digite uma expressão matemática: ')
abre = exp.count('(')
fecha = exp.count(')')
if abre == fecha:
    print(f'A expressão {exp} é uma expressão matemática válida.')
elif abre != fecha:
    print(f'A expressão {exp} não é uma expressão matemática válida.')"""
