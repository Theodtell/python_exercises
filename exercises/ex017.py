#faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa

from math import pow

cateto1 = float(input('Informe o cateto adjacente: '))
cateto2 = float(input('Informe o cateto oposto: '))

hipotenusa = (pow(cateto1, 2) + pow(cateto2 , 2))

print('A hipotenusa do triângulo retângulo é {:.2f}'.format(hipotenusa))