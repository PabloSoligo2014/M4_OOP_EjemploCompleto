'''
Created on 16 ago. 2019

@author: pabli
'''
from GeoPosicion import GeoPosicion

class Lugar(GeoPosicion):
    
    def __init__(self, lat, lon, desc):
        super(Lugar, self).__init__(lat, lon)
        self.__desc = desc
        
    def render(self, canvas):
        if self._ele==None:
            x0 = int(((self.get_lon()+180)*canvas.w)/360.0)
            y0 = canvas.h - int(((self.get_lat()+90)*canvas.h)/180.0)
            midsize = 5
            canvas.create_text(x0+midsize, y0+midsize, text=self.__desc)
            self._ele = canvas.create_rectangle(x0-midsize, y0-midsize, x0+midsize, y0+midsize, fill='blue')
        
        return self._ele
    
        