from email.mime import base
import os
import pyrosim.pyrosim as pyrosim
import pybullet as p
import pybullet_data
import sensor as s
import motor as m
from pyrosim.neuralNetwork import NEURAL_NETWORK
import constants as c

class ROBOT:    
    def __init__(self, solutionID):
        self.solutionID = solutionID
        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        self.nn = NEURAL_NETWORK("brain{}.nndf".format(solutionID))
        os.system("rm brain{}.nndf".format(self.solutionID))
    
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
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName) * c.motorJointRange
                self.motors[jointName].Set_Values(self.robotId, desiredAngle)

                # print(neuronName, jointName, desiredAngle)

    def Think(self):
        self.nn.Update()
        # self.nn.Print()

    def Get_Fitness(self):
        basePositionAndOrientation = p.getBasePositionAndOrientation(self.robotId)
        basePosition = basePositionAndOrientation[0]
        xPosition = basePosition[0]

        f = open("tmp{}.txt".format(self.solutionID), "w")
        f.write(str(xPosition))
        os.system("mv tmp{}.txt fitness{}.txt".format(self.solutionID, self.solutionID))
        f.close()