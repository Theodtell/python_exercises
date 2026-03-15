#faça um programa que leia o salário de um funcionário e mostre o seu novo salário com um aumento de 15%

print('==CALCULADORA DE REAJUSTE SALARIAL==')

func = (input('Informe o nome do funcionário para o reajuste: '))
salario = float(input('Informe o salário atual: '))

salario_novo = (salario*0.15)+salario

print ('O salário atual de {} é R$ {} e passará para R$ {}'.format(func, salario, salario_novo))