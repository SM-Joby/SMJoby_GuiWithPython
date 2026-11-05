from tkinter import*

window = Tk()
window.geometry("500x500")
window.title("CELCIUS TO FAHRENHEIT")
window.config(background = "grey")

def calc():
    c = celcius_space.get()
    if c.replace(".", "",1).isdigit():
        float_c = float(c)
        f = (float_c*9/5)+32
        fahrenheit.config(text = "It is" + str(f) + "degrees Fahrenheit")



heading = Label(window, text = "CELCIUS -> FAHRENHEIT")
heading.place (x = 175, y = 50)
celcius = Label(window, text = "Enter Temperature in degrees Celcius: ")
celcius.place(x = 105, y = 100)
celcius_space = Entry(window, width = 15)
celcius_space.place(x =325, y = 100)
fahrenheit = Label(window, text = "It is ___ degrees fahrenheit")
fahrenheit.place(x = 175, y = 175)
convert = Button(window, text = "CONVERT",bd = 5, command = calc)
convert.place(x = 215, y =225 )

window.mainloop()

