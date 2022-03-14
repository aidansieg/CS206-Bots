from cmath import pi
import pyrosim.pyrosim as pyrosim
import pybullet as p
import pybullet_data
import time
import random
import numpy as np
import constants as c
from simulation import SIMULATION
import sys

directOrGUI = sys.argv[1]
simulation = SIMULATION(directOrGUI)
simulation.Run()
simulation.Get_Fitness()