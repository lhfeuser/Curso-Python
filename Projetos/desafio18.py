from math import radians,sin, cos, tan


# Receber o valor para determinar sin, cos e tan
angulo = float(input('Insisa o ângulo \nÂngulo: '))

# Converta para radianos
cnvt = radians(angulo)

# Obtendo os valores 
s = sin(cnvt)
c = cos(cnvt)
t = tan(cnvt)

# Imprimir os valores
print('O seno é de {:.2f}, o cosseno é de {:.2f} e a tangente é de {:.2f}'.format(s,c,t))



