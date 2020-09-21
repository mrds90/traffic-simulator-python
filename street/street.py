from methods import versor_from_two_points
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
                a=0.5
           
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


    def lane(self,id):
        return self.__lanes[id]
    
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
                print('velocidad maxima de carril: ',self.__maxSpeedLimit)

                self.__widht=widht

        except ValueError:
            print ('posiciones ingresadas incorrectamente')


    def draw(self,surface):
        pygame.draw.line(surface, (100,100,100), self.begining, self.end,self.__widht)
    
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

          
    


