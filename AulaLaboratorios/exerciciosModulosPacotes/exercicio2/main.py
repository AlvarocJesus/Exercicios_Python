import calculoCrivo

def main():
  limite = int(input('Digite um limite para os números primos: '))
  
  crivo = calculoCrivo.calculoCrivo(limite)
  print(*crivo)

main()
