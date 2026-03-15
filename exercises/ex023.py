#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados. Ex: digite um número: 1834. Unidade 4 dezena 3 centena 8 milhar 1

numero = input('Informe um número de 0 a 9999: ')
unidade= numero[0]
dezena = numero[1]
centena = numero[2]
milhar = numero[3]


print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(unidade, dezena, centena, milhar))