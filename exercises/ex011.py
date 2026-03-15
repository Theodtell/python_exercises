#faça um programa que leia a largura e a altura de uma parede em metros, calcule a área e a quantidade de tinta necessária para pinta-la sabendo que cada litro de tinta pinta uma área de 2m²

print ('Calculadora de tinta')

largura = float(input('Informe a largura da sua parede: '))
altura = float(input('Informe agora a altura da sua parede: '))

area = largura * altura
tinta = area / 2

print ('A área total é de {} m² e o total de tinta necessário é de: {} litros'.format(area, tinta))