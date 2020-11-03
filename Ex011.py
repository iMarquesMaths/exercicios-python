larg = float(input('Qual a largura da parede '))
alt = float(input('Qual a altura da parede '))
area = larg * alt
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(larg, alt, area))
tinta = area / 2
print('Para pintar esta parede voce precisara de {}L de tinta'.format(tinta))
