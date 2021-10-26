#Versão 1

print('\033[1;40mQual número você quer digitar?\033[m')

n1 = int(input('Digite o número aqui: '))

print('O número que você digitou foi \033[32m{}\033[m, o seu antecessor é \033[34m{}\033[m e o seu sucessor é \033[33m{}\033[m.'.format(n1, n1-1, n1+1))
print('\033[35m=\033[m'*100)
#Versão 2

print('\033[1;40mQual número você quer escolher?\033[m')

n2 = int(input('Digite aqui: '))
ant = n2 - 1
suc = n2 + 1

print('O número digitado foi \033[33m{}\033[m, o seu antecessor é \033[32m{}\033[m e o seu predecessor \033[34m{}\033[m.'.format(n2, ant, suc))
