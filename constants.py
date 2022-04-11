import numpy as np

# front leg constants
frontLegAmplitude = 1
frontLegFrequency = 10
frontLegPhaseOffset = 0

# back leg constants
backLegAmplitude = np.pi / 4
backLegFrequency = 10
BackLegPhaseOffset = 0

loop = 2500
gravity = -9.8
sleep = 1/60
numberOfGenerations = 10
populationSize = 10

valueErr = -0.23615654831547395

motorJointRange = 0.2

numSensorNeurons = 9
numMotorNeurons = 8

bottomAngleRange = 0
topAngleRange = 2 * np.pi

maxForce = 50