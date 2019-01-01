from tkinter import*
import time 


# Déclaration variable pour rendre le programme adaptatif

largeur = 800
hauteur = 600
speed_mov_raq = hauteur * 0.1

def settings_func(root, default_settings):
    settings_window = Toplevel(root)
    settings_window.lift()
    settings_window.focus_force()
    settings_window.grab_set()
    settings_window.grab_release()

    ##fait ce que tu veux

    index = 0

    a = Entry(settings_window)
    a.pack()
    a.delete(0, END)
    a.insert(0, default_settings[index])
    index += 1

    b = Entry(settings_window)
    b.pack()
    b.delete(0, END)
    b.insert(0, default_settings[index])
    index += 1

    def quit_settings():
        global settings
        settings = [ a.get(), b.get() ] 
        settings_window.destroy()
        

    c = Button(settings_window, text="Quitter", command=quit_settings)
    c.pack()


# Création menu
def play_func(root, settings):
        jeu = Toplevel(root)
        jeu.lift()
        jeu.focus_force()
        jeu.grab_set()
        jeu.grab_release()
        canvas = Canvas(jeu, width=largeur, height=hauteur, bg='black')
        canvas.pack()

        ball = canvas.create_oval(largeur/2 - 10, hauteur/2 - 10, largeur/2 + 10, hauteur/2 + 10, fill="red")
        raq1 = canvas.create_rectangle(10, hauteur/2 - hauteur * 0.1, 20, hauteur/2 + hauteur * 0.1, fill="white")
        raq2 = canvas.create_rectangle(largeur - 10, hauteur/2 - hauteur*0.1, largeur - 20, hauteur/2 + hauteur*0.1, fill='white')

        
        has_moved = Entry(jeu)
        has_moved.pack()
        has_moved.insert(0, "False")

        def ball_move(x, y):
            ScoreGauche = 0
            ScoreDroite = 0
            test = True
            if has_moved.get() == "True":
                while test:
                    canvas.move(ball, x, y)
                    time.sleep(0.025)
                    jeu.update()
                    
                    posraq1 = canvas.coords(raq1)
                    posraq2 = canvas.coords(raq2)
                    pos = canvas.coords(ball)
                    
                    if pos[3] >= hauteur or pos[1] <= 0:
                        y = -y
                    if posraq2[1] <= pos[3] <= posraq2[3] and pos[2] == posraq2[0] or posraq1[1] <= pos[3] <= posraq1[3] and pos[0] == posraq1[2]:
                        x = -x
                    if pos[0] > largeur:
                        test = False
                        ScoreGauche += 1
                        quitter()
                    if pos[2] < 0:
                        test = False
                        ScoreDroite += 1
                        quitter()
            else:
                time.sleep(0.025)
                jeu.update()
                ball_move(x, y)

# Déplacement raquette gauche

        def raq1_move_up(event):
            has_moved.delete(0, END)
            has_moved.insert(0, "True")
            posraq1 = canvas.coords(raq1)
            if posraq1[1] > 0:
                canvas.move(raq1, 0, -speed_mov_raq)

        def raq1_move_down(event):
            has_moved.delete(0, END)
            has_moved.insert(0, "True")
            posraq1 = canvas.coords(raq1)
            if posraq1[3] < hauteur:
                canvas.move(raq1, 0, speed_mov_raq)

        jeu.bind('z', raq1_move_up)
        jeu.bind('s', raq1_move_down)


        def raq2_move_up(event):
            has_moved.delete(0, END)
            has_moved.insert(0, "True")
            posraq2 = canvas.coords(raq2)
            if posraq2[1] > 0:
                canvas.move(raq2, 0, - speed_mov_raq)

        def raq2_move_down(event):
            has_moved.delete(0, END)
            has_moved.insert(0, "True")
            posraq2 = canvas.coords(raq2)
            if posraq2[3] < hauteur:
                canvas.move(raq2, 0, speed_mov_raq)

        jeu.bind('<Up>', raq2_move_up)
        jeu.bind('<Down>', raq2_move_down)

        def init():
            ball_move(10, 10)

        def quitter():
            jeu.destroy()
        
        init()

#play()

root = Tk()

settings = ["par defaut", "lol pierre est nul" ]

def play_game():
    play_func(root, settings)

def show_settings():
    global settings
    settings = settings_func(root, settings)
    print(settings)

play_button = Button(root, text="Jouer", command=play_game)
play_button.place(relx=0.5, rely=0.2, anchor=CENTER)
settings_button = Button(root, text="Options", command=show_settings)
settings_button.place(relx=0.5, rely=0.5, anchor=CENTER)
quit_button = Button(root, text="Quitter", command=root.destroy)
quit_button.place(relx=0.5, rely=0.8, anchor=CENTER)
        
root.mainloop()