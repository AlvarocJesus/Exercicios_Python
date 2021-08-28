# Exercicio 1
letra = input("Digite a letra desejada: ")

if (letra == 'a') or (letra == 'e') or (letra == 'i') or (letra == 'o') or (letra == 'u'):
  print('Essa letra é uma vogal')
elif letra == 'y':
  print('Essa letra, em algumas línguas, pode ser considerada como uma vogal e, em outras, como uma consoante.')
else:
  print('Essa letra é uma consoante.')

# Exercicio 2
dia = int(input('Digite o dia desejado: '))
mes = input('Digite o mês desejado: ')

if mes == 'março':
  if (20 <= dia <= 31):
    print('Outono')
  else:
    print('Verão')
elif mes == 'abril' or mes == 'maio':
  if (1 <= dia <= 31):
    print('Outono')
elif mes == 'junho':
  if (1 <= dia <= 20):
    print('Outono')
  elif (21 <= dia <= 30):
    print('Inverno')
if mes == 'julho' or mes == 'agosto':
  if (1 <= dia <= 31):
    print('Inverno')
if mes == 'setembro':
  if (1 <= dia <= 21):
    print('Inverno')
  elif 22 <= dia <= 31:
    print('Primavera')
if mes == 'outubro' or mes == 'novembro':
  if (1 <= dia <= 31):
    print('Primavera')
if mes == 'dezembro':
  if 1 <= dia <= 21:
    print('Primavera')
  elif 21 <= dia <= 31:
    print('Verão')
if mes == 'janeiro' or mes == 'fevereiro':
  if (1 <= dia <= 31):
    print('Verão')

# Exercicio 3
nota = input('Digite a nota em letra, e o sinal +/-: ')

if (nota == 'A') or (nota == 'A+'):
  print('%s é equivalente a 5.0' %nota)
elif nota == 'A-':
  print('%s é equivalente a 4.5' %nota)
elif nota == 'B+':
  print('%s é equivalente a 4.0' %nota)
elif nota == 'B':
  print('%s é equivalente a 3.5' %nota)
elif nota == 'B-':
  print('%s é equivalente a 3.0' %nota)
elif nota == 'C+':
  print('%s é equivalente a 2.5' %nota)
elif nota == 'C':
  print('%s é equivalente a 2.0' %nota)
elif nota == 'C-':
  print('%s é equivalente a 1.5' %nota)
elif nota == 'D+':
  print('%s é equivalente a 1.0' %nota)
elif nota == 'D':
  print('%s é equivalente a 0.5' %nota)
elif nota == 'F':
  print('%s é equivalente a 0.0' %nota)
else:
  print('Nota inválida')

# Exercicio 4
num = int(input('Digite a linha desejada: '))
letra = input('Digite a coluna desejada: ')

if ((letra == 'a') or (letra == 'c') or (letra == 'e') or (letra == 'g')) and (num % 2 == 0):
  print('Branco')
elif ((letra == 'b') or (letra == 'd') or (letra == 'f') or (letra == 'h')) and (num % 2 != 0):
  print('Branco')
else:
  print('Preto')
  

# Exercicio 5
ano = int(input('Digite um ano: '))

# Metodo 1
animal = ano % 12

if animal == 1:
  print('%d é o ano do(a) Galo' %ano)
if animal == 1:
  print('%d é o ano do(a) Cachorro' %ano)
if animal == 2:
  print('%d é o ano do(a) Cachorro' %ano)
if animal == 3:
  print('%d é o ano do(a) Porco' %ano)
if animal == 4:
  print('%d é o ano do(a) Rato' %ano)
if animal == 5:
  print('%d é o ano do(a) Boi' %ano)
if animal == 6:
  print('%d é o ano do(a) Tigre' %ano)
if animal == 7:
  print('%d é o ano do(a) Lebre' %ano)
if animal == 8:
  print('%d é o ano do(a) Dragão' %ano)
if animal == 9:
  print('%d é o ano do(a) Cobra' %ano)
if animal == 10:
  print('%d é o ano do(a) Cavalo' %ano)
if animal == 11:
  print('%d é o ano do(a) Carneiro' %ano)
if animal == 12:
  print('%d é o ano do(a) Macaco' %ano)

# Metodo 2
animal = ['Macaco', 'Galo', 'Cachorro', 'Porco', 'Rato', 'Boi', 'Tigre', 'Lebre', 'Dragão', 'Cobra', 'Cavalo', 'Carneiro']

resto = animal[ano % 12]

print('{0} é o ano do(a) {1}'.format(ano, resto))