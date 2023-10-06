from tkinter import *
from tkinter import *
from random import *
import time

root = Tk()
root.resizable(width=False, height=False)
root.attributes('-alpha', 0.9) # прозрачность окна

root.geometry('500x500+400+100')
root.title('Звездное небо')
root['bg'] = '#0b193d'

canvas = Canvas(root, width=500, height=400, bg='#0b193d')
canvas.pack()

def fun():
    while True:
        time.sleep(1)
        x =randint(0,600)

        y =randint(0,600)
        # canvas.delete('all')
        canvas.create_oval(x-3,y-3,x+3,y+3, fill ='white')
        canvas.update()

btn = Button (text = 'Зажги звезду',
              bg='white',
              font="Consolas 14",
              fg='black',
                command = fun)

btn.pack(anchor='s', pady = 20)



root.mainloop()