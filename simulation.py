import world as w
import robot as r
import pyrosim.pyrosim as pyrosim
import pybullet as p
import pybullet_data
import constants as c
import time as t

class SIMULATION:
    def __init__(self):
        # connect to pybullet
        self.physicsClient = p.connect(p.GUI)
        # adds floor to sim
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        # adds gravity force for sim
        p.setGravity(0, 0, -9.8)
       
        self.world = w.WORLD()
        self.robot = r.ROBOT()
    
    def Run():
        for i in range(c.loop):
            p.stepSimulation()
        	# # adds sensor from back leg
            # backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
            # frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
            
        	# # motor for torso - backleg joint
            # pyrosim.Set_Motor_For_Joint(bodyIndex= robotId, jointName="Torso_BackLeg", controlMode= p.POSITION_CONTROL, targetPosition= backLegTargetAngles[i], maxForce= 100)
            # pyrosim.Set_Motor_For_Joint(bodyIndex= robotId, jointName="Torso_FrontLeg", controlMode= p.POSITION_CONTROL, targetPosition= frontLegTargetAngles[i], maxForce= 100)

            print(i)
            t.sleep(1/60)
