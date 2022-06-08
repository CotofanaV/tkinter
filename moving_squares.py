
from tkinter import *

fereastra = Tk()

panza = Canvas(fereastra, width=600,height=600)
panza.pack()

patrat_1 = panza.create_rectangle(300, 300, 250,250, fill="green",outline="white")
patrat_2 = panza.create_rectangle(300, 300, 350,250, fill="blue",outline="white")
patrat_3 = panza.create_rectangle(300, 300, 250,350, fill="red",outline="white")
patrat_4 = panza.create_rectangle(300, 300, 350,350, fill="yellow",outline="white")

def miscare():
    panza.after(20,miscare)
    panza.move(patrat_1,-5,-5)
    panza.move(patrat_2,5,-5)
    panza.move(patrat_3,-5,5)
    panza.move(patrat_4,5,5)
    if (panza.coords(patrat_4)[0]== 600):
        fereastra.destroy()


miscare()
fereastra.mainloop()
