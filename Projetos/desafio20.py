from random import shuffle
# Recebe os nome 

al1 = input('Insira o nome do primeiro aluno \nAluno: ')
print('---'*14)
al2 = input('Insira o nome do segundo aluno \nAluno: ')
print('---'*14)
al3 = input('Insira o nome do terceiro aluno \nAluno: ')
print('---'*14)
al4  = input('Insira o nome do quarto aluno \nAluno: ')
print('---'*14)

# Cria a lista
lista = [al1,al2,al3,al4]

# Ordem de apresentação
shuffle(lista)

# mostra a ordem
print('A ordem dos alunos será: ')
print(lista)
