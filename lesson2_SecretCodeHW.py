from tkinter import*

window = Tk()
window.title("Security Check")
window.geometry("300x150")  

pin = Label(window, text="Enter PIN Code", font=("Arial", 12))
pin.place(x = 50, y = 100)

entry_box = Entry(window, show="*", font=("Arial", 12), bd = 5)
entry_box.place(x = 200, y = 100)

submit_button = Button(window, text="Submit", bd = 5, command = window.destroy)
submit_button.place(x = 100, y = 125)


window.mainloop()




