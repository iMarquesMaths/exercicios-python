preco = (float(input('Qual é o valor do produto? R$')))
novo = preco - (preco * 5 / 100)
print('O produto que custava R${:.2f}, na promoção com 5% de desconto vai custar R${:.2f}'.format(preco, novo))
