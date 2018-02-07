def buttons():
	top = Button(c)
	top.place(x =100, y=100)
	top["text"] = "^"
	top["command"] = mtop

	left = Button(c)
	left.place(x =130, y=130)
	left["text"] = ">"
	left["command"] = mleft
	
	down = Button(c)
	down.place(x =100, y=160)
	down["text"] = "\/"
	down["command"] = mdown

	right = Button(c)
	right.place(x =70, y=130)
	right["text"] = "<"
	right["command"] = mright
def mtop():
	c.move(rect,0,-2)
def mleft():
	c.move(rect,2,0)
def mdown():
	c.move(rect,0,2)
def mright():
	c.move(rect,-2,0)
	
from Tkinter import *
master = Tk()
c = Canvas(master, width=460,height=200,bg='grey80')
c.pack()
x=50
y=50
rect = c.create_rectangle(x,y,x+20,y+20,fill="blue",outline="blue")
buttons()

mainloop()