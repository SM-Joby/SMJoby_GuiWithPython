from tkinter import*

window = Tk()
window.geometry("200x300")
window.title("Traffic Light")

red = Button(window, text="STOP", bg="red", fg="white", font = "Calibri", width = 10, height = 10, activeforeground = "blue", activebackground = "pink", bd = 10)
red.pack(side="top")


green = Button(window, text="GO", bg="green", fg="white")
green.pack(side="bottom")


yellow = Button(window, text="WAIT", bg="yellow", fg="black")
yellow.pack(side="left")


window.mainloop()

