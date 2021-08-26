# Exemplo if aninhado
tempo = int(input('Digite o tempo usado no telefone em minutos: '))

if tempo > 400:
  total = tempo * 0.15

else:
  if tempo < 200: 
    total = tempo * 0.18
  else:
    total = tempo * 0.20
  
print('O valor total a pagar e de: %.2f' %total)

# Exercicio 1
nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))

media = (nota1 + nota2) / 2
print(media)
if media == 10.0:
  print("Aprovado com Distinção")
else:
  if media >= 5.0:
    print("Aprovado")
  else:
    print("Reprovado")

# Exercicio 2
num1 = float(input('Digite um numero: '))
num2 = float(input('Digite outro numero: '))
operacao = input('Digite a operação que deseja realizar: ')

if operacao == 'soma':
  op = num1 + num2
elif operacao == 'subtração':
  op = num1 - num2
elif operacao == 'multiplicação':
  op = num1 * num2
elif operacao == 'divisão':
  op = num1 / num2
else:
  print('Operacao escolhida nao e valida!')
  
print('O resultado da operacao {0} e de: {1:.2f}'.format(operacao, op))

# Exemplo operadores logicos
ano = int(input('Digite um ano: '))

if (ano % 400 == 0) or ((ano % 4 == 0) and (ano % 100 != 0)):
  print('O ano %d e bissexto!' %ano)
else:
  print('O ano %d nao e bissexto!' %ano)
  
# Exercicio 3
x = float(input('Digite um valor x: '))
y = float(input('Digite um valor y: '))

if x > 0 and y > 0:
  print('Os pontos estao no quadrante Q1')
elif x < 0 and y > 0:
  print('Os pontos estao no quadrante Q2')
elif x < 0 and y < 0:
  print('Os pontos estao no quadrante Q3')
elif x > 0 and y < 0:
  print('Os pontos estao no quadrante Q4')
elif x == 0 and y != 0:
  print('Os pontos estao sobre um dos eixos cartesianos')
else:
  print('Os pontos estao na origem (x = y = 0)')

# Exercicio 4
salario = float(input('Digite seu salario: '))

reajuste = 0

if 0 <= salario <= 400.00:
  indice = 15 # -> 15%
elif (salario >= 400.01) and (salario <= 800.00):
  indice = 12 # -> 12%
elif (salario >= 800.01) and (salario <= 1200.00):
  indice = 10 # -> 10%
elif (salario >= 1200.01) and (salario <= 2000.00):
  indice = 7 # -> 7%
else: # Acima de R$ 2000.00
  indice = 4 # -> 4%
  
reajuste = salario * (indice/100)
salarioNovo = salario + reajuste

# indiceReajustado = (((salario+reajuste)/salario)-1)

print('O novo salário e R$ {0:.2f}, o valor de reajuste ganho e R$ {1:.2f} e o indice reajustado foi de {2}%%'.format(salarioNovo, reajuste, indice))

# Exercicio 5
classificacao = 0

ask = input('Telefonou para a vítima?\n')
if ask == 'sim':
  classificacao += 1

ask = input('Esteve no local do crime?\n')
if ask == 'sim':
  classificacao += 1

ask = input('Mora perto da vítima?\n')
if ask == 'sim':
  classificacao += 1

ask = input('Devia para a vítima?\n')
if ask == 'sim':
  classificacao += 1

ask = input('Já trabalhou com a vítima?\n')
if ask == 'sim':
  classificacao += 1

if classificacao == 2:
  print("Suspeita")
elif classificacao == 3 or classificacao == 4:
  print("Cúmplice")
elif classificacao == 5:
  print("Assassino")
else:
  print("Inocente")
  
# Exercicio 6
litrosVendido = float(input('Digite a quantidade de litros vendidos: '))
combustivel = input('Digite o tipo de combustível: ')

precoGasolina = 5.60
precoAlcool = 4.19

if combustivel == 'Álcool':
  if litrosVendido > 0 and litrosVendido <= 20:
    desconto = precoAlcool * (3/100)
  else: # acima de 20 litros
    desconto = precoAlcool * (5/100)
  totalPagar = (precoAlcool * litrosVendido) - desconto
elif combustivel == 'Gasolina':
  if litrosVendido > 0 and litrosVendido <= 20:
    desconto = precoGasolina * (4/100)
  else: # acima de 20 litros
    desconto = precoGasolina * (6/100)
  totalPagar = (precoGasolina * litrosVendido) - desconto
else:
  print('Combustivel invalido')
  
print('O valor a ser pago pelo cliente e de %.2f' %totalPagar)

# Exercicio 7
saque = float(input('Qual o valor do saque: '))

if 10 <= saque <= 1000:
  val100 = saque//100
  saque = saque - (val100*100)
  val50 = saque // 50
  saque = saque - (val50*50)
  val10 = saque // 10
  saque = saque - (val10*10)
  val5 = saque // 5
  saque = saque - (val5*5)
  val1 = saque
  
  print('Notas R$100,00 = ', val100)
  print('Notas R$50,00 = ', val50)
  print('Notas R$10,00 = ', val10)
  print('Notas R$5,00 = ', val5)
  print('Notas R$1,00 = ', val1)
else:
  print('O valor para saque deve ser entre R$ 10 e R$ 1000')