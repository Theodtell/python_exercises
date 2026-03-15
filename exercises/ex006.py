#crie um programa que leia um número e mostre o seu dobro, o triplo e a raiz quadrada

n1= int(input('Digite um número: '))
print('O dobro de {} é {}'.format(n1,n1*2))
print('O triplo de {} é {}'.format(n1,n1*3))
print('A raiz quadrada de {} é {:.3f}'.format(n1, n1**(1/2)))
print('E a raiz cubica é {:.3f}'.format(n1**(1/3)))
