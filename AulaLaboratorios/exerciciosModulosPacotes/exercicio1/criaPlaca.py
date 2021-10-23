from random import randrange, choice

def geraLetra():
  letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  letra = []
  
  for i in range(4):
    letra.append(choice(letras))
  return letra

def geraNumero():
  num = []
  for i in range(3):
    num.append(randrange(9))
  return num

def montaPlaca(letra, num):
  placa = []
  for i in range(7):
    if i <=2:
      placa.append(letra[i])
    elif i ==3:
      placa.append(num[0])
    elif i == 4:
      placa.append(letra[3])
    else:
      placa.append(num[i-4])
  return placa
      
