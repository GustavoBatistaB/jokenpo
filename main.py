import tkinter
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import random

# cores --------------------------------
co0 = "#FFFFFF"  # white / branca
co1 = "#333333"  # black / preta
co2 = "#fcc058"  # orange / laranja
co3 = "#fff873"  # yellow / amarela
co4 = "#34eb3d"   # green / verde
co5 = "#e85151"   # red / vermelha
fundo = "#3b3b3b"

janela = Tk()
janela.title("jokenpo")
janela.geometry("260x280")
janela.configure(bg=fundo)

frame_cima = Frame(janela, width=260, height=100, bg=co1, relief="raised")
frame_cima.grid(row=0, column=0, sticky=NW)

frame_baixo = Frame(janela, width=260, height=180, bg=co0,relief="flat")
frame_baixo.grid(row=1, column=0, sticky=NW)

estilo = ttk.Style(janela)
estilo.theme_use("clam")

app_1 = Label(frame_cima, text="Você", height=1, anchor="center", font=("Ivy 10 bold"), bg=co1, fg=co0)
app_1.place(x=40, y=70)

app_1_linha = Label(frame_cima, text="", height=10, anchor="center", font=("Ivy 10 bold"), bg=co0, fg=co0)
app_1_linha.place(x=0, y=0)

app_1_ponto = Label(frame_cima, text="0", height=1, anchor="center", font=("Ivy 30 bold"),bg=co1, fg=co0 )
app_1_ponto.place(x=50, y=20)

app_ = Label(frame_cima, text=":", height=1, anchor="center", font=("Ivy 30 bold"), bg=co1, fg=co0)
app_.place(x=125, y=20)

app_2 = Label(frame_cima, text="Pc", height=1, anchor="center", font=("Ivy 10 bold"), bg=co1, fg=co0)
app_2.place(x=205, y=70)

app_2_linha = Label(frame_cima, text="", height=10, anchor="center", font=("Ivy 10 bold"), bg=co0, fg=co0)
app_2_linha.place(x=255, y=0)

app_2_ponto = Label(frame_cima, text="0", height=1, anchor="center", font=("Ivy 30 bold"), bg=co1, fg=co0)
app_2_ponto.place(x=200, y=20)

app_linha = Label(frame_cima, text="", width=255, anchor="center", font=("Ivy 10 bold"), bg=co0, fg=co0)
app_linha.place(x=0, y=95)

app_texto = Label(frame_baixo, text='Tá pronto ? ', height=1, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co1)
app_texto.place(x=80, y=50)

app_texto_1 = Label(frame_baixo, text='', height=1, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co1)
app_texto_1.place(x=10, y=20)

app_texto_2 = Label(frame_baixo, text='', height=1, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co1)
app_texto_2.place(x=200, y=20)

global voce
global pc
global rondas
global pontos_voce
global pontos_pc

pontos_voce = 0
pontos_pc = 0
rondas = 5


#função logica do jogo


def jogar(i):
    global rondas
    global pontos_voce
    global pontos_pc

    if rondas > 0:
        opcoes = ['Pedra', 'Papel', 'Tesoura']
        pc = random.choice(opcoes)
        voce = i
        app_texto_1['text'] = i
        app_texto_2['text'] = pc

        if voce == pc:
            app_linha['bg'] = co2
            app_1_linha['bg'] = co0
            app_2_linha['bg'] = co0
            app_texto['text'] = 'Foi Empate'

        elif voce == 'Papel' and pc == 'Pedra':
            app_linha['bg'] = co0
            app_1_linha['bg'] = co5
            app_2_linha['bg'] = co0
            pontos_voce += 1
            app_texto['text'] = 'Você Ganhou'

        elif voce == 'Tesoura' and pc == 'Papel':
            app_linha['bg'] = co0
            app_1_linha['bg'] = co5
            app_2_linha['bg'] = co0
            pontos_voce += 1
            app_texto['text'] = 'Você Ganhou'

        elif voce == 'Pedra' and pc == 'Tesoura':
            app_linha['bg'] = co0
            app_1_linha['bg'] = co5
            app_2_linha['bg'] = co0
            pontos_voce += 1
            app_texto['text'] = 'Você Ganhou'

        else:
            app_linha['bg'] = co0
            app_1_linha['bg'] = co0
            app_2_linha['bg'] = co5
            pontos_pc += 1
            app_texto['text'] = 'Pc Ganhou'

        app_1_ponto['text'] = pontos_voce
        app_2_ponto['text'] = pontos_pc

        rondas -=1
    else:

        app_1_ponto['text'] = pontos_voce
        app_2_ponto['text'] = pontos_pc

        fim_do_jogo()


