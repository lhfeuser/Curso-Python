from datetime import date
maior = 0
menor = 0
# Calcula quantas pessoas alcançaram a maior idade
for maiori in range(1,8):
    ano = int(input('Insira o ano de nascimento \nAno: '))
    if date.today().year - ano > 18:
        maior += 1
    else:
        menor += 1
print('Há {} pessoas de maior e {} de menor'.format(maior, menor))