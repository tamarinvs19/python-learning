from time import sleep
import nxt.locator

FREQ_C = 523
FREQ_D = 587
FREQ_E = 659
FREQ_G = 784

b = nxt.locator.find_one_brick()
for i in range(50, 80):
	b.play_tone_and_wait(i*10, 400)
sleep(0.5)
