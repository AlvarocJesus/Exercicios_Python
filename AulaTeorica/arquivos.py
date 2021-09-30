# Escrever um arquivo
""" arquivo = open('teste.txt', 'w')

for linha in range(0,1000):
  arquivo.write('Dado %d\n' %linha)
arquivo.close()

# Ler um arquivo
arquivo = open('./teste.txt', 'r')

lista = arquivo.readlines()
# print(lista)

# for linhs in arquivo.readlines():
for linhs in lista:
  print(linhs)
arquivo.close()

# Criar dois arquivos e ler eles
impares = open('impar.txt', 'w')
pares = open('par.txt', 'w')

for n in range(1000):
  if n % 2 == 0:
    pares.write('%d\n' % n)
  else:
    impares.write('%d\n' % n)
pares.close()
impares.close()

# Leitura e escrita no mesmo codigo
mult4 = open('mult4.txt', 'w')
pares = open('par.txt', 'r')

for n in pares.readlines():
  if int(n) % 4 == 0:
    mult4.write('%s\n' % n)
  
pares.close()
mult4.close()

# Mais de um dado em uma linha
while True:
  contatos = open('contatos.txt', 'a')
  nome = input('Nome: ')
  telefone = input('Telefone: ')
  if nome == '':
    break
  contatos.write('%s %s\n' %(nome, telefone))
contatos.close()

# Ler de dois dados na mesma linha
contatos = open('./contatos.txt', 'r')
# exibe as informacoes de como uma lista
# print(contatos.readlines())
agenda = []

for linha in contatos.readlines():
  # print('Usando strip()', linha.strip())
  print('Usando split()', linha.split(' '))
  agenda.append(linha.strip().split(' '))
agenda[0][0] = 'Ola'
print(agenda)
print(agenda[0][2])

# Exercicio 1
pares = open('pares.txt', 'w')

for par in range(0,1000):
  if par % 2 == 0:
    pares.write('%d\n' %par)
pares.close()

pares = open('pares.txt', 'r')
paresInvertido = open('pares_invertido.txt', 'w')

for i in pares.readlines():
  novo = 998 - int(i)
  paresInvertido.write('%d\n'%novo)

# for i in range(len(lista)-1, -1, -1):
#   novo = 998 - int(i)
#   paresInvertido.write('%d\n'%novo)

pares.close()
paresInvertido.close()

# Exercicio 2
num2 = open('../numeros2.txt', 'r')
numSoma = []
soma = 0

for i in num2.readlines():
  numSoma = i.split()
for num in numSoma:
  soma += int(num)

print(soma)
num2.close()

# Exercicio 3
num = []
num_unicos = []

def listaNum():
  num3 = open('../numeros3.txt', 'r')
  
  for i in num3.readlines():
    num.append(i.strip())
  num3.close()
  
def listaDeUnicos(num):
  for i in range(len(num)):
    if num[i] != num[i-1]:
      num_unicos.append(num[i])
  
  return num_unicos

def novoArquivos(num_unicos):
  unicos = open('numeros3unicos.txt', 'w')
  
  for i in num:
    unicos.write('%d\n' %int(i))
  unicos.close()

listaNum()
listaDeUnicos(num)
novoArquivos(num_unicos) """

# Exercicio 4
import os

def create():
  nome = input('Digite seu nome: ')
  sobrenome = input('Digite seu sobrenome: ')
  telefone = input('Digite seu telefone: ')
  email = input('Digite seu email: ')
  agenda = open(nome+'_'+sobrenome+'.txt', 'w')
  agenda.write('%s %s' %(telefone, email))
  agenda.close()
  print('Contato criado com sucesso!')

def read():
  nome = input('Digite seu nome: ')
  sobrenome = input('Digite seu sobrenome: ')
  agenda = open(nome+'_'+sobrenome+'.txt', 'r')
  print(agenda.readlines())
  agenda.close()

def update():
  nome = input('Digite seu nome: ')
  sobrenome = input('Digite seu sobrenome: ')
  agenda = open(nome+'_'+sobrenome+'.txt', 'w')
  telefone = input('Digite seu novo telefone: ')
  email = input('Digite seu novo email: ')
  agenda.write('%s %s' % (telefone, email))
  print('Contato atualizado com sucesso!')
  agenda.close()

def delete():
  nome = input('Digite seu nome: ')
  sobrenome = input('Digite seu sobrenome: ')
  os.remove(nome+'_'+sobrenome+'.txt')
  print('Contato deletado com sucesso!')

while True:
  print(" 1 - Novo contato\n 2 - Procura (pelo nome)\n 3 - Atualiza contato\n 4 - Apaga contato \n 0 - Sair")
  entrada = int(input('Digite sua opcao: '))
  if entrada == 1:
    create()
  elif entrada == 2:
    read()
  elif entrada == 3:
    update()
  elif entrada == 4:
    delete()
  elif entrada == 0:
    break
