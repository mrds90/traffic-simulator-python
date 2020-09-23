from methods import *
def magnet_street(mousePosition,clickNumber,streetList):
            
        limite=magnet_street_limits(mousePosition,clickNumber,streetList)
        if limite==None:
            if clickNumber==1:
                clickNumber=0
            b=[]
            c=[]
            match=False
            for x in streetList[0:len(streetList)-1-clickNumber]:
                a=circle_and_segment_intercection(x.begining,x.end,mousePosition,15)
                    
                if a!=None:
                        
                    b.append(a)
                    c.append(float(module(array(a)-array(mousePosition))))
                    match=True
                    
            if match==True:
                a=b[c.index(min(c))]  
                return a
            else:
                return mousePosition
            print('devuelvo None')   
        else:
            return limite 
        
def magnet_street_intersection(mousePosition,intersectionList):
        #if len(self.__land.intercetion)>0:
            b=[]
            c=[]
            match=False
            for x in intersectionList:
                a=pointOnACircle(x.position,mousePosition,15)
                    
                if a!=None:
                        
                    b.append(a)
                    c.append(float(module(array(a)-array(mousePosition))))
                    match=True
                    
            if match==True:
                a=b[c.index(min(c))]  
                return a
            return mousePosition
        
def magnet_street_limits(mousePosition,clickNumber,streetList):
        if clickNumber==1:
            clickNumber=0
        b=[]
        c=[]
        match=False
        for x in streetList[0:len(streetList)-1-clickNumber]:
            a=pointOnACircle(x.begining,mousePosition,15)
            a1=pointOnACircle(x.end,mousePosition,15)
            if a!=None:
                
                b.append(a)
                c.append(float(module(array(a)-array(mousePosition))))
                match=True
            if a1!=None:
                b.append(a1)
                c.append(float(module(array(a1)-array(mousePosition))))
                match=True

        if match==True:
            a=b[c.index(min(c))]  
            return a
        else:
            return None
        print('devuelvo None') 
        
def magnet_horizontal_and_vertical(mousePosition,clickNumber,streetList):
        if clickNumber==1:
            clickNumber=0
        b=[]
        c=[]
        d=[]
        e=[]
        matchHorizontal=False
        matchVertical=False
        for x in streetList[0:len(streetList)-1-clickNumber]:
            horizontal=pointOnACircle((x.begining[0],mousePosition[1]),mousePosition,30)
            horizontal1=pointOnACircle((x.end[0],mousePosition[1]),mousePosition,30)
            vertical=pointOnACircle((mousePosition[0],x.begining[1]),mousePosition,30)
            vertical1=pointOnACircle((mousePosition[0],x.end[1]),mousePosition,30)
            if horizontal!=None:
                b.append(horizontal)
                c.append(float(module(array(horizontal)-array(mousePosition))))
                matchHorizontal=True
            if horizontal1!=None:
                b.append(horizontal1)
                c.append(float(module(array(horizontal1)-array(mousePosition))))
                matchHorizontal=True
            if vertical!=None:
                d.append(vertical)
                e.append(float(module(array(vertical)-array(mousePosition))))
                matchVertical=True
            if vertical1!=None:
                d.append(vertical1)
                e.append(float(module(array(vertical1)-array(mousePosition))))
                matchVertical=True

        if matchHorizontal==True and matchVertical==True:
            horizontal=b[c.index(min(c))]  
            vertical=d[e.index(min(e))]  
            return (horizontal[0],vertical[1])
        elif matchHorizontal==True and matchVertical==False:
            horizontal=b[c.index(min(c))]
            return horizontal  
        elif matchHorizontal==False and matchVertical==True:
            vertical=d[e.index(min(e))]
            return vertical
        else:
            return mousePosition
        print('devuelvo None')     
