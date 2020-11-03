count = soma = num = 0
num = int(input('Digite um número (999 para encerrar): '))
while num != 999:
    count += 1
    num = int(input('Digite um número (999 para encerrar): '))
print('Acabou')
print('Voce digitou {} numeros e a soma entre eles foi {}'.format(count, soma))
