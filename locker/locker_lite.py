from tkinter import Tk, Entry, Label, Button
from time import sleep

root = Tk()
root.title("Locker")
root.attributes('-fullscreen', True)
label = Label(root, text="Сделай пререрыв!!", font="Iosevka 60")
label.grid(column=8, row=4)
button = Button(root, text="ОК", command=root.destroy)
button.grid(column=1, row=0) 
root.update()
root.mainloop()

