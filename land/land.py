# singletonImplement

import random
from street import Street

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
        
    
    def append(self,positionOne,PositionTwo,clickOne,lanes:int):
        if clickOne==True:
            self.__streetList.append(Street(len(self.__streetList)-1,positionOne,PositionTwo,lanes,self.__streetWidht))
        elif clickOne==False:
            self.__streetList[len(self.__streetList)-1].end=PositionTwo
            self.__streetList[len(self.__streetList)-1].lanes=lanes
        #print(len(self.__streetList)-1)
    
    @property
    def streetList(self):
        return self.__streetList
    @property
    def size(self):
        return self.__size

    
    