# Exemplo
# Fazer uma função que retorne True ou False para a verificação de números pares.
def verificacaoPar(num):
    return (num % 2 == 0)
# print(verificacaoPar(4))


def imparOuPar(x):
    if verificacaoPar(x) == True:
        return 'par!'
    else:
        return 'impar!'


print(imparOuPar(4))
print(imparOuPar(3))
print(imparOuPar(56))

# Exercicio 1
# Escreva uma função com parâmetros que retorne o maior de dois números. A função deve se chamar maximo(x, y).


def maximo(x, y):
    if x > y:
        return x
    else:
        return y


print(maximo(2, 1))

# Exercicio 2
# Escreva uma função com parâmetros chamada multiplo(x, y). Esta função deve receber dois números e retornar True se o primeiro for múltiplo do segundo número; a função retorna False caso contrário.


def multiplo(x, y):
    if x % y == 0:
        return True
    else:
        return False


print(multiplo(15, 2))


# Exercicio 3
# Escreva uma função com parâmetros que receba a base e a altura de um triângulo e retorne sua área (A = base * altura / 2).
def area(base, altura):
    A = base * altura / 2
    return A


print(area(5, 5))

# Exercicio 4
# Uma data é considerada mágica quando o dia multiplicado pelo mês é igual ao ano de dois dígitos. Por exemplo, 10 de junho de 1960 é uma data mágica porque junho é o sexto mês e 6 vezes 10 é 60, o que equivale ao ano de dois dígitos. Escreva uma função que determine se uma data é ou não uma data mágica. Use sua função em um programa que deve encontrar e exibir todas as datas mágicas do século XX.
dia = int(input('Dia:'))
mes = int(input('Mes:'))
ano = int(input('Ano:'))


def dataMagica(dia, mes, ano):
    magica = dia * mes
    if magica == ano % 100:
        return 'E uma data magica'
    else:
        return 'Nao e uma data magica'


print(dataMagica(dia, mes, ano))

# Exercicio 5
# Existem restrições para que uma pessoa possa doar sangue. Uma delas é relativa ao peso. Mulheres tem que pesar no mínimo 50kg e homens no mínimo 60kg. Faça uma função para informar se uma pessoa está ou não apta a doar sangue sabendo seu sexo e seu peso.
# O programa principal deve ler as entradas, acionar a função e exibir a resposta.
sexo = input('Digite seu sexo: ')
peso = float(input('Digite seu peso: '))


def doarSangue(sexo, peso):
    if sexo == 'Feminino':
        if peso >= 50:
            return 'apta a doar sangue'
        else:
            return 'nao apta a doar sangue'
    elif sexo == 'Masculino':
        if peso >= 60:
            return 'apto a doar sangue'
        else:
            return 'nao apto a doar sangue'


print(doarSangue(sexo, peso))

# Exercicio 6
# Refaça os exercícios 1, 2 e 3 utilizando função lambda.
# 6.1


def maximo(x, y): return x if x > y else y


maximo(10, 8)
# 6.2
def multiplo(x, y): return x % y == 0


print(multiplo(15, 2))
# 6.3
def area(base, altura): return base * altura / 2


print(area(5, 5))

# Exercicio 7
# Escreva uma função que calcula o quociente e o resto da divisão inteira entre dois números. Utilize apenas as operações de soma e subtração para calcular o resultado. Dica: utilize uma estrutura de repetição para isso.
# Faça um programa principal que recebe o dividendo e o divisor do usuário e, depois de chamar a função, exibe o quociente e o resto.

dividendo = float(input('Digite o valor do dividendo: '))
divisor = float(input('Digite o valor do divisor: '))
quociente = 0
x = dividendo
while x >= divisor:
    x = x - divisor
    quociente = quociente + 1
resto = x
print('quociente', quociente, 'resto da divisao', resto)

# Exercicio 8
# Faça uma função que receba quatro valores: I, A, B e C. Destes Valores, I é um valor inteiro valendo 1, 2 ou 3. A, B e C são valores reais. Escreva os números A, B e C obedecendo à tabela a seguir, dependendo do valor de I
I = int(input('Digite 1, ou 2, ou 3: '))
a = float(input('Digite um valor para A: '))
b = float(input('Digite um valor para B: '))
c = float(input('Digite um valor para C: '))

if I == 1:
    if (a > b) and (a > c) and (b > c):
        print(a, b, c)
    if (b > a) and (b > c) and (a > c):
        print(b, a, c)
    if (c > a) and (c > b) and (b > a):
        print(c, b, a)
elif I == 2:
    if (a < b) and (a < c) and (b < c):
        print(c, b, a)
    if (b < a) and (b < c) and (a < c):
        print(c, a, b)
    if (c < a) and (c < b) and (b < a):
        print(a, b, c)
elif I == 3:
    if (a > b) and (a > c) and (b > c):
        print(b, a, c)
    if (b > a) and (b > c) and (a > c):
        print(a, b, c)
    if (c > a) and (c > b) and (b > a):
        print(b, c, a)
else:
    print('Numero de I e invalido')

# Exercicio 9
# Escreva uma função chamada exponencial que recebe um valor n como parâmetro. Sua função deve encontrar e retornar b e k tal que b**k = n e b seja o menor possível.
n = int(input('Digite um numero: '))


def exponencial(n):
    b = 2
    k = 0
    while b <= n:
        if (b**k == n):
            break
        elif b**k > n:
            b += 1
            k = 0
        else:
            k += 1
    return b, k


print(exponencial(n))
