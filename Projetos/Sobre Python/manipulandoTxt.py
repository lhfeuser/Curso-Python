# Manipulando Cadeia de Textos dentro do Python 

"""
Frase = 'Meu nome é Lucas'
Fatiamento de String == Pegar partes dela
[] = Lista
frase[2] = u (pega o caracter informado pelo valor dentro da lista)
frase[9:13] (pega os caracteres irfamados excluindo o último informado)
frase[9:21:2] (faz o mesmo que o anterior pelo o números de casas solicitada)
frase[:5] (omitindo onde começa, começa do começo. Indo até o informado para um antes)
frase[15:] (omitindo o fim, começa no informado e vai até o fim)
frase[9::3] (começa no nove, vai até o fim e pula com o valor informado)

Analisando a String

len(frase) (informa o comprimento da frase)
frase.count('o') (conta quantas vezes a letra solicitado aparece na str)
frase.find('deo') (Indica onde a sequencia de letras informadas COMEÇAM a aparecer)
frase.find('Android') (Procura dentro da string a frase indicada. Não encontrand retorna -1)
'Curso' in frase (Indica se tem a palavra na string. Retornando True or False)

Transformação
frase.replace('Python', 'Android') (Substitui o segundo pelo primeiro)
frase.upper() (Coloca a string em maiusculo)
frase.lower() (Coloca a string em minusculo)
frase.capitalize() (Coloca tudo para minusculo e deixa apenas o primeiro caracter em maiusculo)
frase.title() (Deixa todas a Primeiras Letras em maiusculo)
frase.strip() (Remove todos os espaços inúteis)
frase.rstrip() (Remove os espaços a direita)
frase.lstrip() (Remove os espaços a esquerda)

Divisão de String
frase.split() (Divide/Separa a frase em palavras pelos espaços, e gera uma nova lista)
frase

"""
