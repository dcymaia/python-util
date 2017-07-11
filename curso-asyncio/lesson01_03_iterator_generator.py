import random


def lancar_dados(n):
	for i in range(0, n):
		yield random.randint(1, 6)


for dado in lancar_dados(10):
	print(dado)		