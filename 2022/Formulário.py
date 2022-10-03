from tkinter import *
from tkinter.ttk import *
cor1 = 'white'
janela = Tk()
janela.title('Formulário Principal')
janela.geometry('630x500')
cor = '#d1c7ff'
janela.title('Formulário de Cadastro de Cliente')
janela.config(bg=cor)


import webbrowser

combo = Combobox (janela)
combo['values']=('Angola','Brasil','Portugal')
combo.current(0)
combo.place(x=200, y=100)

codigo = Label(janela, width=20,height=2, text='Código:',font='Arial 12', relief='solid', fg='black', bg='#d1c7ff')
codigo.place(x=0, y=80)

nome = Label(janela, width=20,height=2, text='Nome:',font='Arial 12', relief='solid', fg='black', bg='#d1c7ff')
nome.place(x=0, y=120)

estado = Label(janela, width=20,height=2, text='Estado:',font='Arial 12', relief='solid', fg='black', bg='#d1c7ff')
estado.place(x=0, y=160)

cidade = Label(janela, width=20,height=2, text='Cidade:',font='Arial 12', relief='solid', fg='black', bg='#d1c7ff')
cidade.place(x=0, y=200)

bairro = Label(janela, width=20,height=2, text='Bairro:',font='Arial 12', relief='solid', fg='black', bg='#d1c7ff')
bairro.place(x=0, y=240)

logradouro = Label(janela, width=20,height=2, text='Logradouro:',font='Arial 12', relief='solid', fg='black', bg='#d1c7ff')
logradouro.place(x=0, y=280)

complemento = Label(janela, width=20,height=2, text='Complemento:',font='Arial 12', relief='solid', fg='black', bg='#d1c7ff')
complemento.place(x=0, y=320)


cadastro = Label(janela, width=20,height=2, text='Cadastro de Cliente', font= 'Arial 15', relief='flat', bg='#d1c7ff')
cadastro.place(x=220, y=0)

#estilos botao - groove-solid-flat-sunken-ridge
consultar = Button(janela, width=10, text="Consultar", relief='solid', fg='black', bg='white')
consultar.place(x=496, y=65)

novo = Button(janela, width=10, text="Novo", relief='solid', fg='black', bg='white')
novo.place(x=300, y=450)

salvar = Button(janela, width=10, text="Salvar", relief='solid', fg='black', bg='white')
salvar.place(x=496, y=450)

apagar = Button(janela, width=10, text="Apagar", relief='solid', fg='black', bg='white')
apagar.place(x=400, y=450)


codigo = Entry(janela, width=20,  font = "arial 15", relief='solid')
codigo.place(x=200, y=87)

nome = Entry(janela, width=34,  font = "arial 15", relief='solid')
nome.place(x=200, y=128)

estado = Entry(janela, width=23,  font = "arial 15", relief='solid')
estado.place(x=200, y=170)

cidade = Entry(janela, width=34,  font = "arial 15", relief='solid')
cidade.place(x=200, y=205)

bairro = Entry(janela, width=34,  font = "arial 15", relief='solid')
bairro.place(x=200, y=247)

logradouro = Entry(janela, width=34,  font = "arial 15", relief='solid')
logradouro.place(x=200, y=285)

complemento = Entry(janela, width=23,  font = "arial 15", relief='solid')
complemento.place(x=200, y=327)

janela.mainloop()