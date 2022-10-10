from tkinter import *
janela = Tk()
janela.title('Facebook')
janela.geometry('820x230')

janela.iconphoto(False, PhotoImage(file='..\Auladia10\Foto\Foto.png'))

f_nav = Frame(janela, width = 820, height = 50, bg= 'blue')
f_nav.place (x=0, y=0)

f_esq = Frame(janela, width=180,height=200, bg='white')
f_esq.place (x=0, y=50)

f_meio = Frame(janela, width=400,height=200, bg='black')
f_meio.place (x=180, y=50)

f_dir = Frame(janela, width=175,height=200, bg='black')
f_dir.place (x=590, y=50)

text = Label(f_esq,width=22, text= 'Atalhos',bg='white')
text.place (x=0, y=65)

text2 = Label(f_esq, width=22, text= 'Bem vindo ao Facebook', bg='white')
text2.place (x=0, y=90)

janela.mainloop()