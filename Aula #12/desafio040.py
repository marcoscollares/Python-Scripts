print('Desafio 40 - Aquele clássico da Média')
print("""Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO""")
print('\033[1;35m~\033[m'*70)
print('\033[1m                            MÉDIA ESCOLAR\033[m')
print('\033[1;35m~\033[m'*70)

primeira = float(input('Digite a primeira nota: '))
segunda = float(input('Digite a segunda nota: '))
calculo = (primeira + segunda)/2

if calculo < 5.0:
    print('\033[31mO aluno está REPROVADO com a média de {:.1f}!\033[m'.format(calculo))
elif calculo >= 5.0 and calculo<= 6.9:
    print('\033[33mO aluno está em RECUPERAÇÃO com a média de {:.1f}!\033[m'.format(calculo))
else:
    print('\033[36mO aluno está APROVADO com a média de {:.1f}!\033[m'.format(calculo))