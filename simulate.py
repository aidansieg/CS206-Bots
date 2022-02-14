from cmath import pi
import pyrosim.pyrosim as pyrosim
import pybullet as p
import pybullet_data
import time
import random
import numpy as np

physicsClient = p.connect(p.GUI)

# adds floor to sim
p.setAdditionalSearchPath(pybullet_data.getDataPath())
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")

# adds gravity force for sim
p.setGravity(0, 0, -9.8)

p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)

x = np.linspace(0, 2 * pi, 1000)

frontLegAmplitude = pi/4
frontLegFrequency = 10
frontLegPhaseOffset = 5
frontLegTargetAngles = frontLegAmplitude * np.sin(frontLegFrequency * x + frontLegPhaseOffset)

backLegAmplitude = pi/4
backLegFrequency = 15
BackLegPhaseOffset = pi/4
backLegTargetAngles = backLegAmplitude * np.sin(backLegFrequency * x + BackLegPhaseOffset)

backLegSensorValues = np.zeros(1000)
frontLegSensorValues = np.zeros(1000)

# np.save("data/targetAngles.npy", targetAngles)
# exit()

for i in range(1000):
	p.stepSimulation()
	# adds sensor from back leg
	backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
	frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
	
	# motor for torso - backleg joint
	pyrosim.Set_Motor_For_Joint(bodyIndex= robotId, jointName="Torso_BackLeg", controlMode= p.POSITION_CONTROL, targetPosition= backLegTargetAngles[i], maxForce= 100)
	pyrosim.Set_Motor_For_Joint(bodyIndex= robotId, jointName="Torso_FrontLeg", controlMode= p.POSITION_CONTROL, targetPosition= frontLegTargetAngles[i], maxForce= 100)

	print(i)
	time.sleep(1/60)

np.save("data/backLegSensorValues.npy", backLegSensorValues)
np.save("data/frontLegSensorValues.npy", frontLegSensorValues)

p.disconnect()
