from dataSet import deletaDados, trataDados

def main():
  arq = input('Digite o nome do arquivo com o extensão: ')
  
  lista = trataDados(arq)
  lista2 = deletaDados(lista)
  for i in range(len(lista2)):
    for n in range(len(lista2[i])):
      if n == 5:
        print(lista2[i][n], end='')
      else:
        print(lista2[i][n], end=',')
    print()

main()
