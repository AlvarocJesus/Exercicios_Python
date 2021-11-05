""" from tkinter import *
from tkinter import messagebox

janela = Tk()

janela.title("Algoritmos")
janela.geometry('400x400')

# Texto
rotulo = Label(janela, text='Primeira aplicacao grafica no Python!', font=('Arial Bold', 14))
rotulo.place(x=200, y=100, anchor=CENTER)

# Botao conectado com uma funcao
def clique():
  rotulo['text'] = entrada.get()

btn = Button(janela, text='Clique!', command=clique)
btn.place(relx=0.5, rely=0.5, anchor=CENTER)

# Botao sem utilidade
btn = Button(janela, text='Clique2!')
btn.place(x=100, y=50, anchor=CENTER)

# Caixa de texto
entrada = Entry(janela, width=14, font=('Arial Bold', 14))
entrada.place(x=200, y=50, anchor=CENTER)

# Caixa de mensagem
# info message
def show():
  res = messagebox.showinfo('Aviso', 'O botao de mensagem foi criado!!! ;-)')
  print(res)
botao=Button(janela, text='Mensagem', command=show)
botao.place(x=100, y=50, anchor=CENTER)

# askyesno message
def show():
  res = messagebox.askyesno('Sim ou Nao!', 'Python e legal?')
  print(res)
botao = Button(janela, text='Mensagem', command=show)
botao.place(x=100, y=50, anchor=CENTER)

# info message
def show():
  res = messagebox.askquestion('Sim ou Nao!', 'Python e legal?')
  res = messagebox.askyesnocancel('Sim ou Nao!', 'Python e legal?')
  res = messagebox.askokcancel('Sim ou Nao!', 'Python e legal?')
  res = messagebox.askretrycancel('Sim ou Nao!', 'Python e legal?')
  print(res)
botao = Button(janela, text='Mensagem', command=show)
botao.place(x=100, y=50, anchor=CENTER)

janela.mainloop() 
# Exemplo somar dois numeros
from tkinter import *

janela = Tk()

janela.title("Soma")
janela.geometry('600x400')

rotulo = Label(janela, text='Entre o primeiro numero:', font=('Arial Bold', 14))
rotulo.place(relx=0.5, rely=0.2, anchor=CENTER)

rotulo1 = Label(janela, text='Entre o segundo numero:', font=('Arial Bold', 14))
rotulo1.place(relx=0.5, rely=0.4, anchor=CENTER)

rotulo2 = Label(janela, text='Resultado:', font=('Arial Bold', 14))
rotulo.place(relx=0.5, rely=0.6, anchor=CENTER)

entrada = Entry(janela, width=10, font=('Arial Bold', 14))
entrada.place(relx=0.55, rely=0.2, anchor=CENTER)

entrada1 = Entry(janela, width=10, font=('Arial Bold', 14))
entrada1.place(relx=0.55, rely=0.4, anchor=CENTER)

entrada2 = Entry(janela, width=10, font=('Arial Bold', 14))

entrada2.place(relx=0.55, rely=0.6, anchor=CENTER)

def clique():
  entrada2.delete(0, END)
  valor1 = int(entrada.get())
  valor2 = int(entrada1.get())
  soma = valor1+valor2
  entrada2.insert(0, soma)

def clique():
  entrada.delete(0, END)
  entrada1.delete(0, END)
  entrada2.delete(0, END)

btn = Button(janela, text='Soma', font=('Arial', 16), command=clique)
btn.place(relx=0.5, rely=0.8, anchor=CENTER)

btn = Button(janela, text='Soma', font=('Arial', 16), command=clique)
btn.place(relx=0.6, rely=0.8, anchor=CENTER)

janela.mainloop()  """