def iniciar_jogo():

    global icon_1
    global icon_2
    global icon_3
    global b_icon_1
    global b_icon_2
    global b_icon_3

    b_jogar.destroy()

    icon_1 = Image.open('image/pedra.png')
    icon_1 = icon_1.resize((50, 50), Image.ANTIALIAS)
    icon_1 = ImageTk.PhotoImage(icon_1)
    b_icon_1 = Button(frame_baixo, command=lambda: jogar('Pedra') , width=50, image=icon_1, compound=CENTER, bg=co0, fg=co0, font=("Ivy 10 bold"),
                      anchor=CENTER, relief=FLAT)
    b_icon_1.place(x=15, y=60)

    icon_2 = Image.open('image/tesoura.png')
    icon_2 = icon_2.resize((50, 50), Image.ANTIALIAS)
    icon_2 = ImageTk.PhotoImage(icon_2)
    b_icon_2 = Button(frame_baixo, command=lambda: jogar('Tesoura'), width=50, image=icon_2, compound=CENTER, bg=co0, fg=co0, font=("Ivy 10 bold"),
                      anchor=CENTER, relief=FLAT)
    b_icon_2.place(x=100, y=90)

    icon_3 = Image.open('image/papel.png')
    icon_3 = icon_3.resize((50, 50), Image.ANTIALIAS)
    icon_3 = ImageTk.PhotoImage(icon_3)
    b_icon_3 = Button(frame_baixo, command=lambda: jogar('Papel'), width=50, image=icon_3, compound=CENTER, bg=co0, fg=co0, font=("Ivy 10 bold"),
                      anchor=CENTER, relief=FLAT)
    b_icon_3.place(x=170, y=60)


def fim_do_jogo():
    global rondas
    global pontos_voce
    global pontos_pc

    rondas = 5
    pontos_pc = 0
    pontos_voce = 0

    b_icon_1.destroy()
    b_icon_2.destroy()
    b_icon_3.destroy()

    jogador_voce = int(app_1_ponto['text'])
    jogador_pc = int(app_2_ponto['text'])

    if jogador_voce > jogador_pc:
        app_texto['text'] = 'Voce Venceu o jogo '
        app_texto['fg'] = co4

        app_linha['bg'] = co4
        app_1_linha['bg'] = co4
        app_2_linha['bg'] = co4

    elif jogador_pc > jogador_voce:
        app_texto['text'] = 'Você perdeu o jogo '
        app_texto['fg'] = co5

        app_linha['bg'] = co5
        app_1_linha['bg'] = co5
        app_2_linha['bg'] = co5

    else:
        app_texto['text'] = 'Ninguém Ganhou '
        app_texto['fg'] = co2

        app_linha['bg'] = co2
        app_1_linha['bg'] = co2
        app_2_linha['bg'] = co2

    def jogar_denovo():
        app_1_ponto['text'] = '0'
        app_2_ponto['text'] = '0'
        app_texto['text'] = ''
        app_texto['fg'] = co1

        app_linha['bg'] = co0
        app_1_linha['bg'] = co0
        app_2_linha['bg'] = co0

        b_jogar_denovo.destroy()

        iniciar_jogo()
    b_jogar_denovo = Button(frame_baixo, command=jogar_denovo, width=30, text='Jogar denovo', bg=fundo, fg=co0, font=("Ivy 10 bold"),
                anchor=CENTER, relief=RAISED, overrelief=RIDGE)
    b_jogar_denovo.place(x=5, y=151)



b_jogar = Button(frame_baixo,command=iniciar_jogo, width=30, text='Jogar', bg=fundo, fg=co0, font=("Ivy 10 bold"),
                     anchor=CENTER, relief=RAISED, overrelief=RIDGE)
b_jogar.place(x=5, y=151)


janela.mainloop()
