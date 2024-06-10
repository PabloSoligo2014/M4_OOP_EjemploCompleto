'''
Created on 16 ago. 2019

@author: pabli
'''


class GeoPosicion(object):
    '''
    classdocs
    '''


    def __init__(self, lat=0, lon=0):
        '''
        Constructor
        '''
        self.__lat = lat
        self.__lon = lon
        self._ele = None
       
        
    def set_lat(self, value):
        if(value<-90 or value>90):
            raise Exception("Invalid lat")
        self.__lat = value
    
    def set_lon(self, value):
        if(value<-180 or value>180):
            raise Exception("Invalid lon")
        self.__lon = value
        
    def get_lat(self):
        return self.__lat
    
    def get_lon(self):
        return self.__lon
          
 
    def render(self, canvas):
        if self._ele==None:
            x0 = int(((self.__lon+180)*canvas.w)/360.0)
            y0 = canvas.h - int(((self.__lat+90)*canvas.h)/180.0)
            midsize = 5
            self._ele = canvas.create_oval(x0-midsize, y0-midsize, x0+midsize, y0+midsize, fill='red')
        return self._ele
        
    def __str__(self):
        return str(self.__lat)+", "+str(self.__lon)
    def __repr__(self):
        return str(self.__lat)+", "+str(self.__lon)
        