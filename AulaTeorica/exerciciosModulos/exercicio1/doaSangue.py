def doarSangue(sexo, peso):
  if sexo == 'Feminino':
    if peso >= 50:
      return True
    else:
      return False
  elif sexo == 'Masculino':
    if peso >= 60:
      return True
    else:
      return False
