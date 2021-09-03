# Exercicio 1
## Escreva um programa que faça a contagem regressiva de 10 até 0. O programa deve imprimir cada número da contagem a cada um segundo
""" from time import sleep
x = 10
while x >= 0:
  print(x)
  sleep(1)
  x -= 1 """
  
# Exercicio 2
## Escreva um programa que imprime a tabuada do número digitado pelo usuário.
""" num1 = int(input('Digite um numero para saber a tabuada: '))

i = 0
while i <= 10:
  result = num1 * i
  print('{0} X {1} = {2}'.format(num1, i, result))
  i += 1 """
  
# Exercicio 3
## Faça um programa que solicita um número entre 0 e 10. Mostre uma mensagem de erro caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido. Quando o valor for válido dê a mensagem “número aceito!”
# Dica: Você pode utilizar operadores lógicos (and ou or) na condição do while também!
""" while True:
  num1 = int(input('Digite um numero entre 0 e 10: '))
  if 0 <= num1 <= 10:
    print('número aceito!')
    break
  else:
    print('número recusado, digite novamente!') """

""" num1 = int(input('Digite um numero entre 0 e 10: '))
while num1 < 0 or num1 > 10:
  print('Numero invalido!')
  num1 = int(input('Digite um numero entre 0 e 10: '))
print('Número aceito!') """
    
# Exercicio 4
# Faça um programa que gera 70 vezes um número aleatório entre 1 e 100 e, então, exiba qual foi o maior número gerado e quantas vezes o maior número foi atualizado no seu código.
# Para isso, você deve comparar o número gerado na iteração presente com o maior número armazenado até o momento.
""" from random import randrange

# numero = randrange(1, 101)
maiorNum = 0
num = 0
# exiba qual foi o maior número gerado e quantas vezes o maior número foi atualizado no seu código

for i in range(1, 71):
  numero = randrange(1, 101)
  if numero > maiorNum:
    maiorNum = numero
    num += 1
print('O maior numero gerado foi {0} e a variavel maior numero foi alterada {1}'.format(maiorNum, num)) """
    
# Exercicio 5
# Escreva um programa que calcula a média aritmética de 5 números digitados pelo usuário. Utilize contadores e acumuladores.
""" soma = 0
for i in range(1, 6):
  num = float(input('Digite a nota%d do aluno: ' %i))
  soma = soma + num
  media = soma / 5
  i += 1
print(media) """

# Exercicio 6
# Escreva um programa que leia números digitados pelo usuário. O programa deve ler os números até que 0 (zero) seja digitado. Quando 0 for digitado, o programa deve exibir a quantidade de dígitos que foram digitados, a somatória destes dígitos e a média aritmética.
""" soma = 0
media = 0
i = 0

while True:
  digi = int(input('Digite um numero para somar ou digite 0 para sair: '))
  if digi == 0:
    break
  else:
    i += 1
    soma = soma + digi
    media = soma / i

print('A somatoria: {0} e a media: {1}'.format(soma,media)) """

# Exercicio 7
# Um zoológico em particular determina o preço da entrada com base na idade do visitante. Os visitantes com 2 anos de idade ou menos têm entrada gratuita. Crianças entre 3 e 12 anos pagam R$ 14,00. Idosos com 65 anos ou mais pagam R$ 18,00. A entrada para todos os outros visitantes custa R$ 23,00.
# Crie um programa que comece lendo as idades de todos os visitantes de um mesmo grupo, sendo uma idade informada em cada linha. O usuário digitará uma linha em branco para indicar que não há mais pessoas no grupo. Em seguida, seu programa deve exibir o custo total para o grupo. O custo deve ser exibido usando duas casas decimais
""" total = 0

while True:
  idade = input('Digite sua idade: \n')
  if idade == '':
    break
  idade = int(idade)
  if idade <= 2:
    total += 0
  elif 3 <= idade <= 12:
    total += 14
  elif 12 < idade < 65:
    total += 23
  elif idade >= 65:
    total += 18

print('O custo total do grupo sera R$ %.2f' %total) """

# Exercicio 8
# Escreva um programa que calcule o perímetro de um polígono. Comece recebendo do usuário os valores de x e y para o primeiro ponto do polígono. Em seguida, continue lendo pares de valores x e y até que o usuário insira uma linha em branco para a coordenada x. Cada vez que você lê uma coordenada adicional, você deve calcular a distância até o ponto anterior e adicioná-la ao perímetro. Quando uma linha em branco for inserida para a coordenada x, seu programa deve adicionar a distância do último ponto de volta ao primeiro ponto. Em seguida, ele deve exibir o perímetro total.
import math
perimetro = 0
xInicial = float(input('Digite o x da coordenada: '))
yInicial = float(input('Digite o y da coordenada: '))
xAnterior, yAnterior = xInicial, yInicial

while True:
  x = input('Digite o x da coordenada (em branco para sair): ')
  if (x == ''):
    distancia = math.sqrt(((xAnterior-xInicial)**2) + ((yAnterior-yInicial)**2))
    perimetro += distancia
    break
  x = float(x)
  y = float(input('Digite o y da coordenada: '))
  distancia = math.sqrt(((xAnterior-x)**2) + ((yAnterior-y)**2))
  perimetro += distancia
  xAnterior, yAnterior = x, y
print('O perímetro desse polígono é', perimetro)
  
# Exemplos

# Exemplo 1
# x = 0
# for x in range(11):
#   print(x)
  
# While
# while x <= 10:
#   print(x)
#   x += 1

""" # Exemplo while com if -> insere todos os numeros pares de 0 ate o numero digitado
ultimo = int(input('Digite o ultimo digito da contagem: '))

i = 0

while i <= ultimo:
  if i % 2 == 0:
    print(i)
  i += 1 """

# Exemplo while aninhado
""" tabuada = 1
while tabuada <= 10:
  print()
  print('Tabuada do', tabuada)
  multiplicador = 0
  while multiplicador <= 10:
    print(tabuada, 'X', multiplicador, '=', (tabuada*multiplicador))
    multiplicador += 1
  tabuada += 1 """