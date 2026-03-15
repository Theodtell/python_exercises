# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua posição inteira. Ex: número 6.177 e o número tem a parte inteira 6

from math import trunc

n = float(input('Informe um número real: '))
n = trunc(n)
print(n)