""" -------------------------------------------------  """
""" # Exercicio 1
from tkinter import *

window = Tk()
window.title('Conversão numérica')
window.geometry('600x300')

label = Label(window, text='Numero decimal:', font=('Arial', 14))
label.place(relx=0.4, rely=0.3, anchor=CENTER)

entrada = Entry(window, width=10, font=('Arial', 12))
entrada.place(relx=0.6, rely=0.3, anchor=CENTER)

labelResposta = Label(window, text='Numero decimal:', font=('Arial', 14))
labelResposta.place(relx=0.4, rely=0.7, anchor=CENTER)
resposta = Entry(window, width=10, font=('Arial', 12))
resposta.place(relx=0.6, rely=0.7, anchor=CENTER)

def convBin():
  resposta.delete(0, END)
  valor = int(entrada.get())
  convertido = format(valor, 'b')
  resposta.insert(0, convertido)

def convHexa():
  resposta.delete(0, END)
  valor = int(entrada.get())
  convertido = format(valor, 'X')
  resposta.insert(0, convertido)

def convOctal():
  resposta.delete(0, END)
  valor = int(entrada.get())
  convertido = format(valor, 'o')
  resposta.insert(0, convertido)

binario = Button(window, text='Binario', font=('Arial', 14), command=convBin)
binario.place(relx=0.3, rely=0.5, anchor=CENTER)

hexa = Button(window, text='Hexadecimal', font=('Arial', 14), command=convHexa)
hexa.place(relx=0.5, rely=0.5, anchor=CENTER)

octa = Button(window, text='Octal', font=('Arial', 14), command=convOctal)
octa.place(relx=0.7, rely=0.5, anchor=CENTER)

window.mainloop() 
# Exercicio 2
from tkinter import *
from tkinter import messagebox

window = Tk()
window.title('Vogal ou Consoante')
window.geometry('600x300')

label = Label(window, text='Digite uma letra:', font=('Arial', 14))
label.place(relx=0.3, rely=0.2, anchor=CENTER)

entrada = Entry(window, width=10, font=('Arial', 12))
entrada.place(relx=0.6, rely=0.2, anchor=CENTER)

def confirma():
  letra = entrada.get()
  if (letra == 'a') or (letra == 'e') or (letra == 'i') or (letra == 'o') or (letra == 'u'):
    res = messagebox.showinfo('Aviso', 'Essa letra é uma vogal')
  elif letra == 'y':
    res = messagebox.showinfo(
        'Aviso', 'Essa letra, em algumas línguas, pode ser considerada como uma vogal e, em outras, como uma consoante.')
  else:
    res = messagebox.showinfo('Aviso', 'Essa letra é uma consoante.')
  
  if res:
    entrada.delete(0, END)

btn = Button(window, text='Verificar', font=('Arial', 14), command=confirma)
btn.place(relx=0.5, rely=0.5, anchor=CENTER)

window.mainloop() """

# Exercicio 3
from tkinter import *

window = Tk()
window.title('Calculadora')
window.geometry('600x600')

entrada = Entry(window, width=58, font=('Arial', 14))
entrada.place(relx=0.5, rely=0.2, anchor=CENTER)

tecla = Button(window, text='0', font=('Arial', 14))
tecla.place()

tecla1 = Button(window, text='1', font=('Arial', 14))
tecla.place()

tecla2 = Button(window, text='2', font=('Arial', 14))
tecla.place()

tecla3 = Button(window, text='3', font=('Arial', 14))
tecla.place()

tecla4 = Button(window, text='4', font=('Arial', 14))
tecla.place()

tecla5 = Button(window, text='5', font=('Arial', 14))
tecla.place()

tecla6 = Button(window, text='6', font=('Arial', 14))
tecla.place()

tecla7 = Button(window, text='7', font=('Arial', 14))
tecla.place()

tecla8 = Button(window, text='8', font=('Arial', 14))
tecla.place()

tecla9 = Button(window, text='9', font=('Arial', 14))
tecla.place()

teclaIgual = Button(window, text='=', font=('Arial', 14))
tecla.place()

teclaSeno = Button(window, text='sen', font=('Arial', 14))
tecla.place()

teclaCos = Button(window, text='cos', font=('Arial', 14))
tecla.place()

teclaTg = Button(window, text='tg', font=('Arial', 14))
tecla.place()

teclaMais = Button(window, text='+', font=('Arial', 14))
tecla.place()

teclaMenos = Button(window, text='-', font=('Arial', 14))
tecla.place()

teclaMult = Button(window, text='x', font=('Arial', 14))
tecla.place()

teclaDiv = Button(window, text='/', font=('Arial', 14))
tecla.place()

teclaExp = Button(window, text='^', font=('Arial', 14))
tecla.place()

teclaRaiz = Button(window, text='√', font=('Arial', 14))
tecla.place()

clear = Button(window, text='C', font=('Arial', 14))
tecla.place()

window.mainloop()
