# Exercicio 1
# Faça um programa que mostra o menor valor dentro da lista T = [1, 7 ,2 ,4]
T = [1, 7, 2, 4]
menor = T[0]

for i in range(0, len(T)):
  if T[i] < menor:
    menor = T[i]
print(menor)
# Jeito mais simples
# min(T)

# Exercicio 2
# Crie um programa em que peça 10 números reais, armazene-os em uma lista e diga qual é o índice do maior, e seu valor.
z = []
maior = 0
indice = 0
n = 0

while n < 10:
    z.append(float(input('Digite um numero: ')))
    for i in range(0, len(z)):
        if maior < z[i]:
            maior = z[i]
            indice = i
    n += 1
print('Maior numero', maior, 'seu indice e', indice)

# Exercicio 3
# Faça um programa para criar uma lista de 10 elementos(pedir para o usuário) e apresentar: a soma dos ELEMENTOS pares e a soma dos elementos de ÍNDICE par
z = []
soma = 0
indice = 0
n = 0

while n < 10:
  z.append(int(input('Digite um numero: ')))
  n += 1

  for i in range(len(z)):
    if z[i] % 2 == 0:
      soma += z[i]
    if i % 2 == 0:
      indice += i
      

print('Soma de todos os numeros pares', soma, 'soma de todos os indices', indice)

# Exercicio 4
# Faça um programa que imprime uma sequência de n números em ordem inversa à da leitura. Utilize uma lista para isso.
z = []
x = 5

while True:
  n = int(input('Digite um numero: '))
  if n == 10: break
  z.append(n)

print(z[::-1])

for i in range(x):
  z.append(int(input('Digite um numero: ')))
print("Original: ")
print(z)

for i in range(x-1, -1, -1):
  print(z[i], end=",")

# Exercicio 5
# Faça um programa para criar uma lista de 10 elementos inteiros e apresentar todos os conteúdos que forem maiores que a soma de dois de seus antecessores
from random import randrange
numeros = []
soma = 0
n = 0
x = []

while n < 10:
  numeros.append(int(input('Digite um numero: ')))
  n += 1
  
  for i in range(len(numeros)):
    soma = numeros[i-1] + numeros[i-2]
    if numeros[i] > soma:
      x.append(listaInt[i])
print(x)

for i in range(10):
    numeros.append(randrange(0, 101))
print(numeros)
for i in range(2, len(numeros)):
    if numeros[i] > numeros[i-1] + numeros[i-2]:
        x.append(numeros[i])
print(x)

# Exercicio 6
# As temperaturas de uma cidade foram armazenadas na lista temperaturas = [-10, -8, 0, 1, 2, 5, -2, -4]. Faça um programa que imprime a menor e a maior temperatura, assim como a média.
temperaturas = [-10, -8, 0, 1, 2, 5, -2, -4]
media = 0
soma = 0
maior = 0
menor = 999

for i in range(len(temperaturas)):
  soma += temperaturas[i]
  media = soma / len(temperaturas)
  if temperaturas[i] > maior:
    maior = temperaturas[i]
  if temperaturas[i] < menor:
    menor = temperaturas[i]
print('maior temperatura: ', maior, '\nmenor temperatura: ', menor, '\ntemperatura media: ', media)

# Exercicio 7
# Neste exercício, você criará um programa que lê palavras do usuário até que o usuário entre com uma linha em branco. Após o usuário digitar uma linha em branco, seu programa deve exibir cada palavra digitada pelo usuário exatamente uma vez. As palavras devem ser exibidas na mesma ordem em que foram inseridas. Por exemplo, se o usuário inserir:
palavras = []
diferentes = []

while True:
  texto = input('Digite uma palavra: ')
  if texto == '': break
  
  palavras.append(texto)
  
for i in range(len(palavras)):
  if palavras[i] != palavras[i-1]:
    diferentes.append(palavras[i])
    
print(diferentes)

# Exercicio 8
# Faça um programa que preencha uma lista com dez números inteiros aleatórios (de 0 a 100). Calcule e mostre os números superiores a 50 e suas respectivas posições. O programa deverá mostrar uma mensagem caso não exista nenhum número nessa condição
from random import *
num = []

while len(num) < 10:
  num.append(randint(0, 100))

for i in range(len(num)):
  if num[i] > 50:
    print('Numero:', num[i], ', posicao: ', i)
  else:
    print('Numero inferior ou igual a 50')

# Exercicio 9
# Desafio: Faça um programa que crie uma lista com vinte números inteiros aleatórios (de 0 a 200). Ordene, então, essa lista de forma crescente
from random import *
num = []
l = []

while len(num) < 20:
  num.append(randint(0,200))

# Jeito 1
l = sorted(num)
num.sort()

print(l)