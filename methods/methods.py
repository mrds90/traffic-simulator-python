from numpy import array
import math
def versor_from_two_points(pointOne,pointTwo):
    y=array(pointTwo)-array(pointOne)
    y=y/math.sqrt(sum(pow(y,2)))
    return y
def vector_longitud(vector:tuple):
    return math.sqrt(sum(pow(vector,2)))        