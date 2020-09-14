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
    def __init__(self, width, height,streetQuantity):
        self.__vertex=((0,0),(width,0),(width,height),(0,height))
        self.__streetList=[]
        for x in range(streetQuantity):
            self.__streetList.append(Street(x,(random.randint(0,width),(random.randint(0,height))),(random.randint(0,width),(random.randint(0,height))),(random.randint(1,4))))
    
    @property
    def streetList(self):
        return self.__streetList