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
      lenIguais.append(data[i][j].replace(',', '').replace('.', ''))
print(lenIguais)
print(f'O tamanho da palavra mais longa e "{maisLongas}", as outras palavras que tem o mesmo tamanho sao: {lenIguais}') """

# Exercicio 3
# Escreva um programa que exiba a(s) palavra(s) que ocorre(m) com mais freqüência em um arquivo e quantas vezes a(s) palavra(s) aparece(m). Seu programa deve começar lendo o nome do arquivo do usuário. Em seguida, ele deve encontrar a(s) palavra(s) mais frequente(s), ignorando letras maiúsculas ou minúsculas e a pontuação. Desta forma, por exemplo, as palavras apple, apple!, Apple, APPLE e ApPlE devem todas ser contadas como uma única palavra. Para testar, utilize o texto “Python.txt” que está no Moodle.
arq = open('../Python.txt', 'r', encoding='utf-8')
for i in arq.readlines():
  print(i)