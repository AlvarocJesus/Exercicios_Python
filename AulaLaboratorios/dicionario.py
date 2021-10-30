# Exercicio 1
""" codigo_morse = {
  'A': '.-',
  'B': '-...',
  'C': '-.-.',
  'D': '-..',
  'E': '.',
  'F': '..-.',
  'G': '--.',
  'H': '....',
  'I': '..',
  'J': '.---',
  'K': '-.-',
  'L': '.-..',
  'M': '--',
  'N': '-.',
  'O': '---',
  'P': '.--.',
  'Q': '--.-',
  'R': '.-.',
  'S': '...',
  'T': '-',
  'U': '..-',
  'V': '...-',
  'W': '.--',
  'X': '-..-',
  'Y': '-.--',
  'Z': '--..',
  '0': '-----',
  '1': '.----',
  '2': '..---',
  '3': '...--',
  '4': '....-',
  '5': '.....',
  '6': '-....',
  '7': '--...',
  '8': '---..',
  '9': '----.'
}
def converte(codigo_morse, frase):
  convertido = []

  lista = frase.replace('!', '').split()

  for i in range(len(lista)):
    for n in range(len(lista[i])):
      convertido.append(codigo_morse[lista[i][n].upper()])
  return ' '.join(convertido)


# print(converte(codigo_morse, 'Ciencia da Computacao'))
print(converte(codigo_morse, 'Hello World!!!')) """

# Exercicio 2
""" def contaPalavras(frase):
  incidencia = {}
  
  lista = frase.replace('?', '').replace('!', '').replace(',', '').strip().split(' ')
  
  for i in range(len(lista)):
    if lista[i].lower() in incidencia:
      incidencia[lista[i].lower()] = incidencia[lista[i].lower()]+1
    else:
      incidencia[lista[i].lower()] = 1
    
  return incidencia


# frase = "Um teste, dois testes, mais testes, acabou?, SIM !!!"
# print(contaPalavras(frase))

p = " vou testar com testes, um teste, muitos testes, sempre Testando com Testes, muitos testes, mais testes, testes!!!"
print(contaPalavras(p)) """


# Exercicio 3
def numero_texto(num):
  dezena = {
    '1': "dez",
    '2': "vinte",
    '3': "trinta",
    '4': "quarenta",
    '5': "cinquenta",
    '6': "sessenta",
    '7': "setenta",
    '8': "oitenta",
    '9': "noventa",
  }

  unidade = {
    '1': "um",
    '2': "dois",
    '3': "tres",
    '4': "quatro",
    '5': "cinco",
    '6': "seis",
    '7': "sete",
    '8': "oito",
    '9': "nove",
  }
  unidade2={
    '11': "onze",
    '12': "doze",
    '13': "treze",
    '14': "quatorze",
    '15': "quinze",
    '16': "dezsesseis",
    '17': "dezsessete",
    '18': "dezoito",
    '19': "deznove",
  }

  centena = {
    '0': "cem",
    '1': "cento",
    '2': "duzentos",
    '3': "trezentos",
    '4': "quatrocentos",
    '5': "quinhentos",
    '6': "seiscentos",
    '7': "setecentos",
    '8': "oitocentos",
    '9': "novecentos",
  }
  
  lista = []
  
  num = str(num)
  tamanho = len(num)
  
  if tamanho == 1:
    if num in unidade:
      lista.append(unidade[num])
  if tamanho == 2:
    print(num[0])
    if num[0] == '1':
      if num in unidade2:
        lista.append(dezena[num])
    else:
      if num[0] in dezena:
        lista.append(dezena[num[0]])
        if num[1] in unidade:
          lista.append(unidade[num[1]])
  elif tamanho ==3:    
      if num[0] in centena:
        lista.append(centena[num[0]])
        if num[-2] in dezena:
          lista.append(dezena[num[-2]])
          if num[-1] in unidade:
            lista.append(unidade[num[-1]])
  print(' e '.join(lista))


n = int(input("Digite um número entre 0 e 999: "))
numero_texto(n)
