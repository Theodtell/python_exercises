#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média

aluno = input('Informe o nome do aluno: ')
n1 = float(input('Digite aqui a primeira nota: '))
n2 = float(input('Digite aqui a segunda nota: '))

media = (n1 + n2) / 2

print("A média de notas do aluno {} é de: {:.2f}".format (aluno, media))