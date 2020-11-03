peso = float(input('Informe seu peso (Kg): '))
altura = float(input('Informe sua altura (m): '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Classificação: ABAIXO DO PESO')
elif imc >= 18.5 and imc < 25:
    print('Classificação: PESO IDEAL')
elif imc >= 25 and imc < 30:
    print('Classificação: SOBREPESO')
elif imc >= 30 and imc < 40:
    print('Classificação: OBESIDADE')
else:
    print('Classificação: OBESIDADE MÓRBIDA')
