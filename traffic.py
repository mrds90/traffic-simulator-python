from vehicle import Vehicle
from street import Street
import methods
from land import Land
import random
import visual
from visual import *


class Traffic:
    
    def __init__(self,cars,width, height,streetQuantity):
        self.__land=Land(width,height,streetQuantity)
        self.__cars:list=[]
        for x in range(streetQuantity):
            print("street ",x,':')
            print(" start: ",self.__land.streetList[x].begining)
            print(" max speed limit: ",self.__land.streetList[x].maxSpeedLimit)
        
        for y in range(cars):
            self.__cars.append((Vehicle(random.randint(0,len(self.__land.streetList)-1),self.__land)))
            print('initial position: ',self.__cars[y].position)



Traffic(5,1000,800,11)

