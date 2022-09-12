#Criando a primeira janela
from tkinter import *
#Definindo variável de cor
cor1='#e20300'
janela = Tk()
#Titulo da janela
janela.title('Formulário de Cadastro')
#Tamanho da janela
janela.geometry('1366x720')
#Definindo cor da janela
janela.config(bg=cor1)
#Definindo icone da janela
janela.iconphoto(False, PhotoImage(file='..\ProgSoftware\imagens\LogoCadastro.png'))
#True(Tamanho pode ser alterado) False(Tamanho não pode ser alterado)
janela.resizable(width=False, height=True)

#Janela só pode ser fechada se clicar no X
janela.mainloop()