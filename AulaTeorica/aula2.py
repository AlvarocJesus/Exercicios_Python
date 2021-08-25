from math import *
# Exercicio 1
""" dias = int(input("digite a quantidade de dias: "))
horas = int(input("digite a quantidade de horas: "))
minutos = int(input("digite a quantidade de minutos: "))
segundos = int(input("digite a quantidade de segundos: "))

total = (dias * 24 *60 *60) + (dias *60 *60) + (minutos * 60) + segundos

print(total) """

# Exercicio 2
""" km = float(input("Digite a quantidade de quilometros percorridos: "))
diasUso = int(input("Digite a quantidade de dias que o carro foi usado: "))

custoTotal = (60 * diasUso) + (0.15 * km)
print("O custo total e de %.2f" %custoTotal) """

# Exercicio 3
""" altura = float(input("Digite sua altura: "))

pesoIdeal = (72.7*altura) - 58
# peso / (altura x altura)
print("Peso ideal %.2f" %pesoIdeal)
print("Peso ideal {0:.2f}".format(pesoIdeal))
print("Peso ideal", round(pesoIdeal,2)) """

# Exercicio 4
""" salarioHora = float(input("Digite quanto voce ganha por hora: "))
horasTrabalhadas = float(input("Digite quantas horas voce trabalha: "))

salarioBruto = salarioHora * horasTrabalhadas
renda = 11/100 # -> 11%
inss = 8/100 # -> 8%
sindicato = 5/100 # -> 5%

descontos = 0.11 + 0.08 + 0.05
pagaINSS = salarioBruto - inss
pagaSindicato = salarioBruto - sindicato
salarioLiquido = salarioBruto - descontos
print("+ Salário Bruto : R$ {0} \n - IR (11%) : R$ {1} \n - INSS (8%) : R$ {2} \n - Sindicato ( 5%) : R$ {3} \n = Salário Liquido : R$ {4}".format(salarioBruto, renda, inss, sindicato, salarioLiquido)) """

# Exercicio 5
""" x = 3
y = (x**3) - abs(log(x))
print(y) """

# Exercicio 6
""" x = 3
w = 3
k = 3
y = x**2 - w**k
print(y) """

# Exercicio 7
""" x = y = 3
k = ((e**2) + sqrt((x+y))) / 3
print(k) """

# Exercicio 8

# Exercicio 9
""" a = 4
b = 10
c = 5.0
d = 1
f = 5
print(a == c)
print(a < b)
print(d < b)
print(c != f)
print(a == b)
print(c < d)
print(b > a)
print(c >= f)
print(f >= c)
print(c <= c)
print(c <= f) """

# Exercicio 10
""" a = int(input("Digite o primeiro numero: "))
b = int(input("Digite o segundo numero: "))

if a > b:
  print("O primeiro numero e maior", a)
if a < b:
  print("O segundo numero e maior", b)
if a == b:
  print("Os dois numeros sao iguais")"""

# Exercicio 11
""" num = float(input("Digite um numero: "))

if num > 0:
  print("O numero %f e positivo" %num)
if num < 0:
  print("O numero %f e negativo" %num) """

# Exercicio 12
""" dia = int(input("Digite um numero de 1 a 7: "))

if dia == 1:
  print("Hoje e Segunda-feira")
if dia == 2:
  print("Hoje e Terca-feira")
if dia == 3:
  print("Hoje e Quarta-feira")
if dia == 4:
  print("Hoje e Quinta-feira")
if dia == 5:
  print("Hoje e Sexta-feira")
if dia == 6:
  print("Hoje e Sabado")
if dia == 7:
  print("Hoje e Domingo") """

# Exercicio 13
""" salario = float(input("Digite seu salario: "))

if salario > 1250.00:
  salarioNovo = salario * (1 + (10/100)) # -> 10%
if salario <= 1250.00:
  salarioNovo = salario * (1 + (15/100)) # -> 15%

print("Novo salario com aumento é de: %.2f" %salarioNovo) """

# Exercicio 14
# Exercicio 15
# Exercicio 16