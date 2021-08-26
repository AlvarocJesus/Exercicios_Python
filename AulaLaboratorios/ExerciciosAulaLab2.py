# exercicio 1 -> Certo
idade = input("Digite a faixa etária: ")

if idade == 'Bebê':
  print("menor que 2 anos")
if idade == 'Criança':
  print("de 3 a 10 anos")
if idade == 'Adolescente':
  print("de 11 a 17 anos")
if idade == 'Adulto':
  print("de 18 a 64 anos")
if idade == 'Idoso':
  print("maior que 65 anos")

# Exercicio 2 -> Certo
prod1 = int(input("Digite o valor do primeiro produto: "))
prod2 = int(input("Digite o valor do segundo produto: "))
prod3 = int(input("Digite o valor do terceiro produto: "))

totalCompra = prod1 + prod2 + prod3

if totalCompra > 500.00:
  desconto = totalCompra * (20/100)
  print("Desconto: %.2f" %desconto)
else: # totalCompra < 500.00:
  desconto = totalCompra * (10/100)
  print("Desconto: %.2f" %desconto)

# Exercicio 3 -> Certo
lados = int(input())

if lados == 3 :
  print ("triângulo")
elif lados == 4 :
  print ("quadrado")
elif lados == 5 :
  print ("pentágono")
elif lados == 6 :
  print ("hexágono")
elif lados == 7 :
  print ("heptágono")
elif lados == 8 :
  print ("octógono")
elif lados == 9 :
  print ("eneágono")
elif lados == 10 :
  print ("decágono")
else:
  print('Erro!')

# Exercicio 4
valorCompra = float(input("Digite o valor da compra: "))
parcelas = int(input("Digite a quantidade de parcelas: "))

if valorCompra > 5000:
  extra = 0.05
else:
  extra = 0

if parcelas == 1:
  desconto = valorCompra * (0.10 + extra)
  total = valorCompra - desconto
  valorParcelas = total / parcelas
  
if parcelas == 2 or parcelas == 3:
  desconto = valorCompra * (0.05 + extra)
  total = valorCompra - desconto
  valorParcelas = total / parcelas
  
if parcelas > 3:
  desconto = valorCompra * extra
  total = valorCompra - desconto
  valorParcelas = total / parcelas
  

print("Desconto total: %.2f" %desconto)
print("Valor final da compra com desconto: %.2f" %total)
print("Cada parcela será de: %.2f" %valorParcelas)

# Exercicio 5 -> Certo
from math import *

calc = input("Você deseja calcular o volume do dodecaedro ou icosaedro: ")
aresta = int(input('Digite o valor da aresta a em metros: '))

if calc == "dodecaedro":
  V = ((15 + (7 * sqrt(5))) / 4) * (aresta**3)
  print('O volume de um dodecaedro regular com {0:.2f} de aresta é: {1:.2f}'.format(aresta, V))
  
else:
  V = ((5 / 12) * (3 + sqrt(5))) * (aresta**3)
  print('O volume de um icosaedro regular com {0:.2f} de aresta é: {1:.2f}'.format(aresta, V))

# Exercicio 6 -> Certo
mes = input()

if mes == 'janeiro':
  print('31 dias')
elif mes == 'fevereiro':
  print('28 ou 29 dias')
elif mes == 'março':
  print('31 dias')
elif mes == 'abril':
  print('30 dias')
elif mes == 'maio':
  print('31 dias')
elif mes == 'junho':
  print('30 dias')
elif mes == 'julho':
  print('31 dias')
elif mes == 'agosto':
  print('31 dias')
elif mes == 'setembro':
  print('30 dias')
elif mes == 'outubro':
  print('31 dias')
elif mes == 'novembro':
  print('30 dias')
else:
  print('31 dias')

# Exercicio 7 -> Certo
ovo = float(input('Digite a medida do ovo: '))

if ovo < 30:
  print('pequeno')
else:
  print('grande')

# Exercicio 8 -> Certo
vazao = float(input('Digite a vazão da bomba em l/s: '))
capacidade = int(input('Digite a capacidade do reservatório: '))

total =  capacidade / vazao

resHora = total % 3600
hora = (total - resHora) / 3600

total = total - (hora*3600)
resMinuto = total % 60
minuto = (total - resMinuto) / 60

total = total - (minuto*60)
resSeg = total % 60
seg = total

print('Tempo necessário para encher o reservatório: {0:.0f}:{1:.0f}:{2:.0f}'.format(hora, minuto, resSeg))