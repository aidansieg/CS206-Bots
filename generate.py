import pyrosim.pyrosim as pyrosim

# set dimensions of box
length = 1
width = 1
height = 1

pyrosim.Start_SDF("boxes.sdf")

#pyrosim.Send_Cube(name="Box", pos=[0,0,0.5], size=[length,width,height])
pyrosim.Send_Cube(name="Box2", pos=[2.5,2.5,0.5], size=[6,6,1])
for x in range(6):
    length = 1
    width = 1
    height = 1
    for y in range(6):
        length = 1
        width = 1
        height = 1
        for i in range(10):
            length = length * 0.9
            width = width * 0.9
            height = height * 0.9
            pyrosim.Send_Cube(name="Box", pos=[x,y,i+1.5], size=[length,width,height])
            

pyrosim.End()