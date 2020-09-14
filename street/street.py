class Street:
    def __init__(self,begining:tuple,end:tuple,width:float):
        try:
            if (len(begining) !=2 or len(end) !=2):
                raise ValueError
            else:
                self.__begining=begining
                self.__end=end
                self.__width=width
        except ValueError:
            print ('posiciones ingresadas incorrectamente')
            del self
    @property
    def width(self):
        return self.__width
            
    

