import pyrosim.pyrosim as pyrosim
import pybullet as p
import pybullet_data
import sensor as s
import motor as m

class ROBOT:
    def __init__(self):
        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
    
    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = s.SENSOR(linkName)
    
    def Sense(self, t):
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName].Get_Value(t)
    
    def Prepare_To_Act(self):
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = m.MOTOR(jointName)
    
    def Act(self, t):
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName].Set_Values(self.robotId, t)
