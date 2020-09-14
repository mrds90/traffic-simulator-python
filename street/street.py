from methods import versor_from_two_points


class Street:
    __begining:tuple
    __end:tuple
    __lanes:int
    __yDir:tuple
    __xDir:tuple

    def __init__(self,streetID,begining:tuple,end:tuple,lanes:int):
        try:
            if (len(begining) !=2 or len(end) !=2):
                raise ValueError
            else:
                self.__streetID=streetID
                self.__begining=begining
                self.__end=end
                self.__lanes=lanes
                self.__yDir=tuple(self.__y_vector())
                self.__xDir=tuple(self.__x_vector())
        except ValueError:
            print ('posiciones ingresadas incorrectamente')
            


            
    
    @property
    def lanes(self):
        return self.__lanes
    @property
    def yDir(self):
        return self.__yDir 
    @property
    def xDir(self):
        return self.__xDir 
    @property
    def id(self):
        return self.__streetID
    
    #metodos
    def __y_vector(self):
        return(versor_from_two_points(self.__begining,self.__end))

    def __x_vector(self):
        return [self.__yDir[1],-1*self.__yDir[0]]# x2=-y1 y2=x1


          
    

