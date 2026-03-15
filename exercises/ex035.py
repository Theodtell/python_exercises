#desenvolva um programa que leia o comprimento de 3 retas e diga ao usuário se elas podem ou não formar um triângulo

print(20*'='+'Analisador de triângulos'+ 20*'=')
reta1 = int(input('Informe o primeiro lado: '))
reta2 = int(input('Informe o segundo lado: '))
reta3 = int(input('Informe o terceiro lado: '))

if reta1 < reta2 + reta3 and reta2 <reta1 + reta3 and reta3 < reta1 + reta2:
    print('Esse é um triangulo')
else:
    print('Não é um triangulo')  