from separarPalavras import contaPalavras, ordenaPalavras

def main():
  frase = input('Digite as palavras desejadas separando-as por hífen(-): ')
  maiores = contaPalavras(frase)
  print(ordenaPalavras(frase))
  print(maiores)
main()
