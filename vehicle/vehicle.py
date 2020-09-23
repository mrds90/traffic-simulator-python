from random import randint
from land import Land
from numpy import array
from methods import *
from street import Street
from street import Intersection


import pygame

class Vehicle(pygame.sprite.Sprite):
    def __init__(self,street:Street,lane):
        pygame.sprite.Sprite.__init__(self)
        self.__escala=10#variable a definir globalmente
        self.__carImage = pygame.image.load("Images/car01.png") #Cargar imagen
        self.__carImage = pygame.transform.scale(self.__carImage,scale_rect(1,self.__carImage.get_rect().size,(street.widht,0),0) ) #escalo al 10% del tamaño de la pantalla el auto
        self.__street=street
        self.__streetPercent=randint(0,80)/100.0
        self.__relativeMax= randint(66,133)/100 #respeto de la velocidad de los conductores
        self.__speed=randint(30,int(round(self.__relativeMax*(street.laneList[lane].maxSpeedLimit)))) #velocidad del vehiculo al comenzar
        print('velocidad del vehiculo: ',self.__speed)
        self.__aceletation=randint(4,10) #aceleracion del vehiculo
        self.__lane=lane
        self.__direction=self.__initial_direction()
        self.__position=self.set_position(self.__lane)
        self.__set_image_orientation()

    def __set_image_orientation(self):    
        #print("desplazo: ",(a+desp)*land.streetList[streetID].widht*0.8)                        
        angle=angle_between_vector(self.__yDirection,(0,1))
        self.__carImage=pygame.transform.rotate(self.__carImage,90)
        self.__carImage=pygame.transform.rotate(self.__carImage,-1*angle)
        self.__rect=self.__carImage.get_rect()
        self.__rect.center= self.__position
        #print(self.__position)
               

        
        #self.__rect.center = self.__position
        #print('posición :',self.__position)
        #print('carImage :',self.__carImage)
        #print('Rect :',self.__rect)
        #print('center :',self.__rect.center)
        #print('left :',self.__rect.center.left)
        
        
        
    # Method
    def __initial_direction(self):
       self.__yDirection=self.__street.laneList[self.__lane].yDir
       self.__xDirection=self.__street.laneList[self.__lane].xDir
       
       return [self.__xDirection,self.__yDirection]
       
    def set_position(self,lane):
        position=array(self.__yDirection)*module((array(self.__street.laneList[lane].end)-array(self.__street.laneList[lane].begining)))*self.__streetPercent+array(self.__street.laneList[lane].begining)
        return position

    def draw(self,surface):
        surface.blit(self.__carImage,self.__rect)
    def basic_move(self,street,lanes):
        
        
        pixelPerFrame=int(self.__speed/self.__escala)
        #print(pixelPerFrame)
        if pixelPerFrame<1:
            pixelPerFrame=1

        position=(array(self.__position)+pixelPerFrame*array(self.__yDirection))
        
        if module(pixelPerFrame)<module(position-array(self.__street.laneList[self.__lane].end)):
            
            self.__position=tuple(position)
            self.__rect.center= self.__position
    
    def intercection_move(self,intercection:Intersection):
        
        print ('posibles salidas :', len(intercection.posiblesDirection))
        streetIndex=randint(0,len(intercection.posiblesDirection)-1)
            
        
        
        laneIndex=randint(0,intercection.posiblesDirection[streetIndex].lanes-1)
        
        
        self.__street=intercection.posiblesDirection[streetIndex]
        self.__lane=laneIndex
        self.__yDirection=self.__street.laneList[self.__lane].yDir
        start=self.__street.laneList[self.__lane].begining
        end=self.__street.laneList[self.__lane].end
        center=self.__position
        radius=int(self.__speed/self.__escala)
        posisition=array(circle_and_segment_intercection(start,end,center,2*radius))
        print(posisition)
        self._position=tuple(intercection.position)
        self.__set_image_orientation()

        
        
        
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
    def street(self):
        return self.__street
    @property
    def streetPercent(self):
        return self.__streetPercent
    @property
    def speed(self):
        return self.__speed