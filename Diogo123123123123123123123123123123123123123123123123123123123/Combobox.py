from tkinter import *
from tkinter.ttk import *
cor1 = 'white'
janela = Tk()
janela.title('Formulário Principal')
janela.geometry('630x500')
cor = '#d1c7ff'
janela.title('Formulário de Cadastro de Cliente')
janela.config(bg=cor)

def obter():
    resultado = combo.get()
    print(resultado)


combo = Combobox (janela, font = 'Arial 15')
combo['values']=(1,2,3,4,'Joao','Maria')
combo.current(0)
combo.place(x=200, y=100)

label = Label(janela, width=15, text='Faça a sua escolha', font=('Arial 12'), anchor='w')
label.place(x=30, y=105)

botao_nome = Button(janela, command=obter, width=15, text='Ver resposta')
botao_nome.place(x=200, y=150)



janela.mainloop()