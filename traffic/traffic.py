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
        #self.b=0
    
    def vehicleAppend(self,vehicle):
        for y in range(vehicle):
            self.__vehicle.append((Vehicle(random.randint(0,len(self.__land.streetList)-1),self.__land)))
    def move(self):
        pygame.time.delay(50)
        for y in self.__vehicle:
            y.basic_move(self.streetList[y.streetID],self.streetList[y.streetID].lanes)
    def intersections(self):
        self.__land.intersect_point()
        """
        a=len(self.__land.intercetion)
        if a>self.b:
            print('lista')
            for x in self.__land.intercetion:
                print(x)
            self.b=a
        """  
        

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
            for x in self.__land.intercetion:
                a=pointOnACircle(x,mousePosition,25)
                
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

    def magnetHorizontalAndVertical(self,mousePosition,clickNumber):
        if clickNumber==1:
            clickNumber=0
        b=[]
        c=[]
        d=[]
        e=[]
        matchHorizontal=False
        matchVertical=False
        for x in self.streetList[0:len(self.streetList)-1-clickNumber]:
            horizontal=pointOnACircle((x.begining[0],mousePosition[1]),mousePosition,30)
            horizontal1=pointOnACircle((x.end[0],mousePosition[1]),mousePosition,30)
            vertical=pointOnACircle((mousePosition[0],x.begining[1]),mousePosition,30)
            vertical1=pointOnACircle((mousePosition[0],x.end[1]),mousePosition,30)
            if horizontal!=None:
                b.append(horizontal)
                c.append(float(module(array(horizontal)-array(mousePosition))))
                matchHorizontal=True
            if horizontal1!=None:
                b.append(horizontal1)
                c.append(float(module(array(horizontal1)-array(mousePosition))))
                matchHorizontal=True
            if vertical!=None:
                d.append(vertical)
                e.append(float(module(array(vertical)-array(mousePosition))))
                matchVertical=True
            if vertical1!=None:
                d.append(vertical1)
                e.append(float(module(array(vertical1)-array(mousePosition))))
                matchVertical=True

        if matchHorizontal==True and matchVertical==True:
            horizontal=b[c.index(min(c))]  
            vertical=d[e.index(min(e))]  
            return (horizontal[0],vertical[1])
        elif matchHorizontal==True and matchVertical==False:
            horizontal=b[c.index(min(c))]
            return horizontal  
        elif matchHorizontal==False and matchVertical==True:
            vertical=d[e.index(min(e))]
            return vertical
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


