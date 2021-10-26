n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
if m >= 6:
    print('A sua média foi {:.1f} e você foi aprovado! PARABÉNS!!!'.format(m))
else:
    print('A sua média foi {:.1f} e você foi reprovado. ESTUDE MAIS!'.format(m))