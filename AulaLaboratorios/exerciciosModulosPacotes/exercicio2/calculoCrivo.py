def calculoCrivo(limite):
  primos = []
  
  for k in range(limite+1):
    primos.append(k)

  for i in range(len(primos)):
    if primos[i] == 0 or primos[i] == 1:
      primos[i] = 0
    elif primos[i] == 2:
      primos[i] = 2
    else:
      div = []
      for p in range(1,i):
        if len(div) >= 2:
          primos[i] = 0
        else:
          if i % p ==0:
            div.append(p)
          else:
            pass
  return primos
