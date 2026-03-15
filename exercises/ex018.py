#faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosceno e tangente desse ângulo

import math
from ctypes.wintypes import tagMSG

angulo = float(input('Informe um ângulo qualquer: '))
angulo_rad = math.radians(angulo) #para fazer o calculo é encessário transformar em radianos

seno = math.sin(angulo_rad)
cos = math.cos(angulo_rad)
tang = math.tan(angulo_rad)

print('Seno: {:.2f}\n Cosseno: {:.2f}\n Tangente: {:.2f}'.format(seno,cos,tang))