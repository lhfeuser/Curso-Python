# Recebe os valores
v1 = int(input('Insira um valor \nValor: '))
v2 = int(input('Insira outro valor \nValor: '))
# Condições 
if v1 > v2:
    print('O primeiro valor é maior')
elif v2 > v1:
    print('O segundo valor é maior')
else:
    print('Não há valor menor ou maior')
