#escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salário superiores a R$ 1.250,00 = 10% para inferiores 15%

func = input('Informe o nome do funcionário: ')
salario = float(input('Informe o salário: '))

if salario > 1250:
    salario_novo = salario + (salario * 0.10)
    print('O salário de {} passará de R$ {} para R$ {}'.format(func, salario, salario_novo))
else:
    salario_novo = salario + (salario * 0.15)
    print('O salário de {} passará de R$ {} para R$ {}'.format(func, salario, salario_novo))
