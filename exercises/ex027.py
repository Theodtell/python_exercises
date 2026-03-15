#faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente. Exemplo: Ana Maria de Souza = primeiro ana ultimo Souza

nome = str(input('Digite seu nome completo: ')).strip()

primeiro_nome = nome.split()[0]
segundo_nome = nome.split()[-1] #acessa de trás para frente

print('Primeiro nome: {}\nSegundo nome: {}'. format(primeiro_nome, segundo_nome))