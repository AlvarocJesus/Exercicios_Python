from random import *
# Exercicio 1
""" inteiros = []
reais = []
complexos = []
strings = []

for i in range(10):
    inteiros.append(randint(1, 10))
    i += 1
for r in range(15):
    reais.append(uniform(1, 15))
    r += 1
for c in range(7):
    complexos.append(complex(randint(1, 7)))
    c += 1
for s in range(5):
    strings.append(input('Digite uma string: '))
    s += 1

# completo = []
# completo.append(inteiros)
# completo.append(reais)
# completo.append(complexos)
# completo.append(strings)

completo = [inteiros, reais, complexos, strings]
inteiros = []
reais = []
complexos = []
strings = []
for i in range(50):
  completo[0].append(randint(1,50))
print(completo) """

# Exercicio 2
# Faça um programa que cria uma matriz m 10 x 15, sendo que cada elemento é um inteiro gerado aleatoriamente. Então, exiba a matriz completa e, na sequência, somente os elementos da primeira coluna da matriz.
""" M = []

for iLinha in range(10):
  linha = []
  for coluna in range(15):
    linha.append(randint(0, 100))
  M.append(linha)
  
for linha in range(len(M)):
  for coluna in range(len(M[linha])):
    print('{0:4d}'.format(M[linha][coluna]), end=' ')
  print()
for linha in range(10):
  print(M[linha][0], end=' ') """

# Exercicio 3
# Solicitar dados de uma matriz 4x4 e montar um vetor de 4 elementos com a soma dos elementos ímpares de cada linha
""" M = []
soma = []

for indice_linha in range(4):
    linhas = []
    for indice_col in range(4):
        linhas.append(int(input('Digite um numero: ')))
    M.append(linhas)

print(M)
for lin in range(len(M)):
  impar = 0
  for col in range(len(M[lin])):
    if M[lin][col] % 2 != 0:
      impar += M[lin][col]
  soma.append(impar)

print(soma) """

# Exercicio 4
# aça um programa para receber uma matriz 3×3 (solicitar ao usuário) e apresentar a soma dos elementos da diagonal principal e a matriz na forma como deve ser vista: com linhas e colunas
""" M = []
soma = 0

for indice_linha in range(3):
  linha = []
  for indice_coluna in range(3):
    linha.append(int(input()))
  M.append(linha)
  
for linha in range(len(M)):
  for coluna in range(len(M[linha])):
    print('%4d' %M[linha][coluna], end=' ')
    if linha == coluna:
      soma += M[linha][coluna]
  print()
print(soma) """

# Exercicio 5
# Faça um programa que cria uma matriz A 10x5 com números inteiros aleatórios e, então, exiba a matriz transposta de  (At).
# Determinar a transposta de uma matriz é reescrevê-la de forma que suas linhas e colunas troquem de posições ordenadamente, isto é, a primeira linha é reescrita como a primeira coluna, a segunda linha é reescrita como a segunda coluna e assim por diante, até que se termine de reescrever todas as linhas na forma de coluna.
""" M = []
mT = []

for indice_linha in range(10):
  linha = []
  for indice_coluna in range(5):
    linha.append(randint(1, 100))
  M.append(linha)
# print(M)
for linha in range(10):
  for coluna in range(5):
    print('%4d' % M[linha][coluna], end=' ')
  print()

print()
print()

for coluna in range(5):
  for linha in range(10):
    print('%4d' %M[linha][coluna], end=' ')
  print() """

# Jeito 1
# print([*zip(*M)])

# Exercicio 6
# Crie uma matriz m[12][12] com números inteiros aleatórios. Em seguida, calcule e mostre a soma ou a média considerando somente aqueles elementos que estão abaixo da diagonal principal da matriz, conforme ilustrado abaixo(área verde).
m = []
operacao = input('Digite S para soma ou M para media: ')

for indice_linha in range(12):
  linha = []
  for indice_coluna in range(12):
    linha.append(indice_linha + indice_coluna)
  m.append(linha)

soma = 0
media = 0
if operacao == 'S':
  for linha in range(len(m)):
    for coluna in range(len(m[linha])):
      if linha != coluna:
        soma += m[linha][coluna]
        print('linha:', linha, 'coluna: ', coluna, 'teste: ', coluna-linha)
    print()
elif operacao == 'M':
  for linha in range(len(m)):
    for coluna in range(len(m[linha])):
      print('%4d' % m[linha][coluna], end=' ')
      if linha == coluna:
        soma += m[linha][coluna]
    print()
  print()
  media = soma/len(m)
print(soma)
