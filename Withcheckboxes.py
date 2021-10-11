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
        self.frame2 = Frame()
        self.frame2.pack()
        self.frame1 = Frame()
        self.frame1.pack()
        self.var1 = IntVar()
        self.var2 = IntVar()
        self.numberc1 = Checkbutton(self.frame2,text="Numbers and lowercase letters", variable=self.var1, onvalue=1, offvalue=0)
        self.numberc1.pack(side=RIGHT)
        self.numberc2 = Checkbutton(self.frame2,text="Uppercase and lowercase letters", variable=self.var2, onvalue=2, offvalue=1)
        self.numberc2.pack(side=RIGHT)
        self.generate = Button(self.frame1,text="Generate", command=self.generateaction)
        self.generate.pack(anchor=CENTER)

    def generateaction(self):
       if (self.var1.get() == 1) & (self.var2.get() == 1):
           self.textbox.config(state="normal")
           self.textbox.delete(1.0, END)
           self.passwordnumbers = "".join(random.choices(string.ascii_lowercase + string.digits, k=self.passwordamt.get()))
           self.textbox.insert(1.0, self.passwordnumbers)
           time.sleep(0.1)
           self.textbox.config(state="disabled")
       elif (self.var1.get() == 0) & (self.var2.get() == 2):
            self.textbox.config(state="normal")
            self.textbox.delete(1.0, END)
            self.passworduppercase = "".join(random.choices(string.ascii_lowercase + string.ascii_uppercase, k=self.passwordamt.get()))
            self.textbox.insert(1.0, self.passworduppercase)
            time.sleep(0.1)
            self.textbox.config(state="disabled")
       elif (self.var1.get() == 1) & (self.var2.get() == 2):
            self.textbox.config(state="normal")
            self.textbox.delete(1.0, END)
            self.passwordeverything = "".join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits , k=self.passwordamt.get()))
            self.textbox.insert(1.0, self.passwordeverything)
            time.sleep(0.1)
            self.textbox.config(state="disabled")
       else:
            self.textbox.config(state="normal")
            self.textbox.delete(1.0, END)
            self.passwordlowercase = "".join(random.choices(string.ascii_lowercase, k=self.passwordamt.get()))
            self.textbox.insert(1.0, self.passwordlowercase)
            time.sleep(0.1)
            self.textbox.config(state="disabled")

if __name__ == "__main__":
    g = main()
    g.title("Password Generator")
    g.geometry("600x150")
    g.mainloop()