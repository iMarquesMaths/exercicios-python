from datetime import date
atual = date.today().year
nasc = int(input('Ano de Nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
if idade == 18:
    print('Voce completa 18 anos em {}. Aliste-se IMEDIATAMENTE!'.format(atual))
elif idade < 18:
    saldo = 18 - idade
    print('Voce ainda não tem 18 anos, ainda faltam {} ano(s) para se alistar.'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Voce ja passou dos 18 anos, deveria ter se alistado há {} ano(s) .'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))
