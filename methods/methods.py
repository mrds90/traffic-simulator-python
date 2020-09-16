from numpy import array
import pygame
import numpy
import math

def versor_from_two_points(pointOne,pointTwo):
    y=array(pointTwo)-array(pointOne)
    y=y/math.sqrt(sum(pow(y,2)))
    return y
def a_versor(vector):
    vector=array(vector);
    return vector/vector_longitud(vector)

def vector_longitud(vector:tuple):
    return math.sqrt(sum(pow(vector,2)))
def angle_between_vector(v1,v2):
    v1=a_versor(v1)
    v2=a_versor(v2)
    vAux=[v1[1],-v1[0]]
    sign=numpy.dot(v2,vAux)
    sign=sign/numpy.abs(sign)
    ang=(numpy.arcsin(numpy.dot(v1,v2))*sign)*180/numpy.pi
    return ang

def scale_rect(scale,sizeToModify,referenceSize,horzontalOrVertical):
    imageSize=array(sizeToModify)
    windowSize=array(referenceSize)
    relacionDeAspecto=imageSize/windowSize
    scaleFactor=scale/relacionDeAspecto[horzontalOrVertical]
    return (scaleFactor*imageSize).astype(int)   
def rot_center (image,angle):
    center=image.get_rect().center
    rotatedImage = pygame.transform.rotate(image,angle)
    newRect= rotatedImage.get_rect(center=center)
    return newRect