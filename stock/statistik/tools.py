from functools import reduce
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def arithmetic_mean(table):
	return sum(table) / len(table)


def geometric_mean(table):
	return reduce((lambda x, y: x * y), table) ** (1 / len(table))


def harmonic_mean(table):
	return len(table) / sum(1 / i for i in table)


def median(table):
	if len(table) % 2 == 0:
		mid = len(table) // 2
		return (table[mid] + table[mid - 1]) / 2
	else:
		return table[len(table) // 2]


def empiric_distribution():
	pass


def emp_varianz(table):
	x = arithmetic_mean(table)
	return sum((i - x) for i in table) / len(table)


def stichp_varianz(table):
	x = arithmetic_mean(table)
	return sum((i - x) for i in table) / (len(table) - 1)


def quartile(table, p):
	n_times_p = len(table) * p
	if (n_times_p) % 1 == 0:
		n_times_p = int(n_times_p)
		return (table[n_times_p - 1] + table[n_times_p]) / 2
	else:
		return table[int(n_times_p)]


def interquartile_range(table, p1, p2):
	return abs(quartile(table, p1) - quartile(table, p2))


def fence(table, p1, p2):
	_range = interquartile_range(table, p1, p2)
	return quartile(table, p1) - 1.5 * _range, quartile(table, p2) + 1.5 * _range

