from random import randint #importando a biblioteca de escolha aleatoria
from time import sleep #importando a biblioteca de tempo
itens = ('Pedra', 'Papel', 'Tesoura') #defininfo os itens a serem escolhidos
computador = randint(0, 2) #computador escolhe de forma aleatoria uma opção
print('''SUAS OPÇÕES: 
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? ')) #Jogador escolhe sua opção de jogada

print('JO')
sleep(1)
print('KEN')             #Escreve JOKENPO com espera de 1 segundo a cada parte da palavra
sleep(1)
print('PO!!!')

print('-=' * 15) #separador
print('O computador escolheu {}'.format(itens[computador])) #item que o computador escolheu
print('O jogador escolheu {}'.format(itens[jogador])) #item que o jogador escolheu
print('-=' * 15) #separador

if computador == 0: #computador escolheu PEDRA
    if jogador == 0: #jogador escolheu PEDRA
        print('Resultado: EMPATE')
    elif jogador == 1: #jogador escolheu PAPEL
        print('Resultado: VOCE VENCEU')
    elif jogador == 2: #jogaodr escolheu tesoura
        print('Resultado: COMPUTADOR VENCEU')
    else:
        print('JOGADA INVÁLIDA')

elif computador == 1: #computador escolheu PAPEL
    if jogador == 0: #jogador escolheu PEDRA
        print('Resultado: COMPUTADOR VENCEU')
    elif jogaodr == 1: #jogador escolheu PAPEL
        print('Resultado: EMPATE')
    elif jogador == 2: #jogador escolheu TESOURA
        print('Resultado: VOCE VENCEU')
    else:
        print('JOGADA INVÁLIDA')

elif computador == 2: #computador escolheu TESOURA
    if jogador == 0: #jogador escolheu PEDRA
        print('Resultado: VOCE VENCEU')
    elif jogador == 1: #jogador escolheu PAPEL
        print('Resultado: COMPUTADOR VENCEU')
    elif jogador == 2: #jogador escolheu TESOURA
        print('Resultado: EMPATE')
    else:
        print('JOGADA INVÁLIDA')