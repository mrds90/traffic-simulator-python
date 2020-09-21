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
            
            self.__streetList.append(Street(len(self.__streetList)-1,positionOne,positionTwo,lanes,self.__streetWidht))
        elif clickOne==False:
            """ if predict==True:
                for x in range(len(self.__streetList)):
                    for y in range(x+1,len(self.__streetList)):
                        if len(self.__streetList)>1:
                            positionTwo=predictIntersectPoint(self.__streetList[x].begining,self.__streetList[x].end,positionOne,positionTwo)
                """     
            self.__streetList[len(self.__streetList)-1].end=positionTwo
            self.__streetList[len(self.__streetList)-1].lanes=lanes
        #print(len(self.__streetList)-1)
    
    def intersect_point(self):
        self.__intersections=[]
        b=[]
        for x in range(len(self.__streetList)):
            for y in range(x+1,len(self.__streetList)):
                a=getIntersectPoint(self.__streetList[x].begining,self.__streetList[x].end,self.__streetList[y].begining,self.__streetList[y].end)
                if a!=None:
                    b.append(a)
        res = [] 
        if (len(b)>0):
            for i in b: 
                if i not in res: 
                    res.append(i)
                    self.__intersections.append(Intersection(i,self.__streetList))

                    #print ('interseccion ',self.__intersectionón '':'',self.__intersection[len(self.__intersection)-1])
                


    @property
    def streetList(self):
        return self.__streetList
    @property
    def size(self):
        return self.__size
    @property
    def intersections(self):
        return self.__intersections
    