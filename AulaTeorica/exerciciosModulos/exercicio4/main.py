import verificaSenha

senha = input('Digite sua senha: ')

boaSenha = 0

if verificaSenha.tamanhoMin(senha):
  boaSenha += 1
elif verificaSenha.letraMaiuscula(senha):
  boaSenha += 1
elif verificaSenha.letraMinuscula(senha):
  boaSenha += 1
elif verificaSenha.umNum(senha):
  boaSenha +=1

if boaSenha == 5:
  print(True)
else:
  print(False)
