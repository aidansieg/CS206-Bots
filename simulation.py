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
        p.setGravity(0, 0, c.gravity)
       
        self.world = w.WORLD()
        self.robot = r.ROBOT()
    
    def Run(self):
        for time in range(c.loop):
            p.stepSimulation()
            self.robot.Sense(time)
            self.robot.Think()
            self.robot.Act(time)
        	
            t.sleep(c.sleep)
        
    def __del__(self):
        p.disconnect()
