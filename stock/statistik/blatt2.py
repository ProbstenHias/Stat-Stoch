import math

import pandas as pd


def grosse_kisten(path):
	df = pd.read_csv(path)

	jahr = df["Jahr"].tolist()

	flops = df["FLOPS"].tolist()
	flops_log = [math.log(i, 10) for i in flops]
