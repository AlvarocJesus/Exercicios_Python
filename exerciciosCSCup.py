""" from math import trunc


x = int(input())
i = 0
while i < 12:
  i += 1
  if x % 2 != 0:
    print(x)
  x += 1
 """
 
""" x = int(input())
y = int(input())

maior = x if x > y else y
menor = y if y < x else x
menor += 1
soma = 0

while (menor < maior):
    if(menor % 2 != 0):
        soma += menor
    menor += 1
print(soma)
 """

""" def separate(frase):
  nomes = frase.split('_') #.split('.').split('-')
  nome = ''
  
  for i in range(len(nomes)):
    if len(nomes[i])==14:
      print(nomes[i])
      cpf = nomes[i]
    else:
      cpf = 'Inválido'
    if '@' not in nomes[i]:
      email = 'Inválido'
    else:
      email = nomes[i]
  
  return f'Nome: {nome}\nCPF: {cpf}\ne-mail: {email}'


print(separate('João_Silva_Rodrigues_159.138.645-21_jsrodrigues@gmail.com')) """

""" base = input()
num = input()

if base == 'b':
  dec = int(num, 2)
  num = int(num)
  hexa = hex(num).replace('0x','')
  print(f'Decimal = {dec}\nHexadecimal = {hexa[-1]}')
elif base == 'd':
  num = int(num)
  bina = format(num, 'b')
  hexa = format(num, 'X')
  print(f'Binário = {bina}\nHexadecimal = {hexa}')
elif base == 'h':
  dec = int(num, 16)
  num = int(num)
  bina = format(num, 'b')
  print(f'Decimal = {dec}\nBinário = {bina}')
 """


def procuraReversa(dicionario, item):
  lista = []
  for chave, valor in dicionario.items():
    if valor == item:
      lista.append(chave)

  return print(lista)


def main():
  dicionario = {}
  valor = int(input())
  i=0
  while i <8:
    key = input()
    value = int(input())
    dicionario[key] = value
    i+=1
  print(i)
  print(dicionario)
  procuraReversa(dicionario, valor)


main()
