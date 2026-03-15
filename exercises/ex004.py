#faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações sobre ela

x = input('Digite qualquer coisa ai: ')

print ('O tipo primitivo é ', type(x))
print('Só tem espaços? ', x.isspace())
print('É número', x.isnumeric())
print('É letra? ', x.isalpha())
print('Está em maiusculo? ', x.isupper())
print('Está em minusculo? ', x.islower())