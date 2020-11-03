dias = int(input('Quantos dias rodados? '))
km = float(input('Quantos Km rodados? '))
pago = (dias * 60) + (km * 0.15)
print('O valor total a ser pago é de {}'.format(pago))
