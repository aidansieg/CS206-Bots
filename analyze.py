from cProfile import label
import numpy as np
import matplotlib.pyplot as pp

# loads vector data from files
backLegData = np.load("data/backLegSensorValues.npy")
frontLegData = np.load("data/frontLegSensorValues.npy")

# plots vector data and assigns labels
backLegPlot = pp.plot(backLegData, label="Back Leg Data")
frontLegPlot = pp.plot(frontLegData, label="Front Leg Data")

# initializes legend for labels
pp.legend()

# displays graph
pp.show()
