from tkinter import *
cor1 = 'white'
janela = Tk()
janela.title('Formulário Principal')
janela.geometry('630x500')
cor = '#d1c7ff'
janela.title('Formulário de Cadastro de Cliente')
janela.config(bg=cor)

def obter():
    resultado = selecionando_1.get()
    print(resultado)

selecionando_1 = IntVar()

radio_1 = Radiobutton(janela, command=obter, text='Primeiro', value=1, variable=selecionando_1)
radio_1.place(x=0,y=0)

radio_1 = Radiobutton(janela, command=obter, text='Segundo', value=2, variable=selecionando_1)
radio_1.place(x=0,y=50)

radio_1 = Radiobutton(janela, command=obter, text='Terceiro', value=3, variable=selecionando_1)
radio_1.place(x=0,y=100 )

janela.mainloop()
