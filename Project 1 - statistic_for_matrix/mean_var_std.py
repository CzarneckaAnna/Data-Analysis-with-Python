import numpy as np
import statistics as stat

def calculate(list):

	try:
		data = np.array(list).reshape(3,3)
	except ValueError:
		print("List must contain nine numbers.")
	else:
		calculations = {
			"mean" : [np.mean(data, axis=0), np.mean(data, axis=1), np.mean(data)],
			"variance": [np.var(data, axis=0), np.var(data, axis=1), np.var(data)],
			"standard deviation": [np.std(data, axis=0), np.std(data, axis=1), np.std(data)],
			"max": [np.max(data, axis=0), np.max(data,axis=1), np.max(data)],
			"min": [np.min(data, axis=0), np.min(data,axis=1), np.min(data)],
			"sum": [np.sum(data, axis=0), np.sum(data, axis=1), np.sum(data)]
		}
	
		return calculations