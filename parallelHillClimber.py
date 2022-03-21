from solution import SOLUTION
import constants as c
import copy
import os

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        # These are supposed to remove any files with this name but it wont work for some reason
        os.system("rm brain*.nndf")
        os.system("rm fitness*.txt")

        self.nextAvailableID = 0
        self.parents = {}
        for i in range(0, c.populationSize - 1):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1
    
    def Evolve(self):
        self.Evaluate(self.parents)
        for i in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()
    
    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select()

    def Spawn(self):
        self.children = {}

        for i in range(len(self.parents)):
            self.children[i] = copy.deepcopy(self.parents[i])
            self.children[i].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1

    def Mutate(self):
        for i in range(len(self.children)):
            self.children[i].Mutate()

    def Select(self):
        for i in range(len(self.parents)):
            if self.children[i].fitness < self.parents[i].fitness:
                self.parents[i] = self.children[i]
    
    def Print(self):
        for i in range(len(self.parents)):
            print("Parents Fitness: " + str(self.parents[i].fitness) + " Child Fitness: " + str(self.children[i].fitness))

    def Evaluate(self, solutions):
        for i in range(len(solutions)):
            solutions[i].Start_Simulation("DIRECT")

        for i in range(len(solutions)):
            solutions[i].Wait_For_Simulation_To_End()

    def Show_Best(self):
        best = 50
        best_key = 0
        for i in self.parents:
            if self.parents[i].fitness < best:
                best_key = i
                best = self.parents[i].fitness
        
        self.parents[best_key].Start_Simulation("GUI")
        print(best)
