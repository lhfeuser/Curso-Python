from datetime import date
# Recebe o ano de nascimento
ano = int(input('Qual o ano de nascimento do atleta? \nAno: '))
# Calcula a idade
idade = date.today().year - ano
# Condições
if idade <= 9:
    print('Atleta da Categoria Mirim')
elif idade > 9 and idade <= 14:
    print('Atleta da Categoria Infantil')
elif idade > 14 and idade <= 19:
    print('Atleta da Categoria Junior')
elif idade == 20:
    print('Atleta da Categoria Sênior')
else:
    print('Atleta da Categoria Master')

#teste 
print(idade)