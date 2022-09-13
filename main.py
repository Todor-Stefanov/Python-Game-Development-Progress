from tkinter import *


def hello(event):
    print("Hello world!")


root = Tk()
btn = Button(root, text="Click me.")
btn.bind("<Button-1>", hello)

btn.pack()
root.mainloop()