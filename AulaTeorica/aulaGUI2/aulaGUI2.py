import os
from tkinter import *
from tkinter import messagebox, Menu, scrolledtext, Checkbutton
from datetime import datetime

# Exercicio 1
""" window = Tk()
window.title('Algoritmos')
window.geometry('350x200')

hora = Label(window, font=('Arial', 14), foreground='purple')
hora.place(relx=0.5, rely=0.5, anchor=CENTER)

data = Label(window, font=('Arial', 14), foreground='purple')
data.place(relx=0.5, rely=0.7, anchor=CENTER)

def countDown():
  hora['text'] = datetime.today().strftime('%H:%M:%S')
  data['text'] = datetime.today().strftime('%d / %M / %Y')
  window.after(1000, countDown)

countDown()
window.mainloop() """

# Exercicio 2
window = Tk()
window.title('Algoritmos')
window.geometry('500x400')

def newWindow():
  window = Tk()
  window.title('Algoritmos')
  window.geometry('600x500')
  
  placa = Label(window, text='Placa:', font=('Arial', 12))
  placa.place(relx=0.25, rely=0.15, anchor=CENTER)
  
  entryPlaca = Entry(window, width=15, font=('Arial', 12))
  entryPlaca.place(relx=0.5, rely=0.15, anchor=CENTER)
  
  txt = scrolledtext.ScrolledText(window, width=71, height=19)
  txt.place(relx=0.5, rely=0.65, anchor=CENTER)
  
  def buscarVeiculo():
    placa=entryPlaca.get()
    lista=[]
    veiculo = open('./database/'+placa+'.txt', 'r')
      
    for i in veiculo.readlines():
      lista.append(i.strip().split())
      
    for i in range(len(lista)):
      lista[i][-1] = lista[i][-1]+'\n'
        
      txt.insert(1.0, ' '.join(lista[i]))

    veiculo.close()

  btn = Button(window, text='Buscar Veiculo', command=buscarVeiculo)
  btn.place(relx=0.5, rely=0.25, anchor=CENTER)
  

menu = Menu(window)
menu.add_command(label='Buscar Veiculo', command=newWindow)


def criarVeiculo():
  marcaVeiculo = entryMarcaVeiculo.get()
  modelo = entryModelo.get()
  anoFabricacao = entryAnoFabricacao.get()
  placa = entryPlaca.get()
  km = entryKm.get()
  acessorios = []

  if chk_state_arCondicionado.get() == True:
    acessorios.append('Ar Condicionado')
    if chk_state_DirecaoHidraulica.get() == True:
      acessorios.append('Direcao Hidraulica')
      if chk_state_radio.get() == True:
        acessorios.append('Radio')
        if chk_state_airBag.get() == True:
          acessorios.append('AirBag')

  if os.path.isfile('./database/'+placa+'.txt'):
    messagebox.showinfo('Aviso', 'Veiculo ja cadastrado!')
  else:
    veiculo = open('./database/'+placa+'.txt', 'w')
    veiculo.write(f'Marca do veículo: {"".join(marcaVeiculo)}\n')
    veiculo.write(f'Modelo: {modelo}\n')
    veiculo.write(f'Ano de fabricação: {anoFabricacao}\n')
    veiculo.write(f'Placa: {placa}\n')
    veiculo.write(f'Km: {km}\n')
    veiculo.write(f'acessorios: {", ".join(acessorios)}\n')
    messagebox.showinfo('Aviso', 'Veiculo cadastrado com sucesso!')
    veiculo.close()


chk_state_arCondicionado=BooleanVar()
chk_state_DirecaoHidraulica=BooleanVar()
chk_state_radio=BooleanVar()
chk_state_airBag=BooleanVar()

chk_state_arCondicionado.set(False)
chk_state_DirecaoHidraulica.set(False)
chk_state_radio.set(False)
chk_state_airBag.set(False)

chk_arCondicionado = Checkbutton(window, text='Ar Condicionado', variable=chk_state_arCondicionado)
chk_arCondicionado.place(relx=0.25, rely=0.7, anchor=CENTER)

chk_DirecaoHidraulica = Checkbutton(window, text='Direção Hidraulica', variable=chk_state_DirecaoHidraulica)
chk_DirecaoHidraulica.place(relx=0.25, rely=0.65, anchor=CENTER)

chk_radio = Checkbutton(window, text='Radio', variable=chk_state_radio)
chk_radio.place(relx=0.65, rely=0.65, anchor=CENTER)

chk_airBag = Checkbutton(window, text='AirBag', variable=chk_state_airBag)
chk_airBag.place(relx=0.55, rely=0.7, anchor=CENTER)



cpf = Label(window, text='Marca do veículo:', font=('Arial', 12))
cpf.place(relx=0.25, rely=0.1, anchor=CENTER)

name = Label(window, text='Modelo:', font=('Arial', 12))
name.place(relx=0.25, rely=0.15, anchor=CENTER)

dataNascimento = Label(
    window, text='Ano de fabricação:\ndd/mm/aaaa ou dd-mm-aaaa', font=('Arial', 12))
dataNascimento.place(relx=0.25, rely=0.25, anchor=CENTER)

endereco = Label(window, text='Placa:', font=('Arial', 12))
endereco.place(relx=0.25, rely=0.4, anchor=CENTER)

profissao = Label(window, text='Km:', font=('Arial', 12))
profissao.place(relx=0.25, rely=0.5, anchor=CENTER)

# *Entry
entryMarcaVeiculo = Entry(window, width=15, font=('Arial', 12))
entryMarcaVeiculo.place(relx=0.7, rely=0.1, anchor=CENTER)

entryModelo = Entry(window, width=15, font=('Arial', 12))
entryModelo.place(relx=0.7, rely=0.15, anchor=CENTER)

entryAnoFabricacao = Entry(window, width=15, font=('Arial', 12))
entryAnoFabricacao.place(relx=0.7, rely=0.25, anchor=CENTER)

entryPlaca = Entry(window, width=15, font=('Arial', 12))
entryPlaca.place(relx=0.7, rely=0.4, anchor=CENTER)

entryKm = Entry(window, width=15, font=('Arial', 12))
entryKm.place(relx=0.7, rely=0.5, anchor=CENTER)

btn = Button(window, text='Cadastrar veiculo', command=criarVeiculo)
btn.place(relx=0.48, rely=0.8, anchor=CENTER)

window.config(menu=menu)
window.mainloop()
