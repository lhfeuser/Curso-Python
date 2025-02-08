# Recebe números
n1 = int(input('Insira o Primeiro Número \nNúmero: '))
print('--'*15)
n2 = int(input('Insira o Segundo Número \nNúmero: '))
print('--'*15)
n3 = int(input('Insira o Terceiro Número \nNúmero: '))
print('--'*15)
# Condições
if n1 > n2 and n1 > n3:
    print('O maior Número é o {}'.format(n1))
if n2 > n1 and n2 > n3:
    print('O Maior Número é o {}'.format(n2))
else:
    print('O Maior Número é o Número {}'.format(n3))
