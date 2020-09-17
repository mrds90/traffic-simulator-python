from __future__ import division
from numpy import array
import pygame
import numpy
import math
from pygame import Rect

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
    
    




#    geometry.py
#
#    Geometry functions to find intersecting lines.
#    Thes calc's use this formula for a straight line:-
#        y = mx + b where m is the gradient and b is the y value when x=0
#
#    See here for background http://www.mathopenref.com/coordintersection.html
#    
#    Throughout the code the variable p is a point tuple representing (x,y)
#
#    Copyright (C) 2008  Nick Redshaw
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see .




"""
# Calc the gradient 'm' of a line between p1 and p2
def calculateGradient(p1, p2):
  
   # Ensure that the line is not vertical
   if (p1[0] != p2[0]):
       m = (p1[1] - p2[1]) / (p1[0] - p2[0])
       return m
   else:
       return None

# Calc the point 'b' where line crosses the Y axis
def calculateYAxisIntersect(p, m):
   return  p[1] - (m * p[0])

# Calc the point where two infinitely long lines (p1 to p2 and p3 to p4) intersect.
# Handle parallel lines and vertical lines (the later has infinate 'm').
# Returns a point tuple of points like this ((x,y),...)  or None
# In non parallel cases the tuple will contain just one point.
# For parallel lines that lay on top of one another the tuple will contain
# all four points of the two lines
def getIntersectPoint(p1, p2, p3, p4):
   m1 = calculateGradient(p1, p2)
   m2 = calculateGradient(p3, p4)
      
   # See if the the lines are parallel
   if (m1 != m2):
       # Not parallel
      
       # See if either line is vertical
        if (m1 is not None and m2 is not None):
           # Neither line vertical           
           b1 = calculateYAxisIntersect(p1, m1)
           b2 = calculateYAxisIntersect(p3, m2)   
           x = (b2 - b1) / (m1 - m2)       
           y = (m1 * x) + b1           
        else:
           # Line 1 is vertical so use line 2's values
            if (m1 is None):
               b2 = calculateYAxisIntersect(p3, m2)   
               x = p1[0]
               y = (m2 * x) + b2
           # Line 2 is vertical so use line 1's values               
            elif (m2 is None):
               b1 = calculateYAxisIntersect(p1, m1)
               x = p3[0]
               y = (m1 * x) + b1           
            else:
               assert false
        if (False==(x<p1[0] and x<p2[0] and x<p3[0] and x<p4[0]) or (x>p1[0] and x>p2[0] and x>p3[0] and x>p4[0]) or (y>p1[1] and y>p2[1] and y>p3[1] and y>p4[1]) or (y>p1[1] and y>p2[1] and y>p3[1] and y>p4[1])):
            
            return ((x,y),)
   else:
       # Parallel lines with same 'b' value must be the same line so they intersect
       # everywhere in this case we return the start and end points of both lines
       # the calculateIntersectPoint method will sort out which of these points
       # lays on both line segments
       b1, b2 = None, None # vertical lines have no b value
       if m1 is not None:
           b1 = calculateYAxisIntersect(p1, m1)
          
       if m2 is not None:   
           b2 = calculateYAxisIntersect(p3, m2)
      
       # If these parallel lines lay on one another   
       if b1 == b2:
           return p1,p2,p3,p4
       else:
           return None
           """