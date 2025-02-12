totidade = 0
nm = '' # Nome do Homem mais velho
hv = 0 # Homem mias velho idade
fv = 0

for p in range(1,5):
    print('----- {}ª Pessoa -----'.format(p))
    nome = str((input('Nome: '))).strip()
    idade = int((input('Idade: ')))
    sx = str(input('Sexo M|F: ')).upper().strip()
    totidade += idade
    if p == 1 and sx == 'M':
        hv = idade
        nm = nome
    if sx == 'M' and idade > hv:
        hv = idade
        nm = nome
    if sx == 'F' and idade < 20:
        fv += 1


media = totidade / 4
print('A média do grupo é de {}'.format(media))
print('O homem mais velho tem {} anos e seu nome é {}.'.format(hv,nm))
print('{} mulheres tem menos de 20 anos'.format(fv))
    



























