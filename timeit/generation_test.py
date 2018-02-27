def one():
	xs = []
	for i in range(10):
		if i % 2 == 0 and i**4 < 100:
			xs.append(i)
def two():
	xs = [i for i in range(10) if i % 2 == 0 and i**4 < 100]
	
def one_r():
	xs = []
	for i in range(10):
		if i % 2 == 0 and i**4 < 100:
			xs.append(i)
def two_r():
	xs = [i for i in range(10)if i % 2 == 0 and i**4 < 100]