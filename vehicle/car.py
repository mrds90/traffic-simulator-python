import random

class Car:

    def __init__(self,maxVelocity):
        self.__length= 400
        self.__width= 180
        self.__speed=random.randint(0,int(round(1.5*(maxVelocity))))

# Properties
    @property
    def length(self):
        return self.__length
    @property
    def width(self):
        return self.__width
    @property
    def speed(self):
        return self.__speed