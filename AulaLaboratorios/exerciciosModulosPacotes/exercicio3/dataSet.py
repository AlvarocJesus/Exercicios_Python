def trataDados(arq):
  arquivo = open(arq, 'r')
  data = []
  
  for i in arquivo.readlines():
    data.append(i.strip().split(','))
  
  return data

def deletaDados(lista):
  lista2 = []
  for i in range(len(lista)):
    if lista[i][3] == 'ball':
      lista2.append(lista[i])
    else:
      pass
  for k in range(len(lista2)):
    del(lista2[k][2])
    del(lista2[k][1])
  return lista2
