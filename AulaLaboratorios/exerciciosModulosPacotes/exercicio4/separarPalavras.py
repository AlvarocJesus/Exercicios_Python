def ordenaPalavras(frase):
  lista = frase.split('-')
  newlista = sorted(lista)
  
  return '-'.join(newlista)

def contaPalavras(frase):
  maior = menor = 0
  lista = frase.split('-')
  
  for i in range(len(lista)):
    for k in range(len(lista[i])):
      if lista[i][k].isupper():
        maior+=1
      elif lista[i][k].islower():
        menor+=1
  return f'''Maiúsculas = {maior}\nMinúsculas = {menor}'''
