import random as rnd


def drunken_pirates(n, times):
	correct = 0
	for _ in range(times):
		beds = [None] * n
		free_beds = list(range(n))
		for k in range(n):
			tmp: int = rnd.choice(free_beds)
			free_beds.remove(tmp)
			# noinspection PyTypeChecker
			beds[tmp] = k
		for index, ele in enumerate(beds):
			if index == ele:
				correct += 1
	return correct / times


