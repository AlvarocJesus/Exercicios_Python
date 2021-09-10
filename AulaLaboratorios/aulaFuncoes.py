# Exercicio 1
# Escreva uma função que tenha os comprimentos dos dois lados mais curtos de um triângulo retângulo como seus parâmetros. Retorne a hipotenusa do triângulo, calculada usando o teorema de Pitágoras, como o resultado da função. Inclua um programa principal que lê os comprimentos dos lados mais curtos de um triângulo retângulo do usuário e use sua função para calcular o comprimento da hipotenusa
from math import *

ca = int(input('Digite o primeiro lado do triângulo: '))
co = int(input('Digite o segundo lado do triângulo: '))


def calculaHipotenusa(ca, co):
    h = sqrt((ca**2) + (co**2))
    return h


print('Hipotenusa: %.2f' % calculaHipotenusa(ca, co))

# Exercicio 2
# Escreva a função media() que recebe três números como parâmetros e retorna o valor médio desses parâmetros como seu resultado. Escreva somente a função solicitada; não é necessário o programa principal.
num1 = float(input(''))
num2 = float(input(''))
num3 = float(input(''))


def media(num1, num2, num3):
    soma = num1 + num2 + num3
    media = soma / 3
    return media


print("Média: %.2f" % media(num1, num2, num3))

# Exercicio 3
# Crie uma função chamada produtorio que realize o cálculo do produtório, conforme equação abaixo:
# Sua função deverá receber entre 3 e 6 parâmetros e retornar o valor do produtório. Não é necessário fazer o programa principal.
# Produtório é a multiplicação de uma sequência de objetos matemáticos(números, funções, vetores, matrizes, etc.).


def produtorio(num1, num2, num3, num4=1, num5=1, num6=1):
    produto = num1 * num2 * num3 * num4 * num5 * num6
    return produto


print(produtorio(2, 2, 2))

# Exercicio 4
# Em uma determinada jurisdição, as tarifas de táxi consistem em uma tarifa básica de R$ 10.00, mais R$ 0.50 para cada 125 metros percorridos. Escreva uma função que considere a distância percorrida (em quilômetros inteiros) como seu único parâmetro e retorne a tarifa total como seu único resultado. Escreva um programa principal em que a quantidade de km será digitada e onde a função será chamada.
kmPercorridos = int(input('Digite a quantidade de quilômetros: '))


def main(kmPercorridos):
    taxaVaria = (0.5 * ((kmPercorridos*1000) / 125))
    total = 10 + taxaVaria
    return total


print('Tarifa %.2f' % main(kmPercorridos))

# Exercicio 5
# Crie uma função para calcular e retornar o peso de uma pessoa nos outros planetas do Sistema Solar. A função deve ter dois parâmetros: o planeta desejado e o peso em Kg da pessoa na Terra. O programa principal deve receber o peso da pessoa na Terra (em Kg) e o planeta desejado.
planeta = input('Digite o o nome do planeta desejado: ')
peso = float(input('Digite o peso da pessoa na Terra em kg: '))


def pesoPessoa(planeta, peso):
    if planeta == 'Mercúrio':
        pesoPlaneta = peso * 0.37
    elif planeta == 'Vênus':
        pesoPlaneta = peso * 0.88
    elif planeta == 'Marte':
        pesoPlaneta = peso * 0.38
    elif planeta == 'Júpiter':
        pesoPlaneta = peso * 2.64
    elif planeta == 'Saturno':
        pesoPlaneta = peso * 1.15
    elif planeta == 'Urano':
        pesoPlaneta = peso * 1.17
    elif planeta == 'Netuno':
        pesoPlaneta = peso * 1.18
    return pesoPlaneta


print('Peso em {0}: {1:.2f}' .format(planeta, pesoPessoa(planeta, peso)))

# Exercicio 6
# Escreva uma função, test_prime() que recebe um número e verifica se ele é primo ou não. A função retorna True ou False. Não é necessário desenvolver o programa principal.
num = int(input("Digite o número desejado: "))


def test_prime(num):
    cont = 0
    i = 0
    while i <= num or cont < 2:
        i = i + 1
        x = num % i
        if x == 0:
            cont = cont + 1
    if cont <= 2:
        return True
    else:
        return False


print(test_prime(num))

# Exercicio 7
# Escreva uma função que recebe a latitude e a longitude de dois pontos(latitude e longitude do ponto A, latitude e longitude do ponto B) como valores float.  Essa função deve calcular e imprimir a distância em km entre os dois pontos. Utilize os métodos radians, sin, cos e acos do módulo math para auxiliar nos cálculos. A distância é calculada conforma equação:

# dist = 6371.01∗acos(sin(latitude1)∗sin(latitude2)+cos(latitude1)∗cos(latitude2)∗cos(longitude1−longitude2))

# Faça o programa principal que recebe os valores das duas latitudes e das duas longitudes e chama a função.
latitude1 = radians(float(input('Digite a latitude A: ')))
longitude1 = radians(float(input('Digite a longitude A: ')))
latitude2 = radians(float(input('Digite a latitude B: ')))
longitude2 = radians(float(input('Digite a longitude B: ')))


def distancia(latitude1, longitude1, latitude2, longitude2):
    dist = 6371.01*acos(sin(latitude1)*sin(latitude2) +
                        cos(latitude1)*cos(latitude2)*cos(longitude1-longitude2))
    return dist


print('A distância é %.2fkm.' % distancia(
    latitude1, longitude1, latitude2, longitude2))
