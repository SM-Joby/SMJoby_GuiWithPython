from tkinter import* #star will indicate it will work where all the functions are loaded

#creating window
window = Tk() #variable = Tk()
window.geometry("100x100")# .geometry allows us to change the dimensions(lxw) of the window
window.title("MyFirstTitle")
window.config(background = "blue")
#creating button
b1 = Button(window,text = "CLICK ME!!!", command = window.destroy)
b1.pack(side = "top")

window.mainloop()#function whic allows for the window to stay, it doesn't go off
