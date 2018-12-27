from tkinter import*
import time


menu = Tk()
 
canvas = Canvas(menu, width= 800, height=600, bg='black')
canvas.pack()



ball = canvas.create_oval(390,290,410,310, fill = "red")

def ball_move(x,y):
    while True :
        canvas.move(ball,x,y)
        menu.update()
        time.sleep(.025)
        pos = canvas.coords(ball)
        if pos[3] >= 600 or pos[1] <= 0 :
            y = -y
        if pos[2] >= 800 or pos[0] <= 0:
            x = -x
   
ball_move(10,10)




menu.mainloop()