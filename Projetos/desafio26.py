#recebendo a frase
frase = str(input('Digite uma frase \nFrase: ')).strip().lower()
print('A letra .a. apareceu {} x'.format(frase.count('a')), end=' ')
print('e a primeira vez que apareceu foi na posição {}'.format(frase.find('a')+1))
print('e a ultima vez que aparece é na posição {}'.format(frase.rfind('a')+1))



