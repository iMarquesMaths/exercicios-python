from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos valores
    [ 5 ] Encerrar programa''')
    opção = int(input('Qual é a sua opção: '))
    if opção == 1:
        soma = n1 + n2
        print('A soma entre os números {} e {} resulta em {}!'.format(n1, n2, soma))
    elif opção == 2:
        mult = n1 * n2
        print('A multiplicação entre os números {} e {} resulta em {}'.format(n1, n2, mult))
    elif opção == 3:
        if n1 > n2:
            print('O maior valor é {}'.format(n1))
        elif n2 > n1:
            print('O maior valor é {}'.format(n2))
        elif n1 == n2:
            print('Os valores {} e {} são IGUAIS'.format(n1, n2))
    elif opção == 4:
        print('Digite os novos valores')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção inválida, tente novamente.')
    print('=-=' * 10)
    sleep(1)
print('Fim do Programa!')