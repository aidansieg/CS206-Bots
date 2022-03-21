from asyncore import read
from random import weibullvariate
import numpy as np
import pyrosim.pyrosim as pyrosim
import random
import os
import time
import constants as c

class SOLUTION:
    def __init__(self, nextAvailableID):
        self.weights = np.random.rand(3,2)
        self.weights = self.weights * 2 - 1
        self.myID = nextAvailableID
    
    def Start_Simulation(self, type):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()

        strID = str(self.myID)
        os.system("python3 simulate.py {} {}".format(type, strID) + " &")

    def Wait_For_Simulation_To_End(self):
        strID = str(self.myID)

        fitnessFileName = "fitness{}.txt".format(strID)

        while not os.path.exists("fitness{}.txt".format(strID)):
            time.sleep(0.01)

        f = open(fitnessFileName)

        temp = f.readline()

        try:
            self.fitness = float(temp)

        except ValueError:
            self.fitness = c.valueErr
            
        f.close()

        os.system("rm fitness{}.txt".format(strID))
        
    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")

        pyrosim.Send_Cube(name="Box", pos=[-5,2,0.5], size=[1,1,1])        

        pyrosim.End()

    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")

        pyrosim.Send_Cube(name="Torso", pos=[1.5,0,1.5], size=[1,1,1])

        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[1,0,1])
        
        pyrosim.Send_Cube(name="BackLeg", pos=[-0.5,0,-0.5], size=[1,1,1]) 

        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[2,0,1])

        pyrosim.Send_Cube(name="FrontLeg", pos=[0.5,0,-0.5], size=[1,1,1])

        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain{}.nndf".format(self.myID))

        pyrosim.Send_Sensor_Neuron(name= 0, linkName= "Torso")
        pyrosim.Send_Sensor_Neuron(name= 1, linkName= "BackLeg")
        pyrosim.Send_Sensor_Neuron(name= 2, linkName= "FrontLeg")
        pyrosim.Send_Motor_Neuron(name= 3, jointName= "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name= 4, jointName= "Torso_FrontLeg")
        
        for currentRow in range(3):
            for currentColumn in range(2):
                pyrosim.Send_Synapse(sourceNeuronName= currentRow, targetNeuronName= currentColumn + 3, weight= self.weights[currentRow][currentColumn])

        pyrosim.End()
    
    def Mutate(self):
        randomRow = random.randint(0, 2)
        randomColumn = random.randint(0, 1)

        self.weights[randomRow, randomColumn] = (2 * np.random.rand()) - 1
    
    def Set_ID(self, id):
        self.myID = id
