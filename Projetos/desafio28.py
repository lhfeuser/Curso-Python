from random import randint

# Computador sorteia número (0-5)
sort = randint(0,5)
### print(sort)  #teste

# Usuário escolhe um número
jog = int(input('Tente acertar o número sorteado \nNúmero: '))
print('--'*20)
# Condições
if jog == sort:
    print('Parabéns, Você Ganhou!!')
    print('--'*20)
else:
    print('Você Perdeu!')
    print('--'*20)

print('--'*20)
print('Jogue Novamente!')
