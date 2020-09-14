import random
from land import Land
from numpy import array
from methods import vector_longitud


class Vehicle:
    def __init__(self,streetID,land):
        self.__length= 4.0
        self.__streetID=streetID
        self.__streetPercent=random.randint(0,100)/100.0
        self.__relativeMax= (random.randint(66,133)*land.streetList[streetID].maxSpeedLimit)/100 #respeto de la velocidad de los conductores
        self.__speed=random.randint(0,int(round(self.__relativeMax*(land.streetList[streetID].maxSpeedLimit)))) #velocidad del vehiculo al comenzar
        self.__aceletation=random.randint(4,10) #aceleracion del vehiculo
        self.__lane=random.randint(1,land.streetList[streetID].lanes)
        self.__direction=self.__initial_direction(land.streetList[streetID].yDir)
        self.__position=self.__initial_position(land.streetList[streetID].begining,land.streetList[streetID].end)

    # Method
    def __initial_direction(self,streetYDriection):
       self.yDirection=streetYDriection
       return self.yDirection
    def __initial_position(self,streetOrigin,streetEnd):
       initialPosition=array(self.yDirection)*vector_longitud((array(streetEnd)-array(streetOrigin)))*self.__streetPercent+array(streetOrigin)
       return initialPosition

    # Properties
    @property
    def length(self):
        return self.__length
    @property
    def width(self):
        return self.__width
    @property
    def position(self):
        return self.__position
    @property
    def lane(self):
        return self.__lane
    @property
    def streetID(self):
        return self.__streetID
    @property
    def streetPercent(self):
        return self.__streetPercent