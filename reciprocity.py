# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 19:37:38 2022

@author: Daniel Skrabacz

"""
#%% Import Libraries

import numpy as np

#%% Reciprocity of two antennas

Y21 = 1

R1 = 50
R2 = 50

def powerRatio(R1, R2, Y21):
    return 4*R1*R2*Y21**2
    