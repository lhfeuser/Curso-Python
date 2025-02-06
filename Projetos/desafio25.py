# Recebe o Nome
nome = str(input('Qual seu nome completo? \nNome: ')).strip()
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))