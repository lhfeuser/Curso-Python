# Verifica se a frase é um Palíndromo
frase = str(input('Insira uma frase \nFrase: ')).lower()
print('=-'*20)
fse = frase.replace(' ','')
fsi = fse[::-1]
# condições
if fse == fsi:
    print('Parabéns!! Você tem um Palíndromo')
    print('=-'*20)

