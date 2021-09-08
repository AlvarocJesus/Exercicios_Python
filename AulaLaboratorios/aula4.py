# Exercicio 1
# Faça um programa que leia uma quantidade de números que será digitada pelo usuário. Em seguida, digite todos os números, conforme quantidade digitada, e informe o maior deles.
""" entrada = int(input('Entre com a quantidade de números que serão digitados: '))
entrada1 = int(input('1º número : '))
count = 2
for i in range(1, (entrada)):
  x = int(input('{0}º número : '.format(count)))
  # maior = x
  if x > entrada1:
    entrada1 = x
  count += 1
print('Maior número digitado:', entrada1) """

# Exercicio 2
""" tempMin = int(input('Digite o valor mínimo em graus C: '))
tempMax = int(input('Digite o valor máximo em graus C: '))

print('%18s %18s' %('Temperatura em C', 'Temperatura em F'))
for i in range(tempMin, (tempMax+5), 5):
  print('%18d %18d' %(i, i*9/5+32)) """

# Exercicio 3
""" ano = int(input('Digite o ano desejado: '))

if ano < 2007:
  print('Digite um ano maior que 2007')
else:
  salario = (5000*1.015)*1.030
  aumento = 0.03
  z = ano - 2007
  
  while z > 0:
    aumento *= 2
    salario *= (aumento+1)
    z -= 1
print('Salário de %d: R$ %.2f' %(ano, salario)) """

# Exercicio 4
""" num = int(input('Digite o número desejado: '))
E = 1

for i in range(1, (num+1)):
  E += 1/i
print('%.3f' %E) """

# Exercicio 5
""" n = int(input("Digite o número desejado: "))
cont = 0
i = 0

while i <= n or cont < 2:
    i = i + 1
    x = n % i
    if x == 0:
        cont = cont + 1

if cont <= 2:
    print("Número primo")
else:
    print("Número não primo") """

# Exercicio 6
""" n = int(input("Digite n: "))
m = int(input("Digite m: "))
d = 1

divisor  = 2
while divisor <= n:
  if n % divisor == 0 and m % divisor == 0:
    d = divisor
  divisor += 1 

print("%d" %(d)) """

n = int(input("Digite n: "))
m = int(input("Digite m: "))

if (n > 0) and (m > 0):
  print()

# Exercicio 7
""" x = int(input('Digite o número desejado: '))

palpite = x/2
erro = abs(((palpite**2) - x))

while erro > (10**(-12)):
  palpite = (palpite + (x/palpite)) / 2
  erro = (palpite**2) - x
print('%.3f' %palpite) """