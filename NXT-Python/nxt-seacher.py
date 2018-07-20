
from nxt.brick import Brick
from nxt.locator import find_one_brick
from nxt.motor import Motor, PORT_A, PORT_B, PORT_C
from nxt.sensor import Ultrasonic
from nxt.sensor import PORT_4

from time import sleep


def dist(ultrasonic):
	return ultrasonic.get_sample()
def drive(wheels, time, direction = 1):
	for motor in wheels:
		motor.run(power = 90*direction)
	sleep(time)
	for motor in wheels:
		motor.idle()
def phizic(eyes,wheels,ultrasonic):
	command =''
	#print(1)
	while command != 'stop' :
		command = str(input())
		if command in ('d', 'dist'):
			print(dist(ultrasonic))
		if command in ('dr', 'drive'):
			print( 'Write time and direction ')
			time, direction = input()
			drive(wheels,time, direction)

def main ():
	b = find_one_brick()
	eyes = Motor(b, PORT_A)
	wheels = [Motor(b, PORT_B), Motor(b, PORT_C)]
	ultrasonic = Ultrasonic(b, PORT_4)
	
	phizic(eyes,wheels,ultrasonic)
main()