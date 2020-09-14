import random

class Vehicle:

    def __init__(self,maxStreetVelocity):
        self.__length= 400
        self.__width= 180
        self.__position=[random.randint(0,100),random.randint(0,100)]
        self.__relativeMax= (random.randint(66,133)*maxStreetVelocity)/100 #respeto de la velocidad de los conductores
        self.__speed=random.randint(0,int(round(1.5*(maxStreetVelocity)))) #velocidad del vehiculo al comenzar
        self.__aceletation=random.randint(4,10) #aceleracion del vehiculo
        self.__direction=random.randint(0,359) #angulo de avance -->0 horizontal derecha y 90 hacia arriba vertical

        

        
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