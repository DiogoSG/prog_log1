from tkinter import *
janela = Tk()
janela.title('Frame')
janela.geometry('400x400')

frame = Frame(janela, width=200,height=200, bg='blue')
frame.grid (row=1, column=0, pady=2, padx=2)

frame = Frame(janela, width=125,height=125, bg='cyan')
frame.grid (row=1, column=0, pady=2, padx=2)

frame1 = Frame(janela, width=200,height=200, bg='red')
frame1.grid (row=1, column=2, pady=2, padx=2)

foto = PhotoImage(file='..\Frame\Imagem\Foto.png', height=200, width= 200)
Label(frame1,image=foto).pack()

janela.iconphoto(False, PhotoImage(file='..\Frame\Imagem\Logo.png'))



frame2 = Frame(janela, width=200,height=200, bg='light green')
frame2.grid (row=2, column=0, pady=2, padx=2)

botao = Button(janela, height=5, width=10, text='Botão')
botao.grid (row=2, column=0, pady=2, padx=2)

frame3 = Frame(janela, width=200,height=200, bg='black')
frame3.grid (row=2, column=2, pady=2, padx=2)


janela.mainloop()