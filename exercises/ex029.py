#escreva um programa que leia a velocidade de um carro, se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$ 7,00 para cada km acima do limite

velocidade = float(input('Informe a veolicidade do veículo: '))

if velocidade > 80:
    multa = (velocidade - 80) *7
    print('Você foi multado e deverá pagar R${}'.format(multa))
else:
    print('Velocidade permitida!')