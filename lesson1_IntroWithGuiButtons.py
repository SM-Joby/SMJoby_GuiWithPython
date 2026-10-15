from tkinter import*
import random

window = Tk()
window.geometry("200x200")
window.title("AnotherButton")
window.config(background = "yellow")

def colour_change():
    colours = ["red", "green","blue"]
    c = random.choice(colours)
    window.config(background = c)
    

b1 = Button(window,text = "Colour Change!", command = colour_change)
b1.pack(side ="top")

window.mainloop()
