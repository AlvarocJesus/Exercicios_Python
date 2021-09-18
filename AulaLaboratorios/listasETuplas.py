# Exercicio 1
# Faça um programa que leia, um a um, modelos de cinco carros(exemplos: FUSCA, GOL, VECTRA etc) e os guarde em uma mesma lista. Leia(um a um) uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses carros faz com um litro de combustível. Calcule e mostre:
# - O modelo do carro mais econômico
# - Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000 quilômetros.
carros = []
consumo = []
mais = ''
results = ''
carro = ''
con = ''

while len(carros) < 5:
  carros.append(input(''))
  consumo.append(int(input('')))

for i in range(len(carros)):
  results += '{}\n'.format(round(1000/consumo[i]))
  carro += '{}\n'.format(carros[i])
  con += '{}\n'.format(consumo[i])
  
  if consumo[i] == max(consumo):
    mais = carros[i]

print(carro)
print(con)
print(mais)
print(results)

# Exercicio 2
# Crie um programa que leia números inteiros do usuário até que o número 0 seja inserido. Uma vez que todos os números inteiros tenham sido lidos, seu programa deve exibir todos os números negativos, seguidos por todos os números positivos. Dentro de cada grupo, os números devem ser exibidos na mesma ordem em que foram inseridos pelo usuário
numero = []
pos = []
neg = []

while True:
  num = int(input(''))
  if num == 0:
    break
  elif num > 0:
    pos.append(num)
  elif num < 0:
    neg.append(num)

for i in neg:
  numero.append(i)
for i in pos:
  numero.append(i)

  
print(numero)

# Exercicio 3
# O desvio padrão populacional é uma medida de dispersão em torno da média populacional de uma variável aleatória.
# O calculo do desvio padrão populacional pode ser calculado pela equação abaixo:
# Onde: x é a lista com os valores das amostras, μ é a média dos elementos de x e N é a quantidade de amostras.
# A média pode ser calculada pela equação abaixo:
# Faça um programa que calcule a média e o desvio padrão de um vetor com os valores e o número de elementos definido pelo usuário.
from math import *
x = []
soma = 0
dpi = 0
N = int(input('Qual o tamanho da lista: '))

print('Digite os valores:')
for i in range(N):
  x.append(float(input('')))

for i in x:
  soma += i
media = soma / len(x)

sun = 0
for i in x:
  sun += ((i-media)**2)
  dpi = sqrt((sun/N))

print('Média = {0:.2f} e Desvio = {1:.4f}'.format(media, dpi))

# Exercicio 4
# Faça um Programa que leia 20 números inteiros e armazene-os em uma lista. Armazene os números pares na lista par e os números ímpares na lista impar. Imprima as três listas no final.
num = []
n = 0
result = ''
# par = []
par = ''
# impar = []
impar = ''

while n < 20:
  num.append(int(input()))
  n+=1

for i in num:
  result += '{0} '.format(i)
  if i % 2 == 0:
    # par.append(i)
    par += '{0} '.format(i)
  else:
    # impar.append(i)
    impar += '{0} '.format(i)

print(result)
print(impar)
print(par)

# Exercicio 5
# Em álgebra linear, o produto escalar é uma função binária definida entre dois vetores que fornece um número real (também chamado "escalar") como resultado. Algebricamente, o produto escalar de dois vetores é formado pela multiplicação de seus componentes correspondentes e pela soma dos produtos resultantes.
# Faça um programa que leia a dimensão dos vetores a serem multiplicados, em seguida os componentes de cada vetor, e apresente como resultado o resultado escalar.
a = []
b = []
tam = int(input('Digite a dimensão dos vetores: '))
soma = 0
n = 0
m = 0

print('Digite o vetor 1:')
while n < tam:
  a.append(int(input()))
  n+=1

print('Digite o vetor 2:')
while m < tam:
  b.append(int(input()))
  m += 1
  
for i, j in zip(a, b):
  # for j in range(len(b)):
    print('i = ', i)
    print('j = ', j)
    soma += i * j

print(soma)

# Exercicio 6
# Escreva uma função que recebe uma lista de números inteiros e retorne uma nova lista que contém o quadrado de cada um desses números. Você só precisa entregar o código da função.
def quadrado(lista):
  listaQuadrada = []
  for i in lista:
    listaQuadrada.append(i**2)
  return listaQuadrada
    

print(quadrado([1, 2, 3, 4, 5, 6, 7]))
