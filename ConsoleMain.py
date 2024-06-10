'''
Created on 16 ago. 2019

@author: pabli
'''

from GeoPosicion import *

if __name__ == '__main__':
    
    g1 = GeoPosicion()
    g2 = GeoPosicion(-34.0, -58.0)
    
    g1.set_lat(-34)
    g1.set_lon(-54)
    
    
    print(g1)