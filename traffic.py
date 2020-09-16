from vehicle import Vehicle
from street import Street
import methods
from land import Land
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
            

    def streetAppend(self,positionOne,PositionTwo,clickOne,lanes:int):
        self.__land.append(positionOne,PositionTwo,clickOne,lanes)

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
while True:
    window.fill((255,255,255))#recibe tupla con RGB
    #Control de eventos
    for evento in pygame.event.get():
        if evento.type==QUIT: #¿es el evento de apretar la cruz?
            pygame.quit() #Si==>cerrar los procesos de pygame
            sys.exit() #y cerrar ventana
        if evento.type==KEYDOWN:
            if cars==False:
                if evento.key==pygame.K_ESCAPE:
                    print('car will be placed')
                    cars=True
                if evento.key==pygame.K_u:
                    if clickNumber==1:
                        lanes+=1
        if cars==False:
            if evento.type==pygame.MOUSEBUTTONDOWN:
                click=True
                pos1=pygame.mouse.get_pos()
                clickNumber=clickNumber*-1
                if clickNumber==-1:
                    lanes=1
                  
                    
            
    pos2=pygame.mouse.get_pos()
    if clickNumber==1 :
        traffic.streetAppend(pos1,pos2,click,lanes)
        click=False
    if cars==True:
        traffic.vehicleAppend(3)
        cars=False


    for street in traffic.streetList:
        street.draw(window)
    for car in traffic.vehicleList:
        car.draw(window)
    #Actualizar contenido de ventana
    pygame.display.update()