# Recebe o nome da pessoa 
nome = str(input('Digite seu nome \nNome: '))
print('--'*24)
# Manipulações  
maisculo = nome.upper() # maiusculo
minusculo = nome.lower() # minusculo
remv = nome.split() # sepera o nome em lista
junta = ''.join(remv) # junta tudo junto em str dnv
conta = len(junta) # conta os caracter sem os espeços
# print's
print('Seu nome em maiúculo fica {}'.format(maisculo))
print('--'*24)
print('Seu nome em minúsculo fica {}'.format(minusculo))
print('--'*24)
print('Sem contar os espaços seu nome tem {} letras.'.format(conta))
print('--'*24)
print('Seu primeiro nome é {}'.format(remv[0]))
print('--'*24)
