import numpy as np
import pyrosim.pyrosim as pyrosim
import constants as c
class SENSOR:
    def __init__(self, linkName) -> None:
        self.linkName = linkName
        self.values = np.zeros(c.loop)
    
    def Get_Value(self, t):
        self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
    
    def Save_Values(self):
        np.save("data/sensorData.npy")