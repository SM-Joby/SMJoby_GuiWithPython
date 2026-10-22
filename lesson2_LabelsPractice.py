from tkinter import*

window = Tk()
window.geometry("500x500")
window.title("The Best newsletter ever")
window.config(background = "yellow")

subscribe_label = Label(window, text = "Subscribe to our newsletter in the button below", width = 40)
subscribe_label.place(x = 50, y = 75)

email_label = Label(window, text = "Email", bg = "orange")
email_label.place(x = 75 , y =185 )
email_entry = Entry(window, width = 15)
email_entry.place(x = 150, y = 185 )

subscribe_button = Button(window, text = "Subscribe", bg = "red")
subscribe_button.place(x = 250, y = 300)

window.mainloop()