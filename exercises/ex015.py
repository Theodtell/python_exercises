#Calcule o valor de um aluguel de carro de acordo com os Km rodados o carro custa R$ 60,00 por dia e R$ 0,15 por km

print('==CALCULADORA PARA ALUGUEL DE UM CARRO==')

dias = int(input('Informe os dias alugados: '))
km = float(input('Informe a quantidade de km rodados: '))

valor_final = (dias *60) +(km*0.15)

print('O valor a pagar é de: R$ {}'.format(valor_final))