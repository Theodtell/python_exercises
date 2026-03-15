#escreva um programa que faça o computador pensar em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.

import random

print('***JOGO DA ADVINHAÇÃO***')

n = random.randint(1,5)

tentativa = input('Tente adivinhar o número: ')

if tentativa == n:
    print('PARABENS VOCÊ VENCEU!')
else:
    print('Não foi dessa vez ://')
