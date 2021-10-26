print('\033[1;4mDesafio 43 - Índice de Massa Corporal\033[m')
print("""Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida""")

peso = float(input('Digite o teu peso em Kg: '))
altura = float(input('Digite a tua altura em metros: '))
imc = peso / (altura**2)

if imc < 18.5:
    print('Atenção! O teu IMC é de {:.1f}. Você está Abaixo do Peso Ideal!'.format(imc))
elif 18.5 <= imc < 25:
    print('Parabéns! O teu IMC é de {:.1f}. Você está no Peso Ideal!!!'.format(imc))
elif imc >= 25 and imc < 30:
    print('Atenção! O teu IMC é de {:.1f}. Você está com Sobrepeso!'.format(imc))
elif imc >= 30 and imc < 40:
    print('Cuidado! O teu IMC é de {:.1f}. Você está com Obesidade!'.format(imc))
else:
    print('ALERTA! O teu IMC é de {:.1f}. Você tem Obesidade Mórbida!'.format(imc))

