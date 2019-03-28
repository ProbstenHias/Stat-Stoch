import itertools
import os

import math
import pandas as pd

import stock.statistik.tools as stat_tools

data_folder = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + "/files/"


def contingency_table():
	"""
	sheet 2 exercise 1a
	:return:
	"""

	dataframe = pd.read_excel(data_folder + "2.1.xlsx")
	# dataframe.set_index(["Informatiker", "Softwaretechniker", ""])
	print(dataframe.to_string())


def mediziner_stat():
	"""
	sheet 2 excise 3
	:return:
	"""
	k = [10, 8, 10, 16]
	print("arithmetisches Mittel: %s" % stat_tools.arithmetic_mean(k))
	print("empirische Varianz: %s" % stat_tools.empirical_variance(k))
	stichproben = itertools.permutations("ABCD", 2)
	print("alle zweielementigen Stichproben ohne zuruecklegen mit reihenfolge:")
	print(list(stichproben))


mediziner_stat()
