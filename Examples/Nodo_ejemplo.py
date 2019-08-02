#!/usr/bin/env python
from tkinter import *

from PIL import Image, ImageTk

master = Tk()
master.geometry("1280x720")

def callback():
    #print "click!"
    load = Image.open("hola.jpg")
    load = load.resize((250, 250), Image.ANTIALIAS)
    render = ImageTk.PhotoImage(load)
    img = Label( image=render)
    img.image = render
    img.place(x=0, y=0)

def callback2():
    #print "click!"
    load = Image.open("hud.png")
    render = ImageTk.PhotoImage(load)
    img = Label( image=render)
    img.image = render
    img.place(x=0, y=0)




a = Button(master, text="hola", command=callback2)
b = Button(master, text="OK", command=callback)
b.pack()
a.pack()

mainloop()

root = Tk()
app = Window(root)
root.wm_title("Tkinter window")
root.geometry("1000x1000")
root.mainloop()
