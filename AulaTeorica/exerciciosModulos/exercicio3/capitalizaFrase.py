def capitalizaFrase(frase):
  newFrase = frase.split(' ').split('?')
  
  newFrase[0].capitalize()
  
  for i in range(len(newFrase)):
    if '?' == newFrase[i] or '!' == newFrase[i] or '.' == newFrase[i]:
      newFrase[i+1].capitalize()

  # que horas tenho que estar lá? qual é o endereço?
  # return ' '.join(newFrase)
  return newFrase
