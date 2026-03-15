#desenvolva um programa que pergunte a distância de uma viagem em km. calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até 200km e R$ 0,45 para vagens mais longas

distancia = float(input('Informe a distância em km: '))

if distancia <= 200:
    valor = distancia * 0.50
    print('O valor da sua viagem é de R$ {}'.format(valor))
else:
    valor = distancia * 0.45
    print('O valor da sua viagem é de R$ {}'.format(valor))