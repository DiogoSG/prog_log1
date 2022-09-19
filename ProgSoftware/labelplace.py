
from tkinter import *

cor1='#0f00f8'
janela = Tk()

janela.title('Formulário Principal')

janela.geometry('350x350')

cor='0f00f8'

janela.title('Label')

janela.config(bg=cor1)


label_nome = Label (janela, width=10, height=2, text="Nome", font=('Arial 15 bold'),fg="red", bg="black")
label_nome.place(x=0, y=0)

label_nome = Label (janela, width=10, height=2, text="Diogo", font=('Arial 15 bold'),fg="red", bg="black")
label_nome.place(x=150, y=0)

label_Telefone = Label (janela, width=10,height=2,text="Telefone", font=('Arial 15 bold'),fg="red", bg="black")
label_Telefone.place(x=0, y=50)

label_Telefone = Label (janela, width=10,height=2,text="1231234", font=('Arial 15 bold'),fg="red", bg="black")
label_Telefone.place(x=150, y=50)

label_Endereço = Label (janela, width=10,height=2,text="Endereço", font=('Arial 15 bold'),fg="red", bg="black")
label_Endereço.place(x=0, y=100)

label_Endereço = Label (janela, width=10,height=2,text="Capanema", font=('Arial 15 bold'),fg="red", bg="black")
label_Endereço.place(x=150, y=100)

label_Cidade = Label (janela, width=10,height=2,text="Cidade", font=('Arial 15 bold'),fg="red", bg="black")
label_Cidade.place(x=0, y=150)

label_Cidade = Label (janela, width=10,height=2,text="Capanema", font=('Arial 15 bold'),fg="red", bg="black")
label_Cidade.place(x=150, y=150)

label_Estado = Label (janela, width=10,height=2,text="Estado", font=('Arial 15 bold'),fg="red", bg="black")
label_Estado.place(x=0, y=200)

label_Estado = Label (janela, width=10,height=2,text="Paraná", font=('Arial 15 bold'),fg="red", bg="black")
label_Estado.place(x=150, y=200)


janela.iconphoto(False, PhotoImage(file='..\ProgSoftware\imagens\Logo_Label.png'))



janela.mainloop()
