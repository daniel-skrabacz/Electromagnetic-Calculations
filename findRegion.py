# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 08:19:40 2022

Determining if a distance is in the reactive near-field, radiating near-field,
or in the far field

Reactive Near Field Region 

Radiating near-field region - Also known as Fresnel region

Far field region - Fraunhofer region

@author:Daniel Skrabacz

Created on: July 9, 2022
"""

#%% Import libraries

import numpy as np

#%% Define Functions

def findRegion(R, D, wavelength):
    if R < 0.62*np.sqrt(D**3/wavelength):
        x = 'Reactive NF'
    elif 2*D**2/wavelength > R & R >=  0.62*np.sqrt(D**3/wavelength):
        x = 'Fresnel Region or Radiating NF'
    else:
        x = 'Fraunhofer or Far Field Region'
    return x

#%% Test case(s)

R = [0.5, 5, 100] #meters
D = 0.2 # meters
wavelength = 0.01 # meters

for i in R:
    print(str(i)+str(' meters'), findRegion(i,D,wavelength))
        
        
        
        
        
        
        
        