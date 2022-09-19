from tkinter import *
cor1 = '#0f00f8'
janela = Tk()
janela.title('Formulário Principal')
janela.geometry('350x350')
cor = '0f00f8'
janela.title('Label')
janela.config(bg=cor1)

import webbrowser
global contador
contador = 0
def executar():
    global contador
    texto1 = 'Numero impar:  '
    texto2 = 'Numero par:  '
    if contador %2 ==0:
        resultado = texto2 + str(contador)
        label['text'] = resultado
        label['fg'] = '#24851e'
    else:
        resultado = texto1 + str(contador)
        label['text'] = resultado
        label['fg'] = '#2586c2'
    contador += 1

label = Label(janela, width=20,height=2, text='Texto apresentado', relief='flat', fg='white', bg='#121211')
label.place(x=0, y=0)

button = Button(janela, text="Clique aqui", width=20, height=10,command=lambda: webbrowser.open('https://www.cnnbrasil.com.br/wp-content/uploads/sites/12/2022/09/tse-caneta-azul-100001603164.jpg?w=161'))
button.place(x=150, y=20)



janela.mainloop()