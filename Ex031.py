distancia = float(input('Qual a distancia da sua viagem? '))
print('Voce esta prestes a começar uma viagem de {}km'.format(distancia))
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print('E o preço da sua passagem sera de R${}'.format(preço))
