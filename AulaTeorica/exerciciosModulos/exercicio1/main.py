import doaSangue

def main():
  sexo = input('Digite Masculino ou Feminino: ')
  peso = float(input('Digite seu peso: '))

  if doaSangue.doarSangue(sexo, peso):
    print('Apto!')
  else:
    print('Nao pode doar!')

if __name__ == '__main__':
  main()