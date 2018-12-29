from tkinter import*
import time


# Déclaration variable pour rendre le programme adaptatif

largeur = 800
hauteur = 600
speed_mov_raq = hauteur * 0.1


# Création menu
def menu():
    menu = Tk()
    menu = Canvas(menu, width=largeur, height=hauteur, bg='white')
    menu.pack()

    def quit_menu():
        menu.destroy()
        jeu()

    def jeu():
        jeu = Tk()
        canvas = Canvas(jeu, width=largeur, height=hauteur, bg='black')
        canvas.pack()

        ball = canvas.create_oval(largeur/2 - 10, hauteur/2 - 10, largeur/2+10, hauteur/2+10, fill="red")
        raq1 = canvas.create_rectangle(10, hauteur/2 - hauteur*0.1, 20, hauteur/2 + hauteur*0.1, fill="white")
        raq2 = canvas.create_rectangle(largeur - 10, hauteur/2 - hauteur*0.1, largeur - 20, hauteur/2 + hauteur*0.1, fill='white')

        def ball_move(x, y):
            ScoreGauche = 0
            ScoreDroite = 0
            test = True
            while test == True:
                canvas.move(ball, x, y)
                time.sleep(0.025)
                jeu.update()
                posraq1 = canvas.coords(raq1)
                posraq2 = canvas.coords(raq2)
                pos = canvas.coords(ball)
                if pos[3] >= hauteur or pos[1] <= 0:
                    y = -y
                if posraq2[1] < pos[3] < posraq2[3] and pos[2] == posraq2[0] or posraq1[1] < pos[3] < posraq1[3] and pos[0] == posraq1[2]:
                    x = -x
                if pos[0] > largeur:
                    test = False
                    ScoreGauche += 1
                    quitter()
                if pos[2] < 0:
                    test = False
                    ScoreDroite += 1
                    quitter()

# Déplacement raquette gauche

        def raq1_move_up(event):
            posraq1 = canvas.coords(raq1)
            if posraq1[1] > 0:
                canvas.move(raq1, 0, -speed_mov_raq)

        def raq1_move_down(event):
            posraq1 = canvas.coords(raq1)
            if posraq1[3] < hauteur:
                canvas.move(raq1, 0, speed_mov_raq)

        jeu.bind('z', raq1_move_up)
        jeu.bind('s', raq1_move_down)


        def raq2_move_up(event):
            posraq2 = canvas.coords(raq2)
            if posraq2[1] > 0:
                canvas.move(raq2, 0, - speed_mov_raq)

        def raq2_move_down(event):
            posraq2 = canvas.coords(raq2)
            if posraq2[3] < hauteur:
                canvas.move(raq2, 0, speed_mov_raq)

        jeu.bind('<Up>', raq2_move_up)
        jeu.bind('<Down>', raq2_move_down)

        def init():
            ball_move(10, 10)

        def quitter():
            jeu.destroy()
            menu()            

        init()
        jeu.mainloop()

    btn_play = Button(menu, text='Play', command=quit_menu, width = 20)
    btn_play.grid(padx= largeur/2, pady= hauteur/2)

    menu.mainloop()
menu()