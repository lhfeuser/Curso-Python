# cotação dolar 02\02\2025 = 5,85

cart = float(input('QuaL valor você deseja converter para dólar? \nValor: '))
cotacao = float(input('Qual a cotação de dolar? \nCotação: '))
convt = cart / cotacao

print('Você terá {:.2f} doláres'.format(convt))