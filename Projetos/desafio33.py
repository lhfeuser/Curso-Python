# Recebe números
n1 = int(input('Insira o Primeiro Número \nNúmero: '))
print('--'*15)
n2 = int(input('Insira o Segundo Número \nNúmero: '))
print('--'*15)
n3 = int(input('Insira o Terceiro Número \nNúmero: '))
print('--'*15)
# Condições
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n2 and n3 > n2: 
    maior = n3
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n2 and n3 < n1:
    menor = n3
# print
print('O maior número é o {}'.format(maior))
print('O menor número é o {}'.format(menor))