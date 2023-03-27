from tkinter import *
import tkinter.messagebox
import webbrowser as wb
import random


fen = Tk()
fen.title("Pierre Feuille Ciseaux")
fen.configure(background="powder blue")
fen.geometry("400x400+0+0")

def augmenter_score(mon_coup, ton_coup):
    global mon_score, ton_score
    if mon_coup == 1 and ton_coup==2:
        ton_score+=1
    elif mon_coup==2 and ton_coup==1:
        mon_score+=1
    elif mon_coup==1 and ton_coup==3:
        mon_score+=1
    elif mon_coup==3 and ton_coup==1:
        ton_score+=1
    elif mon_coup==3 and ton_coup==2:
        mon_score+=1
    elif mon_coup==2 and ton_coup==3:
        ton_score+=1

def jouer(ton_coup):
    global mon_score, ton_score, score1, score2
    if ton_coup==1:
        mon_coup = random.randint(1, 2)
        if mon_coup ==2:
            lab3.configure(image=papier)
        else :
            lab3.configure(image=pierre)
    elif ton_coup==2:
        mon_coup = random.randint(2, 3)
        if mon_coup == 2:
            lab3.configure(image=papier)
        else:
            lab3.configure(image=ciseaux)
    elif ton_coup==3:
        mon_coup = random.choice([1, 3])
        if mon_coup == 1:
            lab3.configure(image=pierre)
        else:
            lab3.configure(image=ciseaux)
    augmenter_score(mon_coup, ton_coup)
    score1.configure(text=str(ton_score))
    score2.configure(text=str(mon_score))

def jouer_pierre():
    jouer(1)
    lab1.configure(image=pierre)

def jouer_papier():
    jouer(2)
    lab1.configure(image=papier)

def jouer_ciseaux():
    jouer(3)
    lab1.configure(image=ciseaux)

def reinit():
    global mon_score, ton_score, score1, score2, lab1, lab3
    ton_score=0
    mon_score=0
    score1.configure(text=str(ton_score))
    score2.configure(text=str(mon_score))
    lab1.configure(image=rien)
    lab3.configure(image=rien)

def quitter():
    Exit = tkinter.messagebox.askyesno("Pierre feuille ciseaux", "Voulez-vous vraiment fermer le programme?")
    if Exit > 0:
        fen.destroy()
        return

def Aide():
    Aide = tkinter.messagebox.askokcancel("Pierre feuille ciseaux", "Pierre-papier-ciseaux est un jeu effectué avec les mains et opposant deux joueurs.")
    if Aide > 0:
        wb.open_new_tab("https://www.youtube.com/watch?v=k-QodkOo4Ug")
        return

ton_score=0
mon_score=0

rien=PhotoImage(file='rien.gif')
versus=PhotoImage(file='versus.gif')
pierre=PhotoImage(file='pierre.gif')
papier=PhotoImage(file='papier.gif')
ciseaux=PhotoImage(file='ciseaux.gif')

texte1=Label(fen, text='Humain :', font=('Arial', 20))
texte1.grid(row=0, column=0)

texte2=Label(fen, text='Machine :', font=('Arial', 20))
texte2.grid(row=0, column=2)

texte3=Label(fen, text="Pour jouer, cliquez sur une icone", font=('Arial', 20))
texte3.grid(row=3, columnspan=3, pady=5)

score1 = Label(fen, text="0", font=("Arial", 20))
score1.grid(row=1, column=0)

score2 = Label(fen, text="0", font=("Arial", 20))
score2.grid(row=1, column=2)

lab1 = Label(fen, image=rien)
lab1.grid(row=2, column=0)

lab2 = Label(fen, image=versus)
lab2.grid(row=2, column=1)

lab3 = Label(fen, image=rien)
lab3.grid(row=2, column=2)

bouton1 = Button(fen, command=jouer_pierre)
bouton1.configure(image=pierre)
#lab1.configure(image=pierre)
bouton1.grid(row=4, column=0)

bouton2 = Button(fen, command=jouer_papier)
bouton2.configure(image=papier)
bouton2.grid(row=4, column=1)

bouton3 = Button(fen, command=jouer_ciseaux)
bouton3.configure(image=ciseaux)
bouton3.grid(row=4, column=2)

bouton4 = Button(fen, text="Recommencer", command=reinit)
bouton4.grid(row=5, column=0, pady=10, sticky=E)

bouton5= Button(fen, text="Quitter", command=quitter)
bouton5.grid(row=5, column=2, pady=10, sticky=W)

bouton6= Button(fen, text="Aide", command=Aide)
bouton6.grid(row=0, column=1, pady=10, sticky=W)

fen.mainloop()
