# Exercicio 1
# Faça um programa que preencha uma matriz M (2x2), solicitando cada elemento (números inteiros) para o usuário. Depois, calcule e mostre uma matriz resultante da multiplicação dos elementos de M pelo seu maior elemento. Utilize %3d para imprimir a matriz.
M = []
maior = 0

for indice_linha in range(2):
    linha = []
    for indice_coluna in range(2):
        linha.append(int(input('Digite o elemento da linha {0} e coluna {1}: '.format(
            indice_linha, indice_coluna))))
    M.append(linha)

for linha in range(2):
  for coluna in range(2):
    if M[linha][coluna] > maior:
      maior = M[linha][coluna]

print('Matriz resultante:')
for linha in range(2):
  for coluna in range(2):
    M[linha][coluna] = maior * M[linha][coluna]
    print('%3d' % M[linha][coluna], end=' ')
  print()

# Exercicio 2
# Faça um programa que preencha:
# Uma lista com 3 nomes de lojas
# Uma outra lista com 5 nomes de produtos
# Uma matriz com os preços de todos os produtos em cada loja
# O programa deverá mostrar todas as listas: lojas, produtos e preços(Utilize % 3d para imprimir a matriz). Depois, deverá mostrar todas relações(nome do produto – nome da loja - preço) em que o preço não ultrapasse R$ 50, 00.
lojas = []
produtos = []
preco = []

for i in range(3):
  lojas.append(input('Digite o nome da loja: '))

for i in range(5):
  produtos.append(input('Digite o nome do produto: '))

for indice_linha in range(3):
  linha = []
  for indice_coluna in range(5):
    linha.append(
        int(input('Digite o preco do produto {0} na loja {1}: '.format(indice_coluna, indice_linha))))
  preco.append(linha)

print('\nLojas:')
for i in lojas:
  print(i)

print('\nProdutos:')
for i in produtos:
  print(i)

print('\nPreços:')
for linha in range(len(preco)):
  for coluna in range(len(preco[linha])):
    print('%3d' %preco[linha][coluna], end=' ')
  print()

print('\nPreços menores que R$ 50.00: ')
for linha in range(len(preco)):
  for coluna in range(len(preco[linha])):
    if preco[linha][coluna] < 50:
      print('Loja: {0}, produto {1} e preço {2}'.format(
          lojas[linha], produtos[coluna], preco[linha][coluna]))
  print()

# Exercicio 3
# Crie um programa que preencha uma matriz 20x10 (20 linhas e 10 colunas) com números inteiros aleatórios (entre 0 e 10) e some cada uma das linhas, armazenando o resultado das somas em um vetor (lista). A seguir, o programa deverá multiplicar cada elemento da matriz pela soma da linha correspondente e mostrar a matriz resultante.
from random import randint

M = []
somatoria = []

for i in range(20):
  linha = []
  for i in range(10):
    linha.append(randint(0,10))
  M.append(linha)

soma=0
print('Matriz original:')
for linha in range(len(M)):
  for coluna in range(len(M[linha])):
    print('%3d' %M[linha][coluna], end=' ')
    soma += M[linha][coluna]
  somatoria.append(soma)
  print()

print('\nVetor com a somatória de cada linha: ')
print(somatoria)

print('\nmatriz depois da multiplicação:')
for linha in range(len(M)):
  for coluna in range(len(M[linha])):
    M[linha][coluna] = M[linha][coluna] * somatoria[linha]
    print('%5d' % M[linha][coluna], end=' ')
  print()
  
# Exercicio 4
# Elabore um programa que preencha uma matriz 4x2 com números inteiros recebidos do usuário e mostre essa matriz. Calcule e mostre quantos elementos dessa matriz são maiores que 10 e, em seguida, mostre uma segunda matriz com 0 (zero) no lugar dos elementos maiores que 10. Utilize %3d para imprimir todas as matrizes.
M = []
maior = 0

for iLinha in range(4):
  linha = []
  for iColuna in range(2):
    linha.append(int(input('Digite o elemento da linha {0} e coluna {1}: '.format(iLinha, iColuna))))
  M.append(linha)

print('Matriz original:')
for linha in range(len(M)):
  for coluna in range(len(M[linha])):
    print('%3d' %M[linha][coluna], end=' ')
  print()

print()
for linha in range(len(M)):
  for coluna in range(len(M[linha])):
    if M[linha][coluna] > 10:
      maior += 1
      print('{0} é maior que 10!'.format(M[linha][coluna]))
print('No total, %d elementos são maiores que 10!' %maior)

print('\nMatriz sem os números maiores que 10:')
for linha in range(len(M)):
  for coluna in range(len(M[linha])):
    if M[linha][coluna] > 10:
      M[linha][coluna] = 0
    print('%3d' %M[linha][coluna], end=' ')
  print()
