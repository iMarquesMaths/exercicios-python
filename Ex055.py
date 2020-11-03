pesomaior = 0
pesomenor = 0
for pess in range(1,6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(pess)))
    if pess == 1:
        pesoamior = peso
        pesomenor = peso
    else:
        if peso > pesomaior:
            pesomaior = peso
        if peso < pesomenor:
            pesomenor = peso
print('O maior peso lido foi de {}Kg.'.format(pesomaior))
print('O menor peso lido foi de {}Kg.'.format(pesomenor))
