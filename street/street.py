import weakref
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
            x=Lane(range(lanes).index(x),begining,end,self)
            self.__lanes.append(x)
            
    def update_intersections(self,streetList):
        for lane in self.laneList:
            for street in streetList:
                if street!=self:
                    lane.update_intersections(street.laneList)


 
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

    def __init__(self,laneNumber,begining:tuple,end:tuple,street:Street):
        try:
            if (len(begining) !=2 or len(end) !=2):
                raise ValueError
            else:
                self.__street= street #got parent
                self.__laneNumber=laneNumber
                self.__begining=begining
                self.__end=end
                self.__maxSpeedLimit=street.maxSpeedLimit+20*laneNumber
                #print('velocidad maxima de carril: ',self.__maxSpeedLimit)
                self.__intersectionList=[]

        except ValueError:
            print ('posiciones ingresadas incorrectamente')
    
    def __eq__(self, item):
        try:
            if isinstance(item, Lane):
                return list(self.__begining) == list(item.begining) and list(self.__end) == list(item.end)
        except TypeError:
            return NotImplemented


        

    
    def draw(self,surface):
        pygame.draw.line(surface, (180,180,180), self.begining, self.end,self.__street.widht)
    
    def update_intersections(self, laneList):
        
        for lane in laneList:
            a=getIntersectPoint(self.begining,self.end,lane.begining,lane.end)
            if a!=None:
                
                repeat = False   
                for intersection in self.__intersectionList:
                    if module(array(a)-array(intersection.position))<self.widht: # repeat if the distance between intersection is less than lane widht
                        if lane not in (intersection.posiblesDirection + intersection.inputLanes):
                            intersection.update(lane)
                        repeat=True
                if repeat==False:
                    self.__intersectionList.append(Intersection(a,lane,self))
                        
    
    @property
    def street (self):
        return self.__street
    @property
    def widht(self):
        return self.__street.widht
    @property
    def yDir(self):
        return self.__street.yDir 
    @property
    def xDir(self):
        return self.__street.xDir 
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
    def __init__(self,position,lane,parent):
        self.__lane = parent
        self.__position=position
        self.__laneListOut=[]
        self.__laneListIn=[]
        self.update(parent)
        self.update(lane)
    
    def __eq__(self, other): 
        if not isinstance(other, Intersection):
            # don't attempt to compare against unrelated types
            return NotImplemented
       

        return self.position == other.__position and self.__laneListOut == other.__laneListOut and self.__laneListIn == other.__laneListIn
    def update(self,lane):
        if self.lane_check:
            if (not self.set_ouputs_lanes(lane)):
                self.set_inputs_lanes(lane)
        else:
            print('not an intersection of current lane')

    def lane_check(self,lane):
        #print('checking streets involves')
        a=circle_and_segment_intercection(lane.begining,lane.end,self.__position,lane.widht)
        if a!=None:
            return True    
        else:
            return False
          
    def set_inputs_lanes(self,lane):
        if lane not in (self.__laneListIn + self.__laneListOut):
            if pointOnACircle (lane.end,self.__position,3)!=None:
                self.__laneListIn.append(lane)
                return True
        else:
            print("lane is already in current intersection")
            return False

    def set_ouputs_lanes(self,lane:Lane):
        #print('finding posibles outs')
        if lane not in (self.__laneListIn + self.__laneListOut):
            
            if pointOnACircle (lane.end,self.__position,3)==None:
                self.__laneListOut.append(lane)
                return True
            else:
                return False
        else:
            print("lane is already in current intersection")
            return False

      

    @property
    def posiblesDirection(self):
        return self.__laneListOut
    @property
    def inputLanes(self):
        return self.__laneListIn
    @property
    def position(self):
        return self.__position

                


    