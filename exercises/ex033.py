#faça um programa que leia três números e mostre qual é o maior e qual é o menor

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Quase lá! Digite o segundo número: '))
n3 = int(input('Digite só mais um número: '))

if n1 > n2 and n1 > n3:
    print('O maior número é {}'.format(n1))
elif n2 > n1 and n2 > n3:
    print('O maior é o {}'.format(n2))
else:
    print ('O maior é o {}'.format(n3))