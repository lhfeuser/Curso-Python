"""
if primeiro bloco
elif segundo bloco pode usar qntos quiser dentro do if, mas não pode usar sem o if
else terceiro bloco
"""

nome = str(input('Insira seu nome \nNome: '))

if nome == 'Lucas':
    print('Que nome bonito você tem!!!')
elif nome == 'Eduarda' or nome == 'Ana' or nome == 'Rafaela':
    print('Seu nome é bem popular')
elif nome in 'Beatriz Daniela Rafael':
    print('Seu nome é estranho')
else:
    print('Seu nome é normal!!!')
print('Tenha um bom dia, {}!!!'.format(nome))