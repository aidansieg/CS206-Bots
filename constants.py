import numpy as np

# front leg constants
frontLegAmplitude = 1
frontLegFrequency = 10
frontLegPhaseOffset = 0

# back leg constants
backLegAmplitude = np.pi / 4
backLegFrequency = 10
BackLegPhaseOffset = 0

loop = 1000
gravity = -9.8
sleep = 1/240

bottomAngleRange = 0
topAngleRange = 2 * np.pi

maxForce = 20