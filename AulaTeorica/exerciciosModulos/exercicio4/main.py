import verificaSenha

def main():
  senha = input('Digite sua senha: ')

  if verificaSenha.tamanhoMin(senha):
    if verificaSenha.letraMaiuscula(senha):
      if verificaSenha.letraMinuscula(senha):
        if verificaSenha.umNum(senha):
          print('Senha forte!')
        else:
          print('Senha tem que ter pelo menos 1 numero')
      else:
        print('Senha tem que ter pelo menos 1 uma letra minúscula')
    else:
      print('Senha tem que ter pelo menos 1 maiúscula')
  else:
    print('Senha tem que ter pelo menos 8 caracteres')

if __name__ == '__main__':
  main()
