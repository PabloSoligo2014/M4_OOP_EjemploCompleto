'''
Created on 16 ago. 2019

@author: pabli
'''
from GeoPosicion import GeoPosicion
from PIL.ImageTk import PhotoImage
from tkinter.constants import NW, CENTER
import random
class Flight(GeoPosicion):
    
    def __init__(self, lat, lon, number):
        super(Flight, self).__init__(lat, lon)
        self.__number = number
        
    def render(self, canvas):
        if self._ele==None:
            x0 = int(((self.get_lon()+180)*canvas.w)/360.0)
            y0 = canvas.h - int(((self.get_lat()+90)*canvas.h)/180.0)
            if not hasattr(canvas, "airplane_image"):
                canvas.airplane_image = PhotoImage(file="airplane_blue.png")
            
            self._ele = canvas.create_image(x0, y0, image=canvas.airplane_image, state="normal", anchor=CENTER)
            self._text = canvas.create_text(x0, y0, text=self.__number, fill="white")
            #= canvas.create_image(x0, y0, image=a_image)
        else:
            
            
            self.set_lon(self.get_lon()+random.randrange(0,90)*0.01)
            
            x0 = int(((self.get_lon()+180)*canvas.w)/360.0)
            y0 = canvas.h - int(((self.get_lat()+90)*canvas.h)/180.0)
            
            canvas.coords(self._ele, (x0,y0))
            canvas.coords(self._text, (x0,y0))
            
        return self._ele