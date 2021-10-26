print('\033[1;4mDesafio 7 - Média Aritmética\033[m')

nome = input('\033[34mNome do aluno:\033[m ')

print('\033[1;4mDigite abaixo as notas do aluno:\033[m')

port = int(input('\033[34mNota de Língua Portuguesa:\033[m '))
mat = int(input('\033[34mNota de Matemática:\033[m '))
media = (port+mat)/2

print('O aluno \033[34m{}\033[m tem a nota \033[33m{}\033[m em Língua Portuguesa, a nota \033[33m{}\033[m em Matemática e a média final das notas é \033[35m{}\033[m.'.format(nome, port, mat, media))
