print('\033[1;4mDesafio 42 - Analisando Triângulos 2.0\033[m')
print("""\033[1mRefaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes\033[m""")

lado1 = int(input('Digite o valor do primeiro lado: '))
lado2 = int(input('Digite o valor do segundo lado: '))
lado3 = int(input('Digite o valor do terceiro lado: '))
triangulo = ((lado1 + lado2) > lado3) and ((lado1 + lado3) > lado2) and ((lado2 + lado3) > lado1)

if ((lado1 + lado2) <= lado3) or ((lado1 + lado3) <= lado2) or ((lado2 + lado3) <= lado1):
    print('Os lados NÃO formam um triângulo!')
elif triangulo == (lado1 == lado2 == lado3):
    print('Os lados formam um TRIÂNGULO EQUILÁTERO!')
elif triangulo == (lado1 == lado2 or lado2 == lado3 or lado1 == lado3):
    print('Os lados formam um TRIÂNGULO ISÓSCELES!')
elif triangulo == (lado1 != lado2 != lado3 != lado1):
    print('Os lados formam um TRIÂNGULO ESCALENO!')
