# Exercicio 1
# Crie uma função em Python chamada contaPalavras que recebe uma string e conta quantas palavras tem nessa string. Sua função deve  retornar o número de palavras contadas.
def contaPalavras(palavra):
  return len(palavra.split())

print(contaPalavras("A FEI eh fantastica"))

# Exercicio 2
# A Criptografia de César é uma técnica bastante simples e provavelmente a mais conhecida de todas.
# Trata-se de um tipo de substituição, na qual cada letra de um texto a ser criptografado é substituída por outra letra presente no alfabeto, porém deslocada um certo número de posições à esquerda ou à direita.
# Por exemplo, se empregarmos uma troca de quatro posições à esquerda, cada letra é substituída pela letra que está quatro posições adiante no alfabeto, e nesse caso a letra A seria substituída pela letra E, a letra B por F, a letra C por G, e assim sucessivamente.
# Crie uma função chamada criptCesar que receba uma frase e o valor do deslocamento, podendo ser positivo ou negativo. A criptografia deverá ser cíclica, como na imagem acima, isso significa que quando terminar em Z o próximo caractere é A. Distingui
# Sua função deve ignorar caracteres especiais e os espaços.
def criptCesar(p, n):
  lista = []
  for i in p:
    x = ord(i)
    letra = x + n
    if (x >= 65  and x <= 90):
      if letra < 65:
        letra = 91 - (65 - letra)
      elif letra > 90 and letra < 97:
        letra = 64 + (letra - 90)
      elif (x >= 97  and x <= 122):
        if letra > 90 and letra < 97:
          letra = 123 - (97 - letra)
        elif letra > 122:
          letra = 96 + (letra - 122)
        else:
            letra = x
        lista.append((chr(letra)).upper())
    
    for i in lista:
        print(i, end="")

# Exercicio 3
# Implemente uma função que receba um nome completo e apresente apenas o último nome e o 1o nome na seguinte forma:
# último, 1o nome.
def nomeCitacao(nome):
  lista = []
  lista.append(nome.split())
  print('%s, %s' %(lista[0][-1], lista[0][0]))

nomeCitacao("Paulo Santos")

# Exercicio 4
# Crie uma função chamada spellChecker() que recebe uma String e verifica se as palavras dessa String estão corretas, para verificação utilize o arquivo words.txt (o arquivo possui 466k palavras), que possuí todas as palavras do inglês. Sua função deverá retornar uma listas das palavras que não forem encontradas no arquivo.
def spellChecker(palavra):
  listaArq = []
  listaWord = []
  incorrect = []
  arq = open('./words.txt', 'r')
  for i in arq.readlines():
    listaArq.append(i.lower().strip())
  arq.close()
  
  listaWord = palavra.lower().replace(',', '').split()
  
  for lWord in range(len(listaWord)):
    if listaWord[lWord] not in listaArq:
      incorrect.append(listaWord[lWord])
  return incorrect

print(spellChecker("Hello World, Olá Mundo"))


# Exercicio 5
# Jogo da forca
palavraSecreta = input('Digite a palavra secreta:')
erro = 0
repetidas = []
letras = '-' * len(palavraSecreta)
erro1 = '''
X==:==
X  :  
X  O  
X     
X     
X     
===========
'''
erro2 = '''
X==:==
X  :  
X  O  
X  |  
X     
X     
===========
'''
erro3 = '''
X==:==
X  :  
X  O  
X \|  
X     
X     
===========
'''
erro4 = '''
X==:==
X  :  
X  O  
X \|/  
X    
X     
===========
'''
erro5 = '''
X==:==
X  :  
X  O  
X \|/  
X /  
X     
===========
'''
erro6 = '''
X==:==
X  :  
X  O  
X \|/  
X / \ 
X     
===========
'''
acerto = '''
X==:==
X  :  
X    
X   
X  
X     
===========
'''
print('\n\n\n\n\n\n\n\n\n\n', letras)

while True:
  chute = input('\nDigite uma letra:')
  
  if chute in repetidas:
    print('Digite outra letra!\n')
  else:
    if chute in palavraSecreta:
      index = palavraSecreta.find(chute)
      print()
      print(acerto)
      letras = letras[0:palavraSecreta.find(chute)] + chute + letras[palavraSecreta.find(chute)+1:]
      print(letras)
      
    else:
      erro += 1
      repetidas.append(chute)
      print('Você errou!')
      if erro == 1:
        print()
        print(erro1)
      if erro == 2:
        print()
        print(erro2)
      if erro == 3:
        print()
        print(erro3)
      if erro == 4:
        print()
        print(erro4)
      if erro == 5:
        print()
        print(erro5)
      if erro == 6:
        print()
        print(erro6)
        print('\nEnforcado!')  
        break
