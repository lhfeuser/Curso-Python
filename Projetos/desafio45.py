from random import choice
# sorteio máquina
sort = choice(['Pedra','Papel','Tesoura'])
# Escolha jogador
escolha = str(input('Escolha entre: Pedra, Papel ou Tesoura \nEscolha: ')).strip().capitalize()
print('=-'*15)
# Condições
if escolha == sort:
    print('Deu Empate! Tente Novamente!')
elif escolha == 'Tesoura' and sort == 'Papel' or escolha == 'Papel' and sort == 'Pedra' or escolha == 'Pedra' and sort == 'Tesoura':
    print('Parabéns!! Você Ganhou!!')
else:
    print('Você Perdeu! Tente Novamente.')
print('=-'*15)
