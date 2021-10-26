print('\033[1;4mDesafio 49 - Tabuada v.2.0\033[m')
print('\033[1mRefaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.\033[m')
print(' ')
print('=-' * 10)
print('      TABUADA')
print('-=' * 10)
print(' ')
num = int(input('Digite um número: '))
print(' ')
for multiplicador in range(1, 11):
    tabuada = '| {}  * {:2} = {:2} |'.format(num, multiplicador, num*multiplicador)
    print(tabuada)

#Outro modo de fazer
#for m in range(1, 11):
#   result = num * m
#    tabuada = '| {}  * {:2} = {:2} |'.format(num, m, result)
#    print(tabuada)