print('-' * 30 )
print('ANALISADOR DE TRIANGULO')
print('-' * 30 )
r1 = float(input('Primeiro Segmento: '))
r2 = float(input('Segundo Segmento: '))
r3 = float(input('Terceiro Segmneto: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM formar um triangulo!', end=' ')
    if r1 == r2 == r3:
        print('Tipo: EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:
        print('Tipo: ESCALENO!')
    else:
        print('Tipo ISÓSCELES!')
else:
    print('Os segmentos acima NÃO PODEM formar um triangulo.')
    