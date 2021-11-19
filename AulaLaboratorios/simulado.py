# Exercicio 1
# A seguinte sequência de números 0 1 1 2 3 5 8 13 21... é conhecida como série de Fibonacci. Nessa sequência, cada número, depois dos 2 primeiros, é igual à soma dos 2 anteriores. Escreva um algoritmo que leia um inteiro N (N < 46) e mostre os N primeiros números dessa série.

n=int(input())
a, b = 0, 1
k=1
while k <= n:
  print(a, end=' ')
  a, b = b, a+b
  k=k+1

# Exercicio 2
def humor(a,b,c):
  if a > b and c > b or c==b:
    return (':)')
  elif b > a and b > c or c == b:
    return (':(')
  elif b > a and (c>b and c-b<=b-a):
    return (':(')
  elif b > a and (c > b and c-b >= b-a):
    return (':)')
  elif a > b and (b > c and c-b <= b-a):
    return (':)')
  elif a > b and (b > c and c-b >= b-a):
    return (':(')
  elif a == b and b > c:
    return (':(')
  else:
    return (':(')

a = 4
b = 10
c = 20
print(humor(a,b,c))

# Exercicio 3
n = int(input())
f=1
for i in range(0, n):
  f=f*(n-i)
print(f)

# Exercicio 5
# Leia 4 valores inteiros A, B, C e D. A seguir, se B for maior do que C e se D for maior do que A, e a soma de C com D for maior que a soma de A e B e se C e D, ambos, forem positivos e se a variável A for par escrever a mensagem "Valores aceitos", senão escrever "Valores não aceitos".
A = int(input('Digite o valor de A:'))
B = int(input('Digite o valor de B:'))
C = int(input('Digite o valor de C:'))
D = int(input('Digite o valor de D:'))

if B>C and D>A and C+D>A+B and C>0 and D>0 and A%2==0:
  print('Valores aceitos')
else:
  print('Valores não aceitos')

# Exercicio 6
lista = [0,-5,10,7,-8,6,14,8,-2,0,-1,14]
for i in range(len(lista)):
  if lista[i]<0:
    lista[i]=-2*lista[i]
  else:
    lista[i]+=1
print(lista)

# Exercicio 7
i = 0
j = 1
value = 0
temp = 0
temp2 = 0

while i <= 2:
    if(temp2 == 0):
        print("I=%.0f J=%.0f" % (i, j))
    else:
        print("I=%.1f J=%.1f" % (i, j))

    temp += 1
    if(temp == 3):
        i += 0.2
        value += 0.2
        j = value
        temp = 0
        temp2 += 1

    if(temp2 == 5):
        temp2 = 0
    j += 1

# Exercicio 8
# Faça um programa que leia um valor N. Este N será o tamanho de um vetor X[N]. A seguir, leia cada um dos valores de X, encontre o menor elemento deste vetor e a sua posição dentro do vetor, mostrando esta informação.
n = int(input('Digite o valor de N:'))
x = []

for i in range(n):
  a = int(input(f'Digite o {i+1} valor de X:'))
  x.append(a)

menor = 99
posicao = 0
for i in range(len(x)):
  if x[i] < menor:
    menor = x[i]
    posicao = i
print(f'Menor valor: {menor}')
print(f'Posicao: {posicao}')

# Exercicio 9
a = 2
b=3
c=2
d = 6

if b>c and d>a and c+d>a+b and c>0 and d>0 and a%2==0:
  print('Valores aceitos')
else:
  print('Valores nao aceitos')

# Exercicio 10
# Leia um valor inteiro n. Apresente o quadrado de cada um dos valores pares, de 1 até n, inclusive n, se for o caso.
n=int(input())

for i in range(1, n+1):
  if i%2==0:
    print(f'{i}^2 = {i**2}')
