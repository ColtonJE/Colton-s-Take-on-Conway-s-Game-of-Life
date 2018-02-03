from tkinter import *

master = Tk()
canvas = Canvas(None)
v = StringVar()
t = StringVar()
label = Label(canvas, text='')
label1 = Label(canvas, text='')
canvas.pack()
label.pack()
label1.pack()
master.mainloop()

while 1:
    width = canvas.cget('width')
    height = canvas.cget('height')
    v.set(str(width))
    t.set(str(height))
    label.config(textvariable= v)
    label1.config(textvariable= t)
    master.update()


