#crie um programa que leia o nome completo de uma pessoa e mostre:
# Nome com todas as letras maúsculas, nome com todas minusculas, quantias letras tem ao todo (sem considerar espaços) e quantas letras tem o primeiro nome

nome = input('Informe o seu nome completo: ')

print(nome.upper())
print(nome.lower())
print(len(nome.strip()))
print(len(nome.split()[0])) #vai dividir a frase em partes, nesse caso, de 0 até 3 - (0)Theo (1)Dutra (2)Tell