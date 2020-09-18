from __future__ import division
from numpy import array
from numpy import dot
import pygame
import numpy
import math
from pygame import Rect
def module(vector):
    return math.sqrt(dot(vector,vector))

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
    if sign !=0:
        sign=sign/numpy.abs(sign)
    else:
        sign=1  
    
    ang=(numpy.arccos(numpy.dot(v1,v2))*sign)*180/numpy.pi
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

def cross (v,w):
    return (v[0]*w[1]-v[1]*w[0])
def getIntersectPoint(p,endOne,q,endTwo):
    p=array(p)
    endOne=array(endOne)
    q=array(q)
    endTwo=array(endTwo)
    
    r=endOne-p
    s=endTwo-q
    
    t=cross((q-p),s)/cross(r,s)
    u=cross((q-p),r)/cross(r,s)
    
    if cross(r,s)==0 and cross((q-p),r)==0:
        return None
    if cross(r,s)==0 and cross((q-p),r)!=0:
        return None
    if cross(r,s)!=0 and t>=0 and t<=1 and u>=0 and u<=1:
        return list(p+t*r)
    return None
    

def predictIntersectPoint(p,endOne,q,endTwo):
    p=array(p)
    endOne=array(endOne)
    q=array(q)
    endTwo=array(endTwo)
    
    r=endOne-p
    s=(endTwo-q)*1.10
    
    t=cross((q-p),s)/cross(r,s)
    u=cross((q-p),r)/cross(r,s)
    
    if cross(r,s)==0 and cross((q-p),r)==0:
        return tuple(endTwo)
    if cross(r,s)==0 and cross((q-p),r)!=0:
        return tuple(endTwo)
    if cross(r,s)!=0 and t>=0 and t<=1 and u>=0 and u<=1:
        prediction=p+t*r
        if module((prediction)-endTwo)<50:
            return tuple(prediction)
        else:
            return tuple(endTwo)
    return tuple(endTwo)




def circle_and_segment_intercection(start,end,center,radius):
    
    start=array(start)
    end=array(end)
    center=array(center)
    
    hypotenuse=center-start

    segment=end-start
    segment=a_versor(segment)
    side=(hypotenuse[0]*segment[0]+hypotenuse[1]*segment[1])
    
    D=start+segment*side
    dist=module(D-center)
    
 

    if abs(dist)<=radius:
        return tuple(start+a_versor(segment)*side)
    else:
        return None
    















