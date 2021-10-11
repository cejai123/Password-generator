import tkinter 
from tkinter import *
import string
import random
import time
class main(Tk):
    def __init__(self):
        super().__init__()
        v1 = DoubleVar()
        self.textbox = Text(width=70, height=2)
        self.textbox.pack()
        self.textbox.config(state="disabled")
        self.passwordlabel = Label(text="How many characters do you want the password to have.").pack()
        self.passwordamt = Scale(variable=v1, from_=1, to=100,orient=HORIZONTAL)
        self.passwordamt.pack()
        self.frame1 = Frame()
        self.frame1.pack()
        self.generate = Button(self.frame1,text="Generate", command=self.generateaction).pack(anchor=CENTER)

    def generateaction(self):
        self.textbox.config(state="normal")
        self.textbox.delete(1.0,END)
        self.passwordliteral = "".join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=self.passwordamt.get()))
        self.textbox.insert(1.0, self.passwordliteral)
        time.sleep(0.1)
        self.textbox.config(state="disabled")

if __name__ == "__main__":
    g = main()
    g.title("Password Generator")
    g.geometry("600x140")
    g.mainloop()