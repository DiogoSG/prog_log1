import tkinter as tk
from tkinter import filedialog


class Tela:

    def __init__(self, master):
        self.nossaTela = master
        self.arquivoAberto = None
        self.criaWidgets()

    def criaWidgets(self):
        self.lbl1 = tk.Label(self.nossaTela, text='Entre o nome:', font=('Arial', 12))
        self.lbl1.grid(column=0)

        self.entradaNome = tk.Entry(self.nossaTela, font=('Arial', 12))
        self.entradaNome.grid(row=0, column=1, padx=20)

        self.lbl2 = tk.Label(self.nossaTela, text="Entre com o telefone:", font=('Arial', 12))
        self.lbl2.grid(row=1, column=0)

        self.entradaTel = tk.Entry(self.nossaTela, font=('Arial', 12))
        self.entradaTel.grid(row=1, column=1, padx=20)

        self.cadastra = tk.Button(self.nossaTela, text="Cadastrar", command=self.salvar)
        self.cadastra.grid(row=2, column=0, columnspan=2, pady=20)

    def salvar(self):
        nome = self.entradaNome.get()
        telefone = self.entradaTel.get()
        if self.arquivoAberto is None:
            self.arquivoAberto = filedialog.askopenfilename(defaultextension= '.txt', filetypes=(('Arquivos de Texto', '*.txt', ('Todos arquivos', '*.*'))))

        if self.arquivoAberto is not None:
            dados = open(self.arquivoAberto, 'a')
            dados.write('\nNome:{}\n--->Telefone:{}'.format(nome, telefone))
            dados.close()
        else:
            print('Erro')


janelaRaiz = tk.Tk()
Tela(janelaRaiz)
janelaRaiz.mainloop()
