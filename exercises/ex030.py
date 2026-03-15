#crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR

numero = int(input('Informe um número inteiro: '))

if numero % 2 == 0:
    print ('Esse número é par')
else:
    print('Esse número é impar')