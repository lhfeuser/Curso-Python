# Recebe as notas
n1 = float(input('Insira a primeira nota \nNota: '))
n2 = float(input('Insira a segunda nota \nNota: '))
# Condições
if (n1 + n2) / 2 >= 7:
    print('Parabéns, Você Foi Aprovado!!!!')
elif (n1 + n2) / 2 <= 6.9 and (n1 + n2) / 2 >= 5.0:
    print('Você ficou de exame!')
else:
    print('Você reprovou!')