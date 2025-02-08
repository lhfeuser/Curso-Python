from datetime import date
# Recebe o ano
ano = int(input('Insira o ano para saber se é Bissexto \nAno: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano é Bissexto')
else:
    print('O ano não é Bissexto')