salario = float(input('Qual é o salário atual do funcionario? R$'))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('O funcionario que ganhava {:.2f}, passa a ganhar {:.2f}'.format(salario, novo))
