# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 09:42:15 2022

@author: Daniel Skrabacz
"""
#%% Import Libraries

import numpy as np

#%% EM functions

def wavelength(f):
    return 3e8/f

def eAnt(length, G):
    firstTerm = length**2/(np.pi*4)
    return firstTerm*G



def skin_depth(sigma, f, ur=1):
    """
    Parameters
    ----------
    u0 = 4*pi*1e-7 (Henries per meter)
    u : relative permeability (Henries per meter)
    sigma : electrical conductivity (Siemens per meter)
    f : frequency (Hz)

    Returns
    -------
    skin depth (meters)

    """
    u0 = 4*np.pi*1e-7
    skin = np.sqrt(1/(ur*u0*f*sigma*np.pi))
    return skin


def waveEqu(k,t,w):
    return np.exp(-1j*(k-w*t))


def recipP1P2(R1,R2, Y21):
    """
    Reciprocity theorem applied to simple antennas    

    Parameters
    ----------
    R1 : Resistance of generator impedance
    R2 : Resistance of load impedance
    Y21 : transfer admittance of generator, antenna, and load impedances

    Returns
    -------
    Power ratio of Power Out vs Power in

    """
    return 4*R1*R2*(Y21**2)


    