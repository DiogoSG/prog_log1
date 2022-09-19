
from tkinter import *

cor1='#0f00f8'
janela = Tk()

janela.title('Formulário Principal')

janela.geometry('350x350')

cor='0f00f8'

janela.title('Label')

janela.config(bg=cor1)

label_nome = Label (janela, width=10, height=2, text="Nome", font=('Arial 15 bold'),fg="red", bg="black")
label_nome.grid(row=0, column=0)

label_Telefone = Label (janela, width=10,height=2,text="Telefone", font=('Arial 15 bold'),fg="red", bg="black")
label_Telefone.grid(row=1, column=0)

label_Endereço = Label (janela, width=10,height=2,text="Endereço", font=('Arial 15 bold'),fg="red", bg="black")
label_Endereço.grid(row=2, column=0)

label_Cidade = Label (janela, width=10,height=2,text="Cidade", font=('Arial 15 bold'),fg="red", bg="black")
label_Cidade.grid(row=3, column=0)

label_Estado = Label (janela, width=10,height=2,text="Estado", font=('Arial 15 bold'),fg="red", bg="black")
label_Estado.grid(row=4, column=0)

janela.iconphoto(False, PhotoImage(file='..\ProgSoftware\imagens\Logo_Label.png'))



janela.mainloop()
