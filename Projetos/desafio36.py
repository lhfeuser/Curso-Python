# Recebe os dados
casa = float(input('Qual o Valor da Casa? \nValor: '))
sal = float(input('Qual é o seu salário? \nSalário: '))
temp = int(input('Em quanto meses você quer pagar? \nMeses: '))
# calculo do valor do financiamento 
fin = casa / temp

# condições
if fin > (sal * 0.30):
    print('FINANCIAMENTO NEGADO')
else:
    print('Financiamento Aprovado!!!')