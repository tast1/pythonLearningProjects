from tkinter import *
from tkinter import ttk

root = Tk()

frame = Frame(root)

LableText = text="Manybutons"
Lable = LableText
Lable(frame, LableText).pack()

Button(frame, text="B1").pack(side=LEFT, fill=Y)
Button(frame, text="B2").pack(side=LEFT, fill=Y)
Button(frame, text="B3").pack(side=LEFT, fill=Y)
Button(frame, text="B4").pack(side=LEFT, fill=Y)

frame.pack()



root.mainloop()
