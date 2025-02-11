from datetime import date
# pega o ano atual sozinho
ano = date.today().year
# recebe o ano de nascimento 
nasc = int(input('Em qual ano você nasceu? \nAno: '))
# condições
if (ano - nasc) == 18:
    print('Você precisa se alistar')
elif (ano - nasc) > 18:
    print('Já passou {} anos da hora de se alistar'.format((ano-nasc)-18))
else:
    print('Você não precisa de alistar, faltam {} anos ainda'.format((18 - (ano-nasc))))


