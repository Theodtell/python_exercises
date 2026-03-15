#Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada

print ('===TABUADA===')
n = int(input('Digite o número desejado: '))

print ('===Tabuada de {}==='.format(n))
for i in range (0 , 11):
    print ('{} X {} = {}'.format(i,n, n * i))
