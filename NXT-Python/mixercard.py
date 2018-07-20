import nxt.locator
from nxt.motor import *
from nxt.sensor import *
from time import sleep
from random import randint

def WaitForCompletion(mc, port):
	while not mc.is_ready(port):
			pass
def change_deck( b, direction = 1): 
	'''
	direction = 1 -> to right
	direction = -1 -> to left
	'''
	
	if direction == 1:
		touch = Touch(b, PORT_2)
	if direction ==-1:
		touch = Touch(b, PORT_1)
	
	mc.set_output_state(PORT_B,70*direction, 0)
	mc.set_output_state(PORT_C,-30, 0)
	while not touch.is_pressed():
		pass
	mc.set_output_state(5, 0 , 0)
	b.play_tone_and_wait(239, 500)
	
def move_card(mc, d ):
	'''
	d = 1 -> out
	d = -1 -> in
	'''
	
	if d ==1:
		portin = PORT_C
		portout = PORT_A
	if d ==-1:
		portin = PORT_A
		portout = PORT_C
	m = Motor(b, portout)
	m.reset_position(False)
	interout = 460
	interin = 490
	mc.cmd(portout,-1*40, interout, 1,1,1)
	while  abs(m.get_tacho().rotation_count) - 240  < -10:
		#print(m.get_tacho().rotation_count)
		if abs(m.get_tacho().rotation_count) > 240:
			break
	mc.cmd(portin,40, interin, 1,1,1)
	WaitForCompletion(mc, portin)
	
def one_to_two(b, mc):
	global deck_left, deck_right
	deck_left = 0 
	deck_right = 0
	e = Color20(b, PORT_3)
	mc.start()
	last=0
	while e.get_color() != 2:
		new = randint(0,1)
		if new == 0:
			deck_left += 1
		else:
			deck_right += 1
		if last == new :
			pass
		elif new == 0:
			change_deck( b, -1)
		elif new == 1:
			change_deck(b, 1)
		last = new
		move_card(mc, 1)
		sleep(0.1)
		#print (e.get_color())
	mc.stop()
def close_deck( b, mc, deck):
	mc.start()
	for i in range(0, deck):
		move_card(mc , -1)
		sleep(0.1)
	mc.stop()
global deck_left, deck_right

b = nxt.locator.find_one_brick()
mc = b.mc
one_to_two(b, mc)
mc.start()
change_deck( b, -1)
mc.stop()
close_deck(b , mc, deck_left)
mc.start()
change_deck( b, 1)
mc.stop()
close_deck(b , mc, deck_right)


