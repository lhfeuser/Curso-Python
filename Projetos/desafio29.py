# Solicita a velocidade do carro
vel = int(input('Qual Foi a Velocidade Obtida \nVelocidade: '))

# Condições
if (vel - 80) > 0:
    print('Você foi multado!!! Valor da sua multa é de: R${:.2f}'.format((vel - 80)*7))
else:
    print('Parabéns!!! Você Não Foi Multado')
    