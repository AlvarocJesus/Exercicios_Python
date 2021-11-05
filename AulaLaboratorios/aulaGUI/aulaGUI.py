from tkinter import *
from tkinter import scrolledtext

window = Tk()
window.title('Busca de palavras suspeitas')
window.geometry('600x500')

def incidenciaPalavras():
  frequency.delete(0, END)
  txt.delete(END, END)
  frequencia = 0
  word = suspectWord.get()
  
  arqWord = []
  arquivo = open('chat.txt', 'r')
  for i in arquivo.readlines():
    arqWord.append(i.strip().split())
  arquivo.close()
  
  for i in range(len(arqWord)):
    for k in range(len(arqWord[i])):
      if word.lower() in arqWord[i][k].lower():
        arqWord[i][-1] = arqWord[i][-1]+'\n\n'
        txt.insert(1.0, ' '.join(arqWord[i]))
        frequencia+=1
  
  frequency.insert(0, frequencia)

label = Label(window, text='Palavra Suspeita:', font=('Arial', 14))
label.place(relx=0.15, rely=0.1, anchor=CENTER)

suspectWord = Entry(window, width=15, font=('Arial', 14))
suspectWord.place(relx=0.41, rely=0.1, anchor=CENTER)

btn = Button(window, text='Pesquisar!', command=incidenciaPalavras)
btn.place(relx=0.63, rely=0.1, anchor=CENTER)

label1 = Label(window, text='Frequência:', font=('Arial', 14))
label1.place(relx=0.15, rely=0.19, anchor=CENTER)

frequency = Entry(window, width=15, font=('Arial', 14))
frequency.place(relx=0.41, rely=0.19, anchor=CENTER)

label1 = Label(window, text='Ocorrências:', font=('Arial', 14))
label1.place(relx=0.15, rely=0.3, anchor=CENTER)

txt = scrolledtext.ScrolledText(window, width=71, height=19)
txt.place(relx=0.5, rely=0.65, anchor=CENTER)

window.mainloop()
