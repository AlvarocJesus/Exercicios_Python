# Exercicio 1
# Escreva uma função chamada read_file que abre e exibe o conteúdo de um arquivo chamado "poema.txt". Escreva apenas a função.
lista = []
def read_file():
  poema = open('poema.txt', 'r')
  for letra in poema.readlines():
    print(letra.strip())
  print(lista)
read_file()

# Exercicio 2
# Escreva uma função chamada conta_palavras que conte e exibe e quantidade de palavras contidas em um arquivo chamado "palavras.txt". Entregue apenas a função.
def conta_palavras():
  palavras = open('palavras.txt', 'r')
  palavra = []
  qqtWord = 0

  for linha in palavras.readlines():
    separada = linha.split()
    palavra.append(separada)
  for p in range(len(palavra)):
    qqtWord += len(palavra[p])
  print('Quantidade de palavras:', qqtWord)
conta_palavras()

# Exercicio 3
# Crie uma função chamada lista_arquivo, que recebe uma lista de palavras, escreve cada uma dessas palavras em um arquivo e exibe o conteúdo do arquivo. Entregue apenas a função.
cores = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
def lista_arquivo(cores):
  cor = open('cores.txt', 'w')
  
  for i in cores:
    cor.write('%s\n' %i)
  cor.close()
  
  cor = open('cores.txt', 'r')
  for i in cor.readlines():
    print(i.strip())
lista_arquivo(cores)

# Exercicio 4
# Escreva uma função chamada acha_palavra, que recebe uma palavra como parâmetro e conta e exibe a quantidade de ocorrências dessa palavra em um arquivo chamado "busca.txt". Entregue apenas a função.
def acha_palavra(word):
  lista = []
  busca = open('busca.txt', 'r')
  x = 0

  for i in busca.readlines():
    linha = i.split()
    lista.append(linha)

  for i in range(len(lista)):
    for k in range(len(lista[i])):
      if lista[i][k] == word:
        x += 1
  print(x)

# Exercicio 5
# Considere o arquivo "quadrado.txt", que contém, em cada linha, um número inteiro. Escreva uma função chamada ao_quadrado, que lê cada número do arquivo "quadrado.txt", calcula o seu quadrado e armazena o resultado em uma lista. Ao fim, essa função deve exibir o conteúdo da lista. Entregue apenas a função.
def ao_quadrado():
  quadrado = open('quadrado.txt', 'r')
  lista = []

  for i in quadrado.readlines():
    lista.append(int(i.strip()))
  for i in range(len(lista)):
    lista[i] = lista[i]**2
  print(lista)

# Exercicio 6
# Escreva uma função chamada line_count que conte e exiba a quantidade de linhas que não começam com a letra "E" em um arquivo chamado "story.txt". Entregue apenas a função.
def line_count():
  count = open('story.txt', 'r')
  lista = []
  x = 0

  for i in count.readlines():
    lista.append(i.split())
  for i in range(len(lista)):
      for k in range(len(lista[i])):
        if lista[i][k] == 'E' or lista[i][k] == 'Em':
          x += 1
  print("Numero de linhas que nao comecam com 'E'=", len(lista) - x)
