from functools import reduce


def arithmetic_mean(table):
	"""
	calculates the arithmetic mean
	:param table: raw data table
	:return: arithmetic mean
	"""
	return sum(table) / len(table)


def geometric_mean(table):
	"""
	calculates the geometric mean
	:param table: raw data table
	:return: geometric mean
	"""
	return reduce((lambda x, y: x * y), table) ** (1 / len(table))


def harmonic_mean(table):
	"""
	calculates the harmonic mean
	:param table: raw data table
	:return: harmonic mean
	"""
	return len(table) / sum(1 / i for i in table)


def median(table):
	"""
	calculates the median
	:param table: raw data table
	:return: median
	"""
	if len(table) % 2 == 0:
		mid = len(table) // 2
		return (table[mid] + table[mid - 1]) / 2
	else:
		return table[len(table) // 2]


def empiric_distribution():
	"""draws a graph for the empiric distribution
	Work in progress"""
	pass


def empirical_variance(table):
	"""
	calculates the empirical variance
	:param table: raw data table
	:return: empirical variance
	"""
	x = arithmetic_mean(table)
	return sum((i - x) for i in table) / len(table)


def sampling_variance(table):
	"""
	calculates the sampling variance
	:param table: raw data table
	:return: sampling variance
	"""
	x = arithmetic_mean(table)
	return sum((i - x) for i in table) / (len(table) - 1)


def quartile(table, p):
	"""
	calculates a quartile
	:param table: raw data table
	:param p: percentage
	:return: quartile
	"""
	n_times_p = len(table) * p
	if n_times_p % 1 == 0:
		n_times_p = int(n_times_p)
		return (table[n_times_p - 1] + table[n_times_p]) / 2
	else:
		return table[int(n_times_p)]


def interquartile_range(table, p1, p2):
	"""
	calculates interquartile range
	:param table: raw data table
	:param p1: lower percentage
	:param p2: upper percentage
	:return: interquartile range
	"""
	return abs(quartile(table, p1) - quartile(table, p2))


def fence(table, p1, p2):
	"""
	calculates the fence for a boxplot
	:param table: raw data table
	:param p1: lower percentage
	:param p2: upper percentage
	:return: fence
	"""
	_range = interquartile_range(table, p1, p2)
	return quartile(table, p1) - 1.5 * _range, quartile(table, p2) + 1.5 * _range


def chi_squared_coefficient(array):
	"""
	WORK IN PROGRESS
	:param array:  3-dimensional array in the form:
	[ [lower_edge_1, ..., lower_edge_n], [right_edge_1, ..., right_edge_n]
	:param n: total number
	:return:
	"""
	h_thingies = []
	n = sum(array[1])
	for _ in array[1]:
		h_thingies.append([])
	for i, right in enumerate(array[1]):
		for lower in array[0]:
			h_thingies[i].append((right * lower) / n)
	sum_ = 0
	for index1, ele1 in enumerate(array[0]):
		for index2, ele2 in enumerate(array[1]):
			sum += ()
