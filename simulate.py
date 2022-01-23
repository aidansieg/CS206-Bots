import pybullet as p
import pybullet_data
import time

physicsClient = p.connect(p.GUI)

# adds floor to sim
p.setAdditionalSearchPath(pybullet_data.getDataPath())
planeId = p.loadURDF("plane.urdf")

# adds gravity force for sim
p.setGravity(0, 0, -9.8)

p.loadSDF("boxes.sdf")

for i in range(2000):
	p.stepSimulation()
	time.sleep(1/60)
	print(i)

p.disconnect()
