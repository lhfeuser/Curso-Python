# Recebe o nome
n = str(input('Digite seu nome completo \nNome: ')).strip()
nome = n.split()
# Print
print('--'*15)
print('Muito prazer em te conhecer, {}!'.format(nome[0]))
print('--'*15)
print('Seu primeiro nome é: {}'.format(nome[0]))
print('--'*15)
print('Seu último nome é: {}'.format(nome[len(nome)-1]))
print('--'*15)