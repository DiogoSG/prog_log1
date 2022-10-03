from tkinter import *
import tkinter
cor1 = 'white'
janela = Tk()
janela.title('Cronometro')
janela.geometry('400x400')
cor = '#d1c7ff'
janela.title('Cronometro')
janela.config(bg=cor)

hour = StringVar()
minute = StringVar()
second = StringVar()
hour.set('00')
minute.set('00')
second.set('00')

global tempo
tempo = '00:00:00'
count = -5
run = False

def iniciar():
    def valor():
        if run:
            global count
            global tempo
            if count <= -1:
                inicio = 'começando em' + str(abs(count))
                label_time['text'] = inicio
                label_time['font']= 'ivy20'
            else:
                label_time['font'] = 'Times 50 bold'
                d = str(tempo)
                h,m,s = map(int,d.split(':'))
                h=int(h)
                m=int(m)
                s=int(count)

                if(s>=5):
                    count = 0
                    m+=1

                s=str(0)+str(s)
                m=str(0)+str(m)
                h=str(0)+str(h)
                d=str(h[-2:])+':'+str(m[-2:])+':'+str(s[-2:])
                label_time['text'] = d
                tempo = d
                s= int(count)
                m= int(m)
                h=int(h)

                label_time.after(1000, valor)
                count+= 1
                valor()

def start():
    global run
    run = True
    iniciar()

def stop():
    global count
    count = -5





def reset():
    global count
    count = -5
    if run == False:
        global tempo
        tempo = '00:00:00'

hourEntry = Entry(janela, width=3, font='Arial 50', textvariable=hour, bg="#d1c7ff")
hourEntry.place(x=80, y=150)

minuteEntry = Entry(janela, width=3, font='Arial 50', textvariable=minute, bg="#d1c7ff")
minuteEntry.place(x=160, y=150)

secondEntry = Entry(janela, width=3, font='Arial 50', textvariable=second, bg="#d1c7ff", relief='solid')
secondEntry.place(x=240, y=150)

label = Label(janela, font='arial 12', text = 'Cronometro', bg='#d1c7ff')
label.place(x=0,y=0)


iniciar=Button(janela,width=10, text = 'Iniciar', relief='solid')
iniciar.place(x=75, y=250)

Pausar=Button(janela,width=10, text = 'Pausar', relief='solid')
Pausar.place(x=175, y=250)

Zerar=Button(janela,width=10, command=reset, text = 'Zerar', relief='solid')
Zerar.place(x=275, y=250)





janela.mainloop()
