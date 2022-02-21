import pybullet as p
import pybullet_data
import constants as c
import numpy as np
import pyrosim.pyrosim as pyrosim
class MOTOR:
    def __init__(self, jointName) -> None:
        self.jointName = jointName
        self.Prepare_To_Act()
    
    def Prepare_To_Act(self):
        self.amplitude = c.backLegAmplitude
        self.frequency = c.backLegFrequency
        self.offSet = c.BackLegPhaseOffset

        if(self.jointName == "Torso_BackLeg"):
            self.targetAngles = self.amplitude * (np.sin((self.frequency / 2) * np.array(np.linspace(c.bottomAngleRange, c.topAngleRange, c.loop)) + self.offSet))
        else:
            self.targetAngles = self.amplitude * (np.sin(self.frequency * np.array(np.linspace(c.bottomAngleRange, c.topAngleRange, c.loop)) + self.offSet))
        
    def Set_Values(self, robot, t):
        pyrosim.Set_Motor_For_Joint(bodyIndex= robot, jointName= self.jointName, controlMode= p.POSITION_CONTROL, targetPosition= self.targetAngles[t], maxForce= c.maxForce)
    
    def Save_Values(self):
        np.save("data/motorValues.npy", self.targetAngles)