from methods import versor_from_two_points
import random
import pygame


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
                self.__lanes=lanes
                self.__yDir=tuple(versor_from_two_points(self.__begining,self.__end))
                self.__xDir=tuple([self.__yDir[1],-1*self.__yDir[0]])
                self.__maxSpeedLimit=10*random.randint(3,9)
                self.__widht=widht

        except ValueError:
            print ('posiciones ingresadas incorrectamente')
            
    def draw(self,surface):
        pygame.draw.line(surface, (100,100,100), self.begining, self.end,self.__lanes*self.__widht)


            
    
    @property
    def lanes(self):
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
    @property
    def maxSpeedLimit(self):
        return self.__maxSpeedLimit

          
    

