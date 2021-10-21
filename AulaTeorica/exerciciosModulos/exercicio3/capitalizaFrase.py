def capitalizaFrase(frase):
  for i in range(len(frase)):
    if i == 0:
      frase2 = frase[i].upper()+frase[i+1:]
    if ('?' == frase[i] or '!' == frase[i] or '.' == frase[i]):
      if i < len(frase)-1:
        frase2 = frase2[:i+2]+frase2[i+2].upper() + frase2[i+3:]

  # return ' '.join()
  return frase2
# que horas tenho que estar lá? qual é o endereço?
