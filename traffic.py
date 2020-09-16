from vehicle import Vehicle
from street import Street
import methods
from land import Land
import random
import pygame, sys
from pygame.locals import *

class Traffic:
    
    def __init__(self,vehicle,width, height,streetQuantity):
        self.__land=Land(width,height,streetQuantity)
        self.__vehicle:list=[]
        for y in range(vehicle):
            self.__vehicle.append((Vehicle(random.randint(0,len(self.__land.streetList)-1),self.__land)))
            

    @property
    def vehicleList(self):
        return self.__vehicle
    @property
    def streetList(self):
        return self.__land.streetList
    @property
    def size(self):
        return self.__land.size


traffic=Traffic(15,800,600,4)
#print('posición de auto: ',traffic.vehicleList[0].position)



"""for x in range(len(traffic.streetList)):
    print("street ID ",x,':')
    print(" start: ",traffic.streetList[x].begining)
    print(" max speed limit: ",traffic.streetList[x].maxSpeedLimit)
    print(" lanes: ",traffic.streetList[x].lanes)"""


pygame.init() # inicializar pygame (OBLIGATORIO) para usar los recursos de pygame
windowsSize=(traffic.size)
window=pygame.display.set_mode(windowsSize) #seteo ventana
pygame.display.set_caption("Traffic Simulator") #nombre de ventana


while True:
    window.fill((255,255,255))#recibe tupla con RGB
    #Control de eventos
    for evento in pygame.event.get():
        if evento.type==QUIT: #¿es el evento de apretar la cruz?
            pygame.quit() #Si==>cerrar los procesos de pygame
            sys.exit() #y cerrar ventana
    
    for street in traffic.streetList:
        street.draw(window)
    for car in traffic.vehicleList:
        car.draw(window)
    #Actualizar contenido de ventana
    pygame.display.update()