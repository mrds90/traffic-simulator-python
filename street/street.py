from methods import *
import random
import pygame
from numpy import array


class Street (pygame.sprite.Sprite):
    __begining:tuple
    __end:tuple
    __lanes:int
    __yDir:tuple
    __xDir:tuple

    def __init__(self,streetID,begining:tuple,end:tuple,lanes:int,widht):
        try:
            if (len(begining) !=2 or len(end) !=2):
                raise ValueError
            else:
                self.__streetID=streetID
                self.__begining=begining
                self.__end=end
                self.__lanes=[]
                self.__yDir=tuple(versor_from_two_points(self.__begining,self.__end))
                self.__xDir=tuple([self.__yDir[1],-1*self.__yDir[0]])
                self.__maxSpeedLimit=10*random.randint(3,9)
                self.__widht=widht
                self.laneCalculator(lanes)
                
                
        except ValueError:
            print ('posiciones ingresadas incorrectamente')

    def laneCalculator(self, lanes):
        self.__lanes=[]
        for x in range(lanes):
            desp=int((lanes/2))-range(lanes).index(x)
        
            if((lanes%2)>0):
                a=0
            
                #print ("impar: ")
            else:
                a=-0.5
           
            #print ("par: ")
            begining=self.begining-(a+desp)*self.__widht*array(self.__xDir)
            end=self.__end-(a+desp)*self.__widht*array(self.__xDir)
            x=Lane(range(lanes).index(x),begining,end,self.__maxSpeedLimit,self.__widht)
            self.__lanes.append(x)
            

 
    def draw(self,surface):
        for lane in self.__lanes:
            lane.draw(surface)
         
    
    @property
    def lanes(self):
        return len(self.__lanes)
    @lanes.setter
    def lanes(self,lanes):
        self.laneCalculator(lanes)
    @property
    def laneList(self):
        return self.__lanes
    @property
    def widht(self):
        return self.__widht
    @property
    def yDir(self):
        return self.__yDir 
    @property
    def xDir(self):
        return self.__xDir 
    @property
    def id(self):
        return self.__streetID
    @property
    def begining(self):
        return self.__begining
    @property
    def end(self):
        return self.__end
    @end.setter
    def end(self,valor):
        self.__end=valor
        self.__yDir=tuple(versor_from_two_points(self.__begining,self.__end))
        self.__xDir=tuple([self.__yDir[1],-1*self.__yDir[0]])

    @property
    def maxSpeedLimit(self):
        return self.__maxSpeedLimit

          
    
class Lane (pygame.sprite.Sprite):
    __begining:tuple
    __end:tuple
    __yDir:tuple
    __xDir:tuple

    def __init__(self,laneNumber,begining:tuple,end:tuple,streetSpeed,widht):
        try:
            if (len(begining) !=2 or len(end) !=2):
                raise ValueError
            else:
                self.__laneNumber=laneNumber
                self.__begining=begining
                self.__end=end
                self.__yDir=tuple(versor_from_two_points(self.__begining,self.__end))
                self.__xDir=tuple([self.__yDir[1],-1*self.__yDir[0]])
                self.__maxSpeedLimit=streetSpeed+20*laneNumber
                #print('velocidad maxima de carril: ',self.__maxSpeedLimit)
                self.__widht=widht
                self.__intersectionList=[]

        except ValueError:
            print ('posiciones ingresadas incorrectamente')


    def draw(self,surface):
        pygame.draw.line(surface, (100,100,100), self.begining, self.end,self.__widht)
    
    def add_intersection(self,intersection):
        repeat=False
        for aux in self.__intersectionList:
            
            if list(map(int, intersection.position))==list(map(int, aux.position)):
                repeat=True
                aux=intersection
            else:
                print(intersection.position,aux.position)
        
        if repeat==False:
            self.__intersectionList.append(intersection)


    @property
    def widht(self):
        return self.__widht
    @property
    def yDir(self):
        return self.__yDir 
    @property
    def xDir(self):
        return self.__xDir 
    @property
    def laneNumber(self):
        return self.__laneNumber
    @property
    def begining(self):
        return self.__begining
    @begining.setter
    def behining(self,valor):
        self.__begining=valor
        self.__yDir=tuple(versor_from_two_points(self.__begining,self.__end))
        self.__xDir=tuple([self.__yDir[1],-1*self.__yDir[0]])
    @property
    def end(self):
        return self.__end
    
    @end.setter
    def end(self,valor):
        self.__end=valor
        self.__yDir=tuple(versor_from_two_points(self.__begining,self.__end))
        self.__xDir=tuple([self.__yDir[1],-1*self.__yDir[0]])
    
    @property
    def maxSpeedLimit(self):
        return self.__maxSpeedLimit
    @property
    def intersectionList(self):
        return self.__intersectionList

          
    


class Intersection:
    def __init__(self,position,streetList):
        
        self.__position=position
        self.__streetListOut=[]
        self.__streetListIn=[]
        for street in streetList:
            self.streetCheck(street)
    
    def __eq__(self, other): 
        if not isinstance(other, Intersection):
            # don't attempt to compare against unrelated types
            return NotImplemented
        

        return self.position == other.__position and self.__streetListOut == other.__streetListOut and self.__streetListIn == other.__streetListIn
    
    def streetCheck(self,street):
        #print('checking streets involves')
        a=circle_and_segment_intercection(street.begining,street.end,self.__position,street.widht)
        
        if a!=None:
            self.set_ouputs_streets(street)
            self.set_inputs_streets(street)
            
    def set_inputs_streets(self,street):
        if street.end!=self.__position:
            self.__streetListIn.append(street)
        res = [] 
        for i in self.__streetListIn: 
            if i not in res: 
                res.append(i)
        self.__streetListIn=res
    def set_ouputs_streets(self,street):
        #print('finding posible outs')
        if street.begining!=self.__position:
            self.__streetListOut.append(street)
        res = [] 
        for i in self.__streetListOut: 
            if i not in res: 
                res.append(i)
        self.__streetListOut=res
        #print(len(self.__streetListIn), ' posible outs' )
    

    @property
    def posiblesDirection(self):
        return self.__streetListOut
    @property
    def position(self):
        return self.__position

                


    