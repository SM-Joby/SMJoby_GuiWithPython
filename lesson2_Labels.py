from tkinter import*

window = Tk()
window.geometry("500x500")
window.title("LABELS WITH GUI")
window.config(background = "pink")

#label widgets
username_label = Label(window, text = "Username", bg = "blue")
username_label.place(x = 50, y = 100) #in lesson 1 used pack

password_label = Label(window, text = "password", bg = "blue")
password_label.place(x = 50, y = 175)

#entry widgets
username_entry = Entry(window, width = 15)
username_entry.place(x = 125, y = 100)

password_entry = Entry(window, width = 15)
password_entry.place(x = 125, y = 175)

submit_button = Button(window,text = "Submit", bg = "red")
submit_button.place(x = 250, y = 250)

window.mainloop()