import random

def loading_(i):
	symbols = ['▁', '▂', '▃', '▄', '▅', '▆', '▇', '▆', '▅', '▄', '▃', '▂']
	if i < len(symbols) - 1:
		i += 1
	else:
		i = 0
	return symbols[i], i

def shuffle(list, number):
	for i in range(number):
		index1 = random.randint(0, len(list) - 1)
		index2 = random.randint(0, len(list) - 1)
		list[index1], list[index2] = list[index2], list[index1]
