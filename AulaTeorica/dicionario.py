""" 
Sao vetores associativos
  - colecoes desordenadas de dados
  - funciona com a ideia de mapa
  - chave e valor -> key:value
  - chave(key): serve para deixar otimizado
  - valor(value): valor associado a uma chave
  - valores acessados por meio das chaves
  - devem ser exclusivas e valores imutaveis
  - sintaxe: 
  d={
    <key1>:<value1>
  }
"""
""" 'nome': 'fulano',
  5: 'cinco',
  'lista': [1,2,3]
}
print(teste) """

# Acessando elementos
""" ingles={
  'um': 'one',
  'dois': 'two',
  'tres': 'three'
}
ingles_num = {
  1: 'one',
  2: 'two',
  3: 'three'
}
print(ingles['um'])
print(ingles_num[1]) """

# Adicionando elementos
""" ingles_num = {
    1: 'one',
    2: 'two',
    3: 'three'
}
ingles_num[5] = 'five'
print(ingles_num) """

# removendo elementos
""" ingles = {
    'um': 'one',
    'dois': 'two',
    'tres': 'three'
}
ingles_num = {
    1: 'one',
    2: 'two',
    3: 'three'
}
del ingles_num[3]
del ingles['tres']
print(ingles_num)
print(ingles) """

# Alguns metodos
# items() -> retorna todos os elementos do dicionario -> em pares chave:valor
""" dicionario = {
  'um': 'exemplo',
  'dois': 'de',
  'tres': 'dicionario',
}
d = dicionario.items()
d = list(d)
print(d) """

# keys() -> retorna todas as chaves do dicionario
""" dicionario = {
    'um': 'exemplo',
    'dois': 'de',
    'tres': 'dicionario',
}
d = dicionario.keys()
d = list(d)
print(d)
print(d[0]) """

# values() -> retorna todos os valores do dicionario
""" dicionario = {
    'um': 'exemplo',
    'dois': 'de',
    'tres': 'dicionario',
}
d = dicionario.values()
d = list(d)
print(d)
print(d[0]) """

# iteracao
""" dicionario = {
    'um': 'exemplo',
    'dois': 'de',
    'tres': 'dicionario',
}
# iterando pela chave
for chave in dicionario:
  print(chave)

# iterando pelo valor
for valor in dicionario.values():
  print(valor)

# iterando com chave e valor
for chave,valor in dicionario.items():
  print(chave,valor) """

""" ------------------------------------------------------------------------------------------------------- """

# Exercicio 1
""" def procuraReversa(dicionario, item):
  lista = []
  for chave, valor in dicionario.items():
    if valor == item:
      lista.append(chave)
  
  return lista

def main():
  dicionario = {
    1: 'a',
    5: 'b',
    6: 'e',
    'ac': 1234,
    'vf': 4,
    'ot': 10,
    '4': 4
  }
  print(procuraReversa(dicionario, 'a'))
main() """

# Exercicio 2
""" from random import randint
dados = {
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
    9: 0,
    10: 0,
    11: 0,
    12: 0
}
def lancaDado():
  dado1 = randint(1,6)
  dado2 = randint(1,6)
  somatoria = dado1 + dado2
  dados[somatoria] = dados[somatoria] + 1

def imprimir():
  for chave, valor in dados.items():
    print("{0}: {1} = {2:.2f}%".format(chave, valor, (valor/1000000)*100))

def main():
  for i in range(1000000):
    lancaDado()
  imprimir()
  
main() """

# Exercicio 3
""" letras = {}

def caractereUnico(palavra):
  for i in palavra:
    letras[i] = 1
  return len(letras)      

def main():
  palavra = input('Digite uma palavra: ').lower()
  print(caractereUnico(palavra))

main() """

# Exercicio 4
""" palavra1 = {}
palavra2 = {}
def anagrama(frase1, frase2):
  for i in frase1:
    palavra1[i]=1
  for i in frase2:
    palavra2[i] = 1
  if palavra1 == palavra2:
    return 'E um anagrama'
  else:
    return 'Nao e um anagrama'

def main():
  frase1 = input('Texto a primeira palavra: ')
  frase2 = input('Texto a segunda palavra: ')
  
  print(anagrama(frase1, frase2))
  
main() """

# Exercicio 5
from random import randint
cartela = {
    'B': [],
    'I': [],
    'N': [],
    'G': [],
    'O': [],
}

def criaCartela():
  
  for valor in range(5):
    b = randint(1, 15)
    if b not in cartela['B']:
      cartela['B'].append(b)
  
  for valor in range(5):
    i = randint(16, 30)
    if i not in cartela['I']:
      cartela['I'].append(i)
  
  for valor in range(5):
    n = randint(31, 45)
    if n not in cartela['N']:
      cartela['N'].append(n)
  
  for valor in range(5):
    g = randint(46, 60)
    if g not in cartela['G']:
      cartela['G'].append(g)
  
  for valor in range(5):
    o = randint(61, 75)
    if o not in cartela['O']:
      cartela['O'].append(o)

def main():
  criaCartela()
  for chave, valor in cartela.items():
    print(chave, *valor)

main()
