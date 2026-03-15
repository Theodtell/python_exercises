#o mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome de quatro alunos e mostre a ordem sorteada

import random

aluno1 = input('Digite o nome do 1° aluno: ')
aluno2 = input('Digite o nome do 2° aluno: ')
aluno3 = input('Digite o nome do 3° aluno: ')
aluno4 = input('Digite o nome do 4° aluno: ')

alunos = [aluno1, aluno2, aluno3, aluno4]

random.shuffle(alunos)

print ('A ordem de aprensetação será:')

for aluno in alunos:
    print(aluno)