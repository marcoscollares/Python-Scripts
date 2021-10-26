print('\033[1;4mDesafio 57 - Validação de Dados\033[m')
print('\033[1mFaça um programa que leia o sexo de uma pessoa, mas só aceite os valores M ou F. Caso esteja errado, peça a digitação novamente até ter um valor correto.\033[m')

sexo = str(input('Digite o seu sexo [M/F]: ')).upper().strip()[0]
while sexo not in 'MmFf':
    sexo = str(input('Opção Inválida! Digite o seu sexo [M/F]: ')).upper().strip()
print('O sexo digitado foi {}.'.format(sexo))