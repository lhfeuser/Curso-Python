from random import randint
sort = randint(0,10)
jog = 0
cont = 0
print('=-'*7,'Jogo da Advinhação','-='*7)
while sort != jog:
    sort = randint(0,10)
    jog = int(input('Tente Adivinhar o Número (1/10) \nNúmero: '))
    print('=-'*20)
    if jog != sort or jog == sort:
        cont += 1
print('Você jogou {} vezes para acertar o número'.format(cont))
