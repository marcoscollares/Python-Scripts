print('\033[1;4mDesafio 14 - Conversor de temperaturas (Cº para Fº)\033[m')

print('Para fazer a conversão de temperatura em Celsius para Fahrenheits, digite o valor abaixo:')

c = int(input('Digite a temperatura em Celsius: '))
f = c * 1.8 + 32
t = int(f)

print('A temperatura em Celsius é de \033[33m{}ºC\033[m. Após a conversão, a temperatura em Fahrenheits é de \033[31m{}ºF\033[m.'.format(c, t))

