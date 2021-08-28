from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("Python Clock")

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)
    
label = Label(root, font=("Comic Sans MS", 20), background = "black", foreground = "white")
label.pack(anchor= "center")
time()

mainLoop()