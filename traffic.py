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
            a=circle_and_segment_intercection(x.begining,x.end,mousePosition,60)
            
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


traffic=Traffic(800,600)
pygame.init() # inicializar pygame (OBLIGATORIO) para usar los recursos de pygame
windowsSize=(traffic.size)
window=pygame.display.set_mode(windowsSize) #seteo ventana
pygame.display.set_caption("Traffic Simulator") #nombre de ventana

cars=False
click=False
lanes=1
clickNumber=-1
currentStreet=False
predict=True
while True:
    window.fill((30,180,40))#recibe tupla con RGB
    #Control de eventos
    for evento in pygame.event.get():
        if evento.type==QUIT: #¿es el evento de apretar la cruz?
            pygame.quit() #Si==>cerrar los procesos de pygame
            sys.exit() #y cerrar ventana
        if evento.type==KEYDOWN:
            if cars==False:
                if evento.key==pygame.K_q and clickNumber==-1:
                    print('car will be placed')
                    cars=True
                if evento.key==pygame.K_w:
                    if clickNumber==1:
                        lanes+=1
            if evento.key==pygame.K_e:
                    predict=False
        if evento.type==KEYUP:
            if evento.key==pygame.K_e:
                predict=True
        if cars==False:
            if evento.type==pygame.MOUSEBUTTONDOWN:
                click=True
                pos1=traffic.magnetStreet(pygame.mouse.get_pos(),clickNumber)
                clickNumber=clickNumber*-1
                if clickNumber==-1:
                    lanes=1
                  
                    
    if predict == True:
        pos2=traffic.magnetStreet(pygame.mouse.get_pos(),clickNumber)
    else:
        pos2=pygame.mouse.get_pos()
    if clickNumber==1 :
        print('la posición dos vale: ' ,pos2)
        traffic.streetAppend(pos1,pos2,click,lanes)
        click=False
    
        
    if cars==True:
        traffic.vehicleAppend(3)
        cars=False
        traffic.intersections()

    
    

    for street in traffic.streetList:
        street.draw(window)
    for car in traffic.vehicleList:
        car.draw(window)
    #Actualizar contenido de ventana
    pygame.display.update()