# Exercicio 1
def minimo(x,y):
  if x < y:
    return y
  else:
    return x

def maximo(x, y):
  if x > y:
    return y
  else:
    return x

def multiplo(x, y):
  return(x%y==0)


print(minimo(1, 2))
print(maximo(1, 2))
print(multiplo(2, 2))

# Exercicio 2
s=str(input('Entre com uma string: '))
s.islower()
s = s.upper()
s = s.lower()
words=s.split()
count=0
palavras={}
for word in words:
  word=word.replace(',', '')
  palavras[word]=s.count(word)
  count=count+1
print(palavras)

# Exercicio 3
# Crie uma matriz M[12][12] com números inteiros aleatórios (de 0 até 10: randint(0,10)); Então, leia um caractere maiúsculo (S ou M), que indica uma operação que deve ser realizada na matriz. Em seguida, calcule e mostre a soma (S) ou a média (M) considerando somente aqueles elementos que estão na área superior da matriz, conforme ilustrado abaixo (área verde). Exiba a matriz criada e o resultado da operação.
# Para imprimir os elementos da matriz utilize "%3d" para dar espaço de 3 caracteres.
# Utilize somente número inteiros(inclusive no cálculo da média).

from random import randint
p = input()

m = []

for i in range(12):
    linha = []
    for i in range(12):
        linha.append(randint(0, 10))
    m.append(linha)


print("Matriz criada:")
for linha in range(len(m)):
  for coluna in range(len(m[linha])):
    print('%3d' % m[linha][coluna], end=' ')
  print()

if p == "S":
    soma = 0
    for linha in range(len(m)):
        for coluna in range(len(m[linha])):
            if (linha == 0) and (0 < coluna < 11):
                soma += m[linha][coluna]
            elif (linha == 1) and (1 < coluna < 10):
                soma += m[linha][coluna]
            elif (linha == 2) and (2 < coluna < 9):
                soma += m[linha][coluna]
            elif (linha == 3) and (3 < coluna < 8):
                soma += m[linha][coluna]
            elif (linha == 4) and (4 < coluna < 7):
                soma += m[linha][coluna]
            else:
                pass

    print(f"Resultado da conta: {soma}")

elif p == "M":
    soma = 0
    for linha in range(len(m)):
        for coluna in range(len(m[linha])):
            if (linha == 0) and (0 < coluna < 11):
                soma += m[linha][coluna]
            elif (linha == 1) and (1 < coluna < 10):
                soma += m[linha][coluna]
            elif (linha == 2) and (2 < coluna < 9):
                soma += m[linha][coluna]
            elif (linha == 3) and (3 < coluna < 8):
                soma += m[linha][coluna]
            elif (linha == 4) and (4 < coluna < 7):
                soma += m[linha][coluna]
            else:
                pass

    media = soma/30
    media = round(media)
    print(f"Resultado da conta: {media}")

# Exercicio 4
def compute_bill(lista):
  stock={
    'banana':12,
    'pera': 7,
    'morango': 4,
    'caqui': 2,
  }
  prices= {
      'banana': 3,
      'pera': 5,
      'morango': 7.5,
      'caqui': 4,
  }
  total=0
  naoComprado=[]
  for x in lista:
    preco=prices[x]
    if stock[x]>1:
      total+=preco
      stock[x]=stock[x]-2
    else:
      naoComprado.append(x)
  return total, naoComprado
lista_de_compras=['banana', 'morango', 'caqui']
print(compute_bill(lista_de_compras))

# Exercicio 5
A = 0
B = 0

for contador in range(2,7):
  if(A==2):
    A+=4
  else:
    A+=1

for contador in range(0, 8):
  if(B == 3):
    B += 3
  else:
    B += 1

while(A<4):
  if(B == 4):
    B += 2
  else:
    B += 1

while(B < 4):
  if(A == 4):
    A += 2
  else:
    A += 1
print(A)
print(B)

# Exercicio 6
N=[]

for i in range(10):
  N.append(int(input()))

# for k in range(len[N]):
#   print(N[k])

reverse=[]
for i in range(len(N)-1,-1,-1):
  print(i)
  reverse.append(N[i])

for i in range(len(reverse)):
  print(f'N[{i}] = {reverse[i]}')
  

# Exercicio 8
a1,b1,c1=2,3,1

if(a1==b1)and(b1%2==0):
  c1=0
if(a1<b1)and(c1>0):
  c1=1
if(a1 > b1) and (c1==1):
  c1 = 2
if(a1<b1)and(a1%2==0):
  c1=3
if(a1<b1)and(b1%2==0):
  c1=4
if(a1<b1):
  c1=5
if(a1>b1):
  c1=6
else:
  c1 = 7
print(c1)

# Exercicio 9
x= 5
def f1():
  global x
  x=4
def f2(a,b):
  global x
  return a+b+x
total=f2(1,2)
f1()
print(total)

# Exercicio 10
i=0
while i<5:
  print(i)
  i+=1
  if i==3:
    break
else:
  print(0)

# Exercicio 11
# Neste problema, você deverá ler 3 palavras que definem o tipo de animal possível segundo o esquema abaixo, da esquerda para a direita.  Em seguida conclua qual dos animais seguintes foi escolhido, através das três palavras fornecidas.

palavra1 = input('Primeira palavra:\n')
palavra2 = input('Segunda palavra:\n')
palavra3 = input('Terceira palavra:\n')

if palavra1 == 'invertebrado':
  if palavra2 == 'inseto':
    if palavra3 == 'hematofago':
      print('pulga')
    elif palavra3 == 'herbivoro':
      print('lagarta')
  if palavra2 == 'anelideo':
    if palavra3 == 'hematofago':
      print('sanguessuga')
    elif palavra3 == 'onivoro':
      print('minhoca')
elif palavra1 == 'vertebrado':
  if palavra2 == 'mamifero':
    if palavra3 == 'herbivoro':
      print('vaca')
    elif palavra3 == 'onivoro':
      print('homem')
  if palavra2 == 'ave':
    if palavra3 == 'carnivoro':
      print('aguia')
    elif palavra3 == 'onivoro':
      print('pombo')
