from cinema import Cinema
from administrador import Admnistrador
from entrada import Entrada
from cliente import Cliente
from tkinter import *


cinema = Cinema()
adm = Admnistrador()
entrada = Entrada(40)

adm.adicionarSala(cinema, 0, 10)
adm.adicionarSala(cinema, 1, 20)

cliente = ''
filmeEscolhido = ''
poltronasDisponiveis = ['Sessão não escolhida']


for i in range(0, 7):
    adm.adicionarFilme(cinema, i, "Macacos", 2, "Myck")
    adm.adicionarSessao(cinema, i, "Macacos", 0, "18h", 0)
    adm.adicionarSessao(cinema, i, "Macacos", 1, "20h", 1)
    adm.adicionarFilme(cinema, i, "Tigres", 2, "Jorge")
    adm.adicionarSessao(cinema, i, "Tigres", 0, "18h", 0)
    adm.adicionarSessao(cinema, i, "Tigres", 1, "20h", 1)


root = Tk()

nome = StringVar()
telefone = StringVar()
#Providing Geometry to the form
root.geometry("500x1000")

#Providing title to the form
root.title('Cinema')

#this creates 'Label' widget for Registration Form and uses place() method.
label_0 =Label(root,text="Reservar cadeira", width=20,font=("bold",20))
#place method in tkinter is  geometry manager it is used to organize widgets by placing them in specific position
label_0.place(x=90,y=30)

label_1 =Label(root,text="Nome", width=20,font=("bold",10))
label_1.place(x=80,y=100)

#this will accept the input string text from the user.
entry_1=Entry(root, textvariable=nome)
entry_1.place(x=240,y=100)


#this creates 'Label' widget for Email and uses place() method.
label_3 =Label(root,text="Telefone", width=20,font=("bold",10))
label_3.place(x=68,y=120)

entry_3=Entry(root, textvariable=telefone)
entry_3.place(x=240,y=120)

label_4 =Label(root,text="Dia", width=20,font=("bold",10))
label_4.place(x=180,y=140)

#the variable 'var' mentioned here holds Integer Value, by deault 0
dia=IntVar()
#this creates 'Radio button' widget and uses place() method
Radiobutton(root,text="Domingo",padx= 5, variable= dia, value=0).place(x=0,y=160)
Radiobutton(root,text="Segunda",padx= 5, variable= dia, value=1).place(x=80,y=160)
Radiobutton(root,text="Terça",padx= 5, variable= dia, value=2).place(x=160,y=160)
Radiobutton(root,text="Quarta",padx= 5, variable= dia, value=3).place(x=240,y=160)
Radiobutton(root,text="Quinta",padx= 5, variable= dia, value=4).place(x=320,y=160)
Radiobutton(root,text="Sexta",padx= 5, variable= dia, value=5).place(x=400,y=160)
Radiobutton(root,text="Sábado",padx= 5, variable= dia, value=6).place(x=0,y=180)

label_5 =Label(root,text="Filme", width=20,font=("bold",10))
label_5.place(x=80,y=200)

#the variable 'var' mentioned here holds Integer Value, by deault 0
filme=IntVar()
#this creates 'Radio button' widget and uses place() method
Radiobutton(root,text="Macacos",padx= 5, variable= filme, value=0).place(x=200,y=200)
Radiobutton(root,text="Tigres",padx= 5, variable= filme, value=1).place(x=280,y=200)


def settarPrimeiros():
    cliente = Cliente(nome.get(), telefone.get())
    filmeEscolhido = cinema.dias[dia.get()].filmes[filme.get()]
    diaAtual = cinema.dias[dia.get()]
    def settarSessao():
        poltronasDisponiveis = filmeEscolhido.poltronasDisponiveis(sessao.get())
        label_5=Label(root,text="Poltrona",width=20,font=("bold",10))
        label_5.place(x=70,y=420)
        c=StringVar()
        droplist=OptionMenu(root,c, *poltronasDisponiveis)
        droplist.config(width=15)
        c.set('Selecione a cadeira')
        droplist.place(x=240,y=420)
        def reservar():
            try:
                filmeEscolhido.ocuparPoltrona(cliente, entrada, sessao.get(), int(c.get()), diaAtual)
            except KeyError as error:
                print(f"Erro: {error}")
            label9 = Label(root, text=cliente.reservas[len(cliente.reservas)-1].imprimirReserva(), font=("bold", 10))
            label9.place(x=80,y=520)

        Button(root, text='Submeter' , width=20,bg="black",fg='white', command= reservar).place(x=180,y=460)


    label_6 =Label(root,text="Sessao", width=20,font=("bold",10))
    label_6.place(x=80,y=300)

    #the variable 'var' mentioned here holds Integer Value, by deault 0
    sessao=IntVar()
    #this creates 'Radio button' widget and uses place() method
    Radiobutton(root,text="18h",padx= 5, variable= sessao, value=0).place(x=200,y=300)
    Radiobutton(root,text="20h",padx= 5, variable= sessao, value=1).place(x=280,y=300)
    Button(root, text='Confirmar' , width=20,bg="black",fg='white', command= settarSessao).place(x=180,y=340)


Button(root, text='Confirmar' , width=20,bg="black",fg='white', command= settarPrimeiros).place(x=180,y=240)






root.mainloop()

# cliente = Cliente("Eu", "999103081")

# entrada = Entrada(40)

# print(cinema.dias[0].filmes[0].poltronasDisponiveis(0))

# try:
#     cinema.dias[0].filmes[0].ocuparPoltrona(cliente, entrada, 0, 4, cinema.dias[0].nome)
# except KeyError as error:
#     print(f"Erro: {error}")

# try:
#     cinema.dias[0].filmes[0].ocuparPoltrona(cliente, entrada, 0, 4, cinema.dias[0].nome)
# except KeyError as error:
#     print(f"Erro: {error}")



# for reserva in cliente.reservas:
#     print(reserva.imprimirReserva())