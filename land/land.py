# singletonImplement

import random
from methods import *
from street import *

class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Land(metaclass=SingletonMeta):
    def __init__(self, width, height):
        self.__size=(width,height)
        self.__streetList:Street=[]
        self.__streetWidht=int(self.size[0]*0.03)
        self.__intersections:list=[]
        
    
    def street_append(self,positionOne,positionTwo,clickOne,lanes:int):
        if positionOne==positionTwo:
            positionTwo=tuple(array(positionTwo)+[1,1])
        if clickOne==True: 
            self.__streetList.append(Street(len(self.__streetList),positionOne,positionTwo,lanes,self.__streetWidht))
        elif clickOne==False:
            self.__streetList[len(self.__streetList)-1].end=positionTwo
            self.__streetList[len(self.__streetList)-1].lanes=lanes
    
                
    def get_intersections(self):                   
        intersectionList=[]
        for street in self.__streetList:
            for lane in street.laneList:
                if len(lane.intersectionList)>0:
                    print('the street ', street.id ,'in lane',street.laneList.index(lane), 'have ',len(lane.intersectionList),'intersections')
                    for intesection in lane.intersectionList:
                        if intesection not in intersectionList:
                            intersectionList.append(intesection)
                        print('the intesection', lane.intersectionList.index(intesection),'have',len(intesection.posiblesDirection), 'way outs')
                        
        if len(intersectionList)==0:
            print('there is no intersections')
        return intersectionList
    
    def update_intersections(self):
        print('updating intersections ...')
        for street in self.streetList:
            street.update_intersections(self.streetList)
        self.__intersections=self.get_intersections()

    


    @property
    def streetList(self):
        return self.__streetList
    @property
    def size(self):
        return self.__size
    @property
    def intersections(self):
        return self.__intersections
    