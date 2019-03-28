import random as rnd

import stock.statistik.tools as stat_tools


def drunken_pirates(n=5, times=1000):
	"""
	sheet 1 exercise 1
	:param n: number of pirates
	:param times: how often the method should be repeated
	:return: average number of correct lying in the correct bed
	"""
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


def collectibles(n, times=1):
	"""
	sheet 1 exercise 2 :param n: number of total pictures :param times: how often the method should repeat :return: (
	array with entries how many pictures it takes to get from i to i+1 different pictures, number of total pictures it
	takes to get a full set)
	"""
	cards = range(n)
	array = [times] * n
	for _ in range(times):
		is_collected = [False] * n
		for k in cards:
			choice = rnd.choice(cards)
			while is_collected[choice]:
				choice = rnd.choice(cards)
				array[k] += 1
			is_collected[k] = True
	for i in range(len(array)):
		array[i] = array[i] / times
	return array, sum(array)


def calculations(table=None):
	"""
	sheet 1 exercise 3
	calculates arithmetic mean, geometric mean, harmonic mean, median
	:param table:	raw data table
	:return: (calculates arithmetic mean, geometric mean, harmonic mean, median)
	"""
	if table is None:
		table = [16, 10, 6.5, 7, 3, 6, 7, 5, 5.5, 4, 7]
	arith_mean = stat_tools.arithmetic_mean(table)
	geom_mean = stat_tools.geometric_mean(table)
	harm_mean = stat_tools.harmonic_mean(table)
	median = stat_tools.median(table)
	return arith_mean, geom_mean, harm_mean, median
