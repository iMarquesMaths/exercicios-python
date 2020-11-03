from random import randint
from time import sleep
computador = randint(0, 5) #Faz o computador "pensar" um número
print('-=-' * 20)
print('Vou pensar em um número de 0 a 5. Tente adivinhar... haha')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? ')) #jogador tanta adivinhar
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('Parabens, você conseguiu me vencer!')
else:
    print('GANHEI, haha! Você pensou no número {}, e não no número {}'.format(jogador, computador))
print('-=-' * 20)
print('Fim da brincadeira!')
