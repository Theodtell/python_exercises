# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar. Considere Us$ 1,0 = R$ 3,27

print('==Calculando R$ em US$')
print('O valor será calculado usando a referência de: US$ 1,0 = R$ 3,27')

n = float(input('Digite aqui o valor em R$ '))

print ('O valor R$ {} equivale a US$ {:.2f}'.format(n,n/3.27))