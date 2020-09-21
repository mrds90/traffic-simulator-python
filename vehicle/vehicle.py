import random
from land import Land
from numpy import array
from methods import *
from street import Street


import pygame

class Vehicle(pygame.sprite.Sprite):
    def __init__(self,street:Street,lane):
        pygame.sprite.Sprite.__init__(self)
        self.__carImage = pygame.image.load("Images/car01.png") #Cargar imagen
        self.__carImage = pygame.transform.scale(self.__carImage,scale_rect(1,self.__carImage.get_rect().size,(street.widht,0),0) ) #escalo al 10% del tamaño de la pantalla el auto
        self.__street=street
        self.__streetID=street.id
        self.__streetPercent=random.randint(0,80)/100.0
        self.__relativeMax= random.randint(66,133)/100 #respeto de la velocidad de los conductores
        self.__speed=random.randint(30,int(round(self.__relativeMax*(street.lane(lane).maxSpeedLimit)))) #velocidad del vehiculo al comenzar
        print('velocidad del vehiculo: ',self.__speed)
        self.__aceletation=random.randint(4,10) #aceleracion del vehiculo
        self.__lane=lane
        self.__direction=self.__initial_direction()
        self.__position=self.set_position(self.__lane)
        
        #print("desplazo: ",(a+desp)*land.streetList[streetID].widht*0.8)                        
        angle=angle_between_vector(self.__yDirection,(0,1))
        self.__carImage=pygame.transform.rotate(self.__carImage,90)
        self.__carImage=pygame.transform.rotate(self.__carImage,-1*angle)
        self.__rect=self.__carImage.get_rect()
        
        #print(self.__position)
               

        self.__rect.center= self.__position
        #self.__rect.center = self.__position
        #print('posición :',self.__position)
        #print('carImage :',self.__carImage)
        #print('Rect :',self.__rect)
        #print('center :',self.__rect.center)
        #print('left :',self.__rect.center.left)
        
        
        
    # Method
    def __initial_direction(self):
       self.__yDirection=self.__street.lane(self.__lane).yDir
       self.__xDirection=self.__street.lane(self.__lane).xDir
       
       return [self.__xDirection,self.__yDirection]
       
    def set_position(self,lane):
        position=array(self.__yDirection)*module((array(self.__street.lane(lane).end)-array(self.__street.lane(lane).begining)))*self.__streetPercent+array(self.__street.lane(lane).begining)
        return position

    def draw(self,surface):
        surface.blit(self.__carImage,self.__rect)
    def basic_move(self,street,lanes):
        
        escala=10#variable a definir globalmente
        pixelPerFrame=int(self.__speed/escala)
        #print(pixelPerFrame)
        if pixelPerFrame<1:
            pixelPerFrame=1

        position=(array(self.__position)+pixelPerFrame*array(self.__direction[1]))
        
        if module(pixelPerFrame)<module(position-array(self.__street.lane(self.__lane).end)):
            
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