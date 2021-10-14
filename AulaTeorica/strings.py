# Exibindo todos os caractere da tabela ASCII
""" for i in range(0,255):
  print('%c' %i) """
  
# Exercicio 1
# Peça ao usuário uma string e imprima se essa string é um palíndromo ou não. Palíndromo é uma palavra ou frase(normalmente, ignorando-se os espaços em branco) que se pode ler, indiferentemente, da esquerda para a direita ou vice-versa. Exemplos: “ovo”, “a grama é amarga”
""" palavra = input('Digite uma palavra: ')
semEspaco = palavra.replace(' ', '')
novaPalavra = semEspaco[::-1]

if semEspaco == novaPalavra:
  print('E um palindromo')
else:
  print('Nao e palindromo') """

# Exercicio 2
# Neste exercício, você criará um programa em Python que identifica a(s) palavra(s) mais longa(s) em um arquivo. Seu programa deve exibir uma mensagem que inclua o tamanho da palavra mais longa, juntamente com todas as palavras desse comprimento que ocorreram no arquivo. Desconsidere sinais de pontuação. Utilize o arquivo “Python.txt”, que está no Moodle, para testar.
""" maisLongas = 0
lenIguais = []
data = []

arq = open('../Python.txt', 'r', encoding='utf-8')
for i in arq.readlines():
  data.append(i.strip().split(' '))
for i in range(len(data)):
  for j in range(len(data[i])):
    if len(data[i][j].replace(',', '').replace('.', '')) > maisLongas:
      maisLongas = len(data[i][j].replace(',', '').replace('.', ''))
for i in range(len(data)):
  for j in range(len(data[i])):
    if len(data[i][j].replace(',', '').replace('.', '')) == maisLongas:
      # if j not in lenIguais:
      lenIguais.append(data[i][j].replace(',', '').replace('.', ''))
print(lenIguais)
print(f'O tamanho da palavra mais longa e "{maisLongas}", as outras palavras que tem o mesmo tamanho sao: {lenIguais}') """

# Exercicio 3
# Escreva um programa que exiba a(s) palavra(s) que ocorre(m) com mais freqüência em um arquivo e quantas vezes a(s) palavra(s) aparece(m). Seu programa deve começar lendo o nome do arquivo do usuário. Em seguida, ele deve encontrar a(s) palavra(s) mais frequente(s), ignorando letras maiúsculas ou minúsculas e a pontuação. Desta forma, por exemplo, as palavras apple, apple!, Apple, APPLE e ApPlE devem todas ser contadas como uma única palavra. Para testar, utilize o texto “Python.txt” que está no Moodle.
""" data = []
maisFrequentes = []
frequenciaMaior = 0
arq = open('../Python.txt', 'r', encoding='utf-8')
for i in arq.readlines():
  separado = i.replace('.', '').replace(',', '').lower().split()
  data.append(separado)
arq.close()
palavras = []
for palavra in data:
  contador = data.count(palavra)
  if contador > frequenciaMaior:
    maisFrequentes = []
    if palavra not in maisFrequentes:
      maisFrequentes.append(palavra)
    frequenciaMaior = contador
  elif contador == frequenciaMaior:
    if palavra not in maisFrequentes:
      maisFrequentes.append(palavra)
print(frequenciaMaior)
print(maisFrequentes) """

# Exercicio 4
# Pig Latin é uma língua construída pela transformação de palavras da língua inglesa. Embora as origens da língua sejam desconhecidas, ela é mencionada em pelo menos dois documentos do século XIX, sugerindo que ela existe há mais de 100 anos. As seguintes regras são usadas para traduzir o inglês para o Pig Latin:
# a. Se a palavra começar com uma consoante(incluindo y), todas as letras no início da palavra, até a primeira vogal(excluindo y), serão removidas e adicionadas ao final da palavra, seguidas de ay. Por exemplo, computer se torna um omputercay e think se torna inkthay.
# b. Se a palavra começar com uma vogal(não incluindo y), então way é adicionado ao final da palavra. Por exemplo, o algorithm se torna algorithmway e office se torna officeway. Escreva um programa que leia uma linha de texto do usuário. Então, seu programa deve traduzir a linha para Pig Latin e exibir o resultado. Trate letras maiúsculas, minúsculas e pontuação
palavra = input('Digite uma palavra em ingles: ')
vogal = ['a', 'e', 'i', 'o', 'u']
consoantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

word = ''
if palavra.lower()[0] in consoantes:
  for i in palavra:
    if i in vogal:
      word = palavra.slice[:i]
  print(word+'ay')
elif palavra.lower()[0] in vogal:
  print(palavra+'way')
