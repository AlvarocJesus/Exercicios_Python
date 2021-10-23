import criaPlaca

def main():
  l = criaPlaca.geraLetra()
  n = criaPlaca.geraNumero()
  placa = criaPlaca.montaPlaca(l, n)
  print('Placa =', end=' ')
  for i in placa:
    print(i, end='')

main()
