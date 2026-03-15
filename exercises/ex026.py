#Faça um programa que leia uma frase pelo teclado e mostre: quantas vezes aparece a letra "a"; em que posição ela aparece a primeira vez; em que posição ela aparece a ultima vez

frase = input('Digite uma frase: ')

frase_lower = frase.lower()

print (frase_lower.count('a'))
print (frase_lower.find('a'))
print(frase_lower.rfind('a'))
