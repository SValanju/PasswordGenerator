from tkinter import *
import random, string

#title
top=Tk()
top.title("PASSWORD GENERATOR")
top.resizable(width=FALSE, height=FALSE)
Label(top, text="PASSWORD GENERATOR",
            fg="white",
            bg="dark blue",
            font="Helvetica 48 bold").pack()

Label(top, text="Developed By Webmaster Guru",
            fg="white",
            bg="dark blue",
            font="Helvetica 16 bold").pack()

Label(top, text="Welcome To Password Generator",
            fg="blue",
            font="Times 28 bold").pack()

l1= Label(text="\nCreating a better Password:",
          fg="black",
          font="Helvetica 16 bold").pack()

l2=Label(text="\nCan you enter a password that would take a computer more than 1,000 years to crack but isn't too long to type?\nRemember that your password is harder to guess if it's :\n     1.Long\n     2.Not a word in the dictionary\n     3.Contains letters,numbers & punctuation\nYou're going to generate passwords that are hard for a computer to crack.\nThese are useful for protecting important accounts.\nNote that many adults use a password manager program to help them remember lots of tricky passwords.",
         fg="black",
         justify=LEFT).pack()

Label(top, text="", font="Helvetica 9").pack()

#intro_text
title = StringVar()
label = Label(top, textvariable=title, anchor=N, pady=10).pack()
title.set("Password strength:")

#choice_part
def sel():
    selection = choice.get()

choice = IntVar()
R1 = Radiobutton(top, text="BASIC", variable=choice, value=1, command=sel).pack(anchor=CENTER)
R2 = Radiobutton(top, text="MEDIUM", variable=choice, value=2, command=sel).pack(anchor=CENTER)
R3 = Radiobutton(top, text="Strong", variable=choice, value=3, command=sel).pack(anchor=CENTER)
labelchoice = Label(top)
labelchoice.pack()

#pass lenght information
lenlabel = StringVar()
lenlabel.set("Password length:")
lentitle = Label(top, textvariable=lenlabel).pack()

#pass lenght number
val = IntVar()
spinlenght = Spinbox(top, from_=6, to_=20, textvariable=val, width=13).pack()

#password_print
def callback():
    lsum.config(text=passgen())

#button
Btn=Button(top, text="Generate Password", relief=RIDGE, bd=5, height=2, command=callback, pady=3).pack()
password=str(callback)

#password result message
lsum = Label(top, text="")
lsum.pack(side=BOTTOM)

#function
lownum = string.ascii_uppercase + string.ascii_lowercase + string.digits
lowupp = string.ascii_uppercase + string.ascii_lowercase
symbols = """~!@#$%&*()_-+={}[]\|:;<>?/"""
everything = lowupp + lownum + symbols

def passgen():
    if choice.get() == 1:
        return "".join(random.sample(lowupp, val.get()))
    elif choice.get() == 2:
        return "".join(random.sample(lownum, val.get()))
    elif choice.get() == 3:
        return "".join(random.sample(everything, val.get()))

top.mainloop()
