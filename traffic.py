from vehicle import Vehicle
from street import Street
from methods import *
from land import Land
from numpy import array
import random
import pygame, sys
from pygame.locals import *

class Traffic:
    
    def __init__(self,width, height):
        self.__land=Land(width,height)
        self.__vehicle:list=[]
        
    
    def vehicleAppend(self,vehicle):
        for y in range(vehicle):
            self.__vehicle.append((Vehicle(random.randint(0,len(self.__land.streetList)-1),self.__land)))

    def intersections(self)      :
        self.__land.intersect_point()

    def streetAppend(self,positionOne,positionTwo,clickOne,lanes:int):
        self.__land.append(positionOne,positionTwo,clickOne,lanes)

    def magnetStreet(self,mousePosition,clickNumber):
        if clickNumber==1:
            clickNumber=0
        b=[]
        c=[]
        match=False
        for x in self.streetList[0:len(self.streetList)-1-clickNumber]:
            a=circle_and_segment_intercection(x.begining,x.end,mousePosition,30)
            
            if a!=None:
                
                b.append(a)
                c.append(float(module(array(a)-array(mousePosition))))
                match=True
            
        if match==True:
            a=b[c.index(min(c))]  
            return a
        else:
            return mousePosition
        print('devuelvo None')    

    def magnetStreetIntercetion(self,mousePosition):
        #if len(self.__land.intercetion)>0:

            b=[]
            c=[]
            match=False
            for x in self.__land.intercetion[0:len(self.streetList)-1]:
                a=pointOnACircle(x,mousePosition,20)
                
                if a!=None:
                    
                    b.append(a)
                    c.append(float(module(array(a)-array(mousePosition))))
                    match=True
                
            if match==True:
                a=b[c.index(min(c))]  
                return a
            return mousePosition
    
    def magnetStreetLimits(self,mousePosition,clickNumber):
        if clickNumber==1:
            clickNumber=0
        b=[]
        c=[]
        match=False
        for x in self.streetList[0:len(self.streetList)-1-clickNumber]:
            a=pointOnACircle(x.begining,mousePosition,30)
            a1=pointOnACircle(x.end,mousePosition,30)
            if a!=None:
                
                b.append(a)
                c.append(float(module(array(a)-array(mousePosition))))
                match=True
            if a1!=None:
                b.append(a1)
                c.append(float(module(array(a1)-array(mousePosition))))
                match=True

        if match==True:
            a=b[c.index(min(c))]  
            return a
        else:
            return mousePosition
        print('devuelvo None') 


    @property
    def vehicleList(self):
        return self.__vehicle
    @property
    def streetList(self):
        return self.__land.streetList
    @property
    def size(self):
        return self.__land.size
    



#print('posición de auto: ',traffic.vehicleList[0].position)


