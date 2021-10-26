print('\033[1;4mDesafio 38 -  Comparando Números\033[m')
print("""mEscreva um programa que leia dois números inteiros e compare-os mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais""")
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if n1 > n2:
    print('\033[36mO primeiro número é maior.\033[m')
elif n2 == n1:
    print('\033[35mNão existe valor maior, os dois são iguais.\033[m')
else:
    print('\033[31mO segundo número é maior.\033[m')


