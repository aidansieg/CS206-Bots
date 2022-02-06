import pyrosim.pyrosim as pyrosim
import pybullet as p
import pybullet_data
import time
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

backLegSensorValues = np.zeros(300)
frontLegSensorValues = np.zeros(300)

for i in range(300):
	p.stepSimulation()
	# adds sensor from back leg
	backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
	frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
	print(i)
	time.sleep(1/60)

np.save("data/backLegSensorValues.npy", backLegSensorValues)
np.save("data/frontLegSensorValues.npy", frontLegSensorValues)

p.disconnect()
