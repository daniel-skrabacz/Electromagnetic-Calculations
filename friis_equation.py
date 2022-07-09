# -*- coding: utf-8 -*-
"""
Spyder Editor

This script explores the Friis equation for far field between two antennas.

author: Daniel Skrabacz

"""

#%% Import Libraries

import numpy as np

#%% Function

def ffFriis(Pt, Gt, Gr, wavelength, R):
    # Far Field Friis transmission equation
    # Calculate power received knowing the
    # transmitted power, transmission gain,
    # receiver gain, and wavelength of interest
    num = Pt*Gt*Gr*wavelength**2
    den = (np.pi*4*R)**2
    return num/den

#%% Explore wavelengths

Pt = 10 # Watts
Gt = 1
Gr = 10
wavelength = 0.001 #meters

R = np.linspace(0.01, 100)

#%% Run function

values = ffFriis(Pt, Gt, Gr, wavelength, R)

for i in values:
    print(i)