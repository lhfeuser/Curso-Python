from random import choice

# Recebe o nome dos alunos 
al1 = str(input('Qual o nome do primeiro aluno? \nAluno: '))
print('---'*14)
al2 = str(input('Qual o nome do segundo aluno? \nAluno: '))
print('---'*14)
al3 = str(input('Qual o nome do terceiro aluno? \nAluno: '))
print('---'*14)
al4 = str(input('Qual o nome do quarto aluno? \nAluno: '))
print('---'*14)

# Gera um Lista
lista = [al1,al2,al3,al4]

# Sortei o aluno
sort = choice(lista)

# Mostra quem ganhou 
print('O aluno {} irá apagar o quadro!'.format(sort))