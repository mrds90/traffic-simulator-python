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
        self.__street=street
        self.__streetPercent=randint(0,80)/100.0
        self.__lane=lane
        self.__relativeMax= randint(76,133)/100 #respeto de la velocidad de los conductores
        self.__set_speed()
        print('velocidad del vehiculo: ',self.__speed)
        self.__aceletation=randint(4,10) #aceleracion del vehiculo
        self.__direction=self.__initial_direction()
        self.__position=self.set_position(self.__lane)
        self.__load_image()
        



    def __set_speed(self):
        self.__speed=randint(20,int(round(self.__relativeMax*self.__street.laneList[self.__lane].maxSpeedLimit))) #velocidad del vehiculo al comenzar
        
        
    def __load_image(self):
        self.__carImage = pygame.image.load("Images/car01.png") #Cargar imagen
        self.__carImage = pygame.transform.scale(self.__carImage,scale_rect(1,self.__carImage.get_rect().size,(self.__street.widht,0),0) ) #escalo al 10% del tamaño de la pantalla el auto
        self.__set_image_orientation((-1,0))

    def __set_image_orientation(self,originalDirection):    
        #print("desplazo: ",(a+desp)*land.streetList[streetID].widht*0.8)                        
        angle=angle_between_vector(self.__yDirection,originalDirection)
        
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
    def pixel_per_frame(self):
        pixelPerFrame=(self.__speed/self.__escala)
        #print(pixelPerFrame)
        if pixelPerFrame<1:
            pixelPerFrame=1
        return pixelPerFrame

    def basic_move(self,intersection):
    
        advance=1
        if intersection==True:
            advance=2
        pixelPerFrame=self.pixel_per_frame()
        position=(array(self.__position)+advance*pixelPerFrame*array(self.__yDirection))
    
        if (pixelPerFrame)<module(self.__position-array(self.__street.laneList[self.__lane].end)) or intersection==True:
            self.__position=tuple(position)
            self.__rect.center= self.__position
           
   

    
    def intersection_move(self):
        pixelPerFrame=self.pixel_per_frame()
        posiblesIntersections=[]
        distanceList=[]
        match=False
        for intersection in self.street.laneList[self.__lane].intersectionList:
            
            point=pointOnACircle(intersection.position,self.__position,pixelPerFrame)
            # print('interseccion:',intersection.position,'pixel por frame:',self.position,pixelPerFrame,'match?:',point,'final de la calle:',self.__street.laneList[self.__lane].end)
            if point!=None:
                # print(point)
                posiblesIntersections.append(intersection)
                distanceList.append(module(array(point)-array(self.__position)))
                match=True
        
        if match==True:
            intersection=posiblesIntersections[distanceList.index(min(distanceList))]

            if intersection.posiblesDirection!=[]:
                print ('posibles salidas :', len(intersection.posiblesDirection))

                choice=randint(0,len(intersection.posiblesDirection)-1)

                print('selecciono:',choice)
                print('calle actual:',id(intersection.posiblesDirection[choice].street))
                print('calle seleccionada:',id(self.__street))
                
                originalDirection=self.__yDirection
                self.__street=intersection.posiblesDirection[choice].street
                self.__lane=intersection.posiblesDirection[choice].laneNumber
                self.__yDirection=self.__street.laneList[self.__lane].yDir

                # print(originalDirection,self.__yDirection)

                start=self.__street.laneList[self.__lane].begining
                end=self.__street.laneList[self.__lane].end
                self.__position=intersection.position
                if self.__yDirection!=originalDirection:
                    self.__load_image()
                self.__set_speed()
        return match

                
                
                
    def move(self):
        
        self.basic_move(self.intersection_move())
        
        
        
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