n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print('Com as notas {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(n1, n2, media))
if media < 5:
    print('\033[7m REPROVADO \033[m')
elif media >= 5 and media < 7:
    print('\033[7m RECUPERAÇÃO \033[m')
elif media >= 7 and media <= 10:
    print('\033[7m APROVADO \033[m')
else:
    print('\033[1;31mResultado inválido, reveja os valores digitados')
