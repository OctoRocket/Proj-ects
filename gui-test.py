from tkinter import *

window = Tk()
window.title("gui-test")
photo1 = PhotoImage(file="./1.png")
Label (window, image=photo1, bg="black",) .grid(row=0, column=0, sticky=E)
window.mainloop()