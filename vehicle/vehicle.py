import random
from land import Land
from numpy import array
from methods import *
import street


import pygame

class Vehicle(pygame.sprite.Sprite):
    def __init__(self,streetID,land:Land):
        pygame.sprite.Sprite.__init__(self)
        self.__carImage = pygame.image.load("Images/car01.png") #Cargar imagen
        self.__carImage = pygame.transform.scale(self.__carImage,scale_rect(1,self.__carImage.get_rect().size,(land.streetList[streetID].widht,0),0) ) #escalo al 10% del tamaño de la pantalla el auto
        #print(self.__carImage.get_rect().size)
        #print(land.streetList[streetID].widht)
        self.__streetID=streetID
        self.__streetPercent=random.randint(0,100)/100.0
        self.__relativeMax= (random.randint(66,133)*land.streetList[streetID].maxSpeedLimit)/100 #respeto de la velocidad de los conductores
        self.__speed=random.randint(0,int(round(self.__relativeMax*(land.streetList[streetID].maxSpeedLimit)))) #velocidad del vehiculo al comenzar
        self.__aceletation=random.randint(4,10) #aceleracion del vehiculo
        self.__lane=random.randint(1,land.streetList[streetID].lanes)
        self.__direction=self.__initial_direction(land.streetList[streetID].yDir)
        self.__position=self.__initial_position(land.streetList[streetID].begining,land.streetList[streetID].end,land.streetList[streetID].lanes,land.streetList[streetID].widht)
        
        #print("desplazo: ",(a+desp)*land.streetList[streetID].widht*0.8)                        
        angle=angle_between_vector(self.__yDirection,(0,1))
        self.__carImage=pygame.transform.rotate(self.__carImage,90)
        self.__carImage=pygame.transform.rotate(self.__carImage,-1*angle)
        self.__rect=self.__carImage.get_rect()
        
        print(self.__position)
               

        self.__rect.center= self.__position
        #self.__rect.center = self.__position
        #print('posición :',self.__position)
        #print('carImage :',self.__carImage)
        #print('Rect :',self.__rect)
        #print('center :',self.__rect.center)
        #print('left :',self.__rect.center.left)
        
        
        
    # Method
    def __initial_direction(self,streetYDriection):
       self.__yDirection=streetYDriection
       self.__xDirection=streetYDriection[1],-streetYDriection[0]
       
       return [self.__xDirection,self.__yDirection]
       
    def __initial_position(self,streetOrigin,streetEnd,lanes,steetWidht):
        initialPosition=array(self.__yDirection)*vector_longitud((array(streetEnd)-array(streetOrigin)))*self.__streetPercent+array(streetOrigin)
        desp=int((lanes/2)-self.__lane)
        
        if((lanes%2)>0):
            a=0
            
            #print ("impar: ")
        else:
            a=0.5
           
            #print ("par: ")
        initialPosition=initialPosition+(a+desp)*steetWidht*0.9*array(self.__xDirection)
        return initialPosition
    def draw(self,surface):
        surface.blit(self.__carImage,self.__rect)
    def basic_move(self,street,lanes):
        
        escala=100#variable a definir globalmente
        pixelPerFrame=int(self.__speed/escala)
        if pixelPerFrame<1:
            pixelPerFrame=1

        position=(array(self.__position)+pixelPerFrame*array(self.__direction[1]))
        laneModifier=(int(abs(lanes/2)-self.lane)+1)*street.widht
        print(laneModifier)

        if laneModifier*1.5*module(self.__direction[1])<module(position-array(street.end)):
            
            self.__position=tuple(position)
            self.__rect.center= self.__position

        
        
        #print('left :',self.__carImage.left)
    # Properties
    @property
    def length(self):
        return self.__carImage.size[0]
    @property
    def width(self):
        return self.__carImage.size[1]
    @property
    def position(self):
        return self.__position
    @property
    def lane(self):
        return self.__lane
    @property
    def streetID(self):
        return self.__streetID
    @property
    def streetPercent(self):
        return self.__streetPercent