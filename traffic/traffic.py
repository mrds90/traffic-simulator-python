from vehicle import *
from street import Street
from methods import *
from land import Land
from numpy import array
from random import randint
import pygame, sys
from pygame.locals import *

class Traffic:
    
    def __init__(self,width, height):
        self.__vehicle:list=[]
        #self.b=0
    
    def vehicleAppend(self,vehicle,streetList):
        try:
            if streetList==[]:
                raise ValueError
            else:
                for y in range(vehicle):
                    if len(streetList)>1:
                        street=streetList[randint(0,len(streetList)-1)]
                    else:
                        street=streetList[0]
                    if street.lanes>1:
                        lane=randint(0,street.lanes-1)
                    else:
                        lane=0

                    self.__vehicle.append(Vehicle(street,lane))
        except ValueError:
            print ('there is no streets')

    def run(self,streetList,intersectionList):
        pygame.time.delay(50)
        

        for y in self.__vehicle:
            for intersection in intersectionList:
                aux=pointOnACircle(intersection.position,y.position,int(y.speed/10))
                print (aux)
                if aux!=None:
                    y.intercection_move(intersection)

                y.basic_move(streetList[y.street.id],streetList[y.street.id].lanes)
    
 
    @property
    def vehicleList(self):
        return self.__vehicle


    



#print('posición de auto: ',traffic.vehicleList[0].position)


