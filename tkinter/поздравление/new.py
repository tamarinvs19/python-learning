from tkinter import *
def ja1():
	global master
	import pyglet 
	s = pyglet.media.load('Имперский марш.wav')
	s.play()
def il():
	global master
	import pyglet 
	s = pyglet.media.load('The Imperial Suite.wav')
	s.play()
def bc():
	global c,master, rect1,rect2,t1,t2,button1
	c.delete(rect1, rect2,t1,t2)
	button1.pack_forget()
	
	c.create_text(200,90,text="Поздравляю \n с днем рождения! ",
          font="GentiumAlt 20",justify=CENTER,fill="#00008b")
	c.create_text(200,160,text="Да пребудет с тобой\n сила!",
          font="Carlito 22",justify=CENTER,fill="#ff9900")
	ja = Button(master,text='I am your father',width=35,height=1,bg='#b2ec5d',
				  fg='red',font='Verdana 12', command = ja1)
	ja.pack()
	sil = Button(master,text='Сила течёт во мне, и я един с силой',width=35,height=1,bg='#7fc7ff',
				  fg='red',font='Verdana 12', command = il)
	sil.pack()
def st1():
	global master
	master.destory()
def st():
	global c, master, rect1,rect2,t1,t2, button1
	
	rect = c.create_rectangle(50, 50, 350, 350,fill="#adffff",outline="blue")
	rect1 = c.create_rectangle(185, 50, 215, 350,fill="#1ca9c9",outline="blue")
	rect2 = c.create_rectangle(50, 185, 350, 215,fill="#1ca9c9",outline="blue")
	t1 = c.create_text(110,70,text="Папе", 
			  font="GentiumAlt 25",justify=CENTER,fill="#009900")
	t2 = c.create_text(280,330,text="От Славы",
			  font="GentiumAlt 15",justify=CENTER,fill="red")
	button1=Button(master,text='Открыть',width=10,height=1,bg='#ffd700',
				   fg='#800080',font='Carlito 13', command = bc)
	button1.pack()
	
global c, master
master = Tk()
master.title('Папе')
c = Canvas(master, width=400,height=400,bg='grey90' )
c.pack()
st()
mainloop()