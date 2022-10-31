import tkinter as tk
from tkinter import filedialog
class Tela:
    def __int__(self,master):
        self.nossaTela = master
        self.barraMenu = tk.Menu(self.nossaTela)
        self.nossaTela.config(menu = self.barraMenu)
        self.barraMenu.add_command(label = "Ler arquivo", command=self.lerArquivo)
    def lerArquivo(self):
            caminho = filedialog.askopenfile(mode = "r", initialdir = '/Downloads', title='Selecione um arquivo', filetypes = (("Arquivos de texto",'*.txt'),("Arquivos Python","*.py")))

            if caminho:
                conteudo = caminho.read()
                print(conteudo)
            else:
                print('Por favor escolha um arquivo')
janelaRaiz = tk.Tk()
Tela(janelaRaiz)
janelaRaiz.mainloop()
