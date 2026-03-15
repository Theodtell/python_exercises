#um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele lendo o nome deles e escrevendo o nome do escolhido

import random

aluno1 = input('Digite o nome do 1° aluno: ')
aluno2 = input('Digite o nome do 2° aluno: ')
aluno3 = input('Digite o nome do 3° aluno: ')
aluno4 = input('Digite o nome do 4° aluno: ')

escolhido = random.choice([aluno1, aluno2, aluno3, aluno4])

print('O aluno escolhido foi: \n ====={}===='.format(escolhido))