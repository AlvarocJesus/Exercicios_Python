# Pelo menos 8 caracteres
def tamanhoMin(senha):
  if len(senha) >= 8:
    return True
  else:
    return False

# Pelo menos uma letra maiúscula
def letraMaiuscula(senha):
  maiuscula = 0
  for i in range(len(senha)):
    if senha[i].isupper():
      maiuscula+=1
  if maiuscula >= 1:
    return True
  else:
    return False
    

# Pelo menos uma letra minúscula
def letraMinuscula(senha):
  minuscula = 0
  for i in range(len(senha)):
    if senha[i].islower():
      minuscula+=1
  if minuscula >= 1:
    return True
  else:
    return False

# Pelo menos um número
def umNum(senha):
  num = 0
  for i in range(len(senha)):
    if senha[i].isdigit():
      num+=1
  if num >= 1:
    return True
  else:
    return False
