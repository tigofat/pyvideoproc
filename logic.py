import random

def shuffle(list, number):
	for i in range(number):
		index1 = random.randint(0, len(list) - 1)
		index2 = random.randint(0, len(list) - 1)
		list[index1], list[index2] = list[index2], list[index1]
