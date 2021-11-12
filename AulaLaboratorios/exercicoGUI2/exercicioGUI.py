import os
from tkinter import *
from tkinter import messagebox
from datetime import date
from random import randrange

window=Tk()
window.title('Busca de palavras suspeitas')
window.geometry('500x400')

def criarUsuario():
  id = []
  for i in range(5):
    id.append(str(randrange(9)))
  print(id)
  cpf = entryCpf.get()
  nome = entryName.get()
  dataNascimento = entrydataNascimento.get().replace('-', '/').split('/')
  endereco = entryendereco.get()
  profissao = entryprofissao.get()
  
  idade = date.today().year - int(dataNascimento[-1])
  
  if os.path.isfile('./database/'+cpf+'.txt'):
    messagebox.showinfo('Aviso', 'Usuário ja cadastrado!')
  else:
    user = open('./database/'+cpf+'.txt', 'w')
    user.write(f'ID: {"".join(id)}\n')
    user.write(f'Nome: {nome}\n')
    user.write(f'Data de Nascimento: {dataNascimento}\n')
    user.write(f'Idade: {idade}\n')
    user.write(f'Endereço: {endereco}\n')
    user.write(f'Profissão: {profissao}\n')
    messagebox.showinfo('Aviso', 'Usuário cadastrado com sucesso!')
    user.close()


cpf = Label(window, text='CPF:', font=('Arial', 14))
cpf.place(relx=0.25, rely=0.15, anchor=CENTER)

name = Label(window, text='Nome:', font=('Arial', 14))
name.place(relx=0.25, rely=0.25, anchor=CENTER)

dataNascimento = Label(window, text='Data de Nascimento:\ndd/mm/aaaa ou dd-mm-aaaa', font=('Arial', 14))
dataNascimento.place(relx=0.25, rely=0.35, anchor=CENTER)

endereco = Label(window, text='Endereço:', font=('Arial', 14))
endereco.place(relx=0.25, rely=0.5, anchor=CENTER)

profissao = Label(window, text='Profissão:', font=('Arial', 14))
profissao.place(relx=0.25, rely=0.65, anchor=CENTER)

# *Entry
entryCpf = Entry(window, width=15, font=('Arial', 14))
entryCpf.place(relx=0.7, rely=0.15, anchor=CENTER)

entryName = Entry(window, width=15, font=('Arial', 14))
entryName.place(relx=0.7, rely=0.25, anchor=CENTER)

entrydataNascimento = Entry(window, width=15, font=('Arial', 14))
entrydataNascimento.place(relx=0.7, rely=0.35, anchor=CENTER)

entryendereco = Entry(window, width=15, font=('Arial', 14))
entryendereco.place(relx=0.7, rely=0.5, anchor=CENTER)

entryprofissao = Entry(window, width=15, font=('Arial', 14))
entryprofissao.place(relx=0.7, rely=0.65, anchor=CENTER)

btn = Button(window, text='Cadastrar', command=criarUsuario)
btn.place(relx=0.48, rely=0.8, anchor=CENTER)

window.mainloop()
