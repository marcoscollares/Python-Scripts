z = input('\033[1;40mDigite algo 1:\033[m ')
print('\033[34m O tipo primitivo é \033[m', type(z))
print('\033[33m É alfabético? \033[m', z.isalpha())

y = input('\033[1;40mDigite algo 2:\033[m '))
print('\033[34m O tipo primitivo é \033[m', type(y))
print('\033[33m É numérico? \033[m', y.isnumeric(), '\033[m')

x = int(input('\033[1;40mDigite algo 3:\033[m '))
print('\033[34mO tipo primitivo é\033[m ', type(x))

w = float(input('\033[1;40mDigite algo 4:\033[m '))
print('\033[34mO tipo primitivo é\033[m ', type(w))

v = input('\033[1;40mDigite algo 5:\033[m ')
print('\033[34mO tipo primitivo é\033[m ', type(v))
print('\033[33mÉ alfanumérico?\033[m ', v.isalnum())

u = input('\033[1;40mDigite algo 6:\033[m ')
print('\033[34mO tipo primitivo é\033[m ', type(u))
print('\033[33mÉ tudo em maiúsculo?\033[m ', u.isupper())

t = input('\033[1;40mDigite algo 7:\033[m ')
print('\033[34mO tipo primitivo é\033[m ', type(t))
print('\033[33mÉ tudo em minúsculo?\033[m ', t.islower())

