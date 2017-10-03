#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 14:17:01 2017

@author: adafactor
"""

import numpy as np
import matplotlib.pyplot as plt
#from sympy import symbols 

def graphXY( formula_x, formula_y ):
    d = np.arange(-1,1,0.0001)
    x = formula_x(d)
    y = formula_y(d)
    plt.plot(x, y)
    plt.show()
    
def graph1D( fx, fy ):
    d = np.arange(-10, 10, 0.01)
    x = fx(d)
    y = fy(x,d)
    plt.plot(fx(d),fy(x, d))
    plt.show()

graphXY( lambda x : np.sin(x)*np.cos(x)*np.log(np.abs(x)),
      lambda y : np.power(np.abs(y), 0.3)*np.sqrt(np.cos(y)))
graph1D( lambda x: np.power(x**2 - 1, 3),
         lambda x,y: np.power( x**2 + (y**2) -1 ,3 ) - (x**2)*y**3
        )
