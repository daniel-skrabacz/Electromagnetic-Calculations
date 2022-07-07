# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 15:10:38 2021

@author: Daniel
"""
#%% Import Libraries
import numpy as np
import matplotlib.pyplot as plt
plt.style.available




#%% Define function

def in2meter(my_input):
    return my_input*0.0254

def in2mmeter(my_input):
    return my_input*254

def PPInd(d,D,ur):
    """
    Parallel Plate Inductance
    
    Parameters
    ----------
    d : Dielectric thickness separating the parallel plates
    D : Conductor and dielectric width
    ur : Relative permeability
    
    Magnetic field will go a little ways into the copper, so account for that 
    in the thickness (d)
    
    Returns
    -------
    Inductance per unit length
    (nanoHenries per whatever unit used)
    
    """
    from numpy import pi
    u0 = 4*pi*1e-7
    ut = ur*u0
    return ut*d/D

def CharIPP(ur,er,d,D):
    """
    Parameters
    ----------
    ur : relative permeability
    er : relative permittivity
    d : Dielectric thickness separating the parallel plates
    D : Conductor and dielectric width
    
    Returns
    -------
    Parallel plate Characteristic Impedance per unit length
    ohm/meter
    """
    from numpy import sqrt, pi
    u0 = 4*pi*1e-7
    e0 = 8.854e-12
    ut = u0*ur
    et = e0*er
    width_term = d/D
    perm_term = sqrt(ut/et)
    return perm_term*width_term

def coaxICI(b, a, ur=1, e_prime=1):
    """
    

    Parameters
    ----------
    b : Outer conductor radius
    a : Inner conductor radius
    ur : TYPE, optional
        Relative permeability. The default is 1.
    e_prime : TYPE, optional
        Relative Permittivity. The default is 1.

    Returns
    -------
    inductance : Characteristic inductance per unit length

    """
    from numpy import pi, log
    u0 = 4*pi*1e-7
    e0 = 8.854e-12
    ut = u0*ur
    inductance = log(b/a)*ut/(2*pi)
    return inductance

def twowireInd(a, D, ur=1):
    from numpy import arccosh, pi
    u0 = 4*pi*1e-7
    var1 = u0*ur/pi
    var2 = arccosh(D/(2*a))
    return var1*var2
    


def stp_imp(er, h, t, w):
    """
    

    Parameters
    ----------
    er : Relative Permittivity
    h : Distance between conductors
    t : thickness of conductors
    w : Width of Conductors

    Returns
    -------
    Characteristic Impedance of a stripline (like RF stripline)

    """
    et = 30/(np.sqrt(er))
    num_term = 1.9*(2*h + t)
    den_term = 0.8*w + t
    return et*np.log(num_term/den_term)


#%% Create data for varying the conductor width

D = np.linspace(0.1, 5, num = 50)
induct = [PPInd(0.0048, x, 1) for x in D]
#plt.rcParams["font.family"] = "monospace"
plt.style.use('seaborn-bright')
plt.grid()
plt.plot(D,induct)
plt.ylabel('Inductance per unit length (H/m)')
plt.xlabel('Conductor Width (Inches)')

#%% Create data for varying the dielectric thickness

d = np.linspace(0.001, 0.25, num = 50)
induct = [PPInd(x, 2, 1) for x in d]

plt.grid()
plt.legend(["nH/meter"])
plt.plot(d,induct)
plt.ylabel('Inductance per unit length (H/m)')
plt.xlabel('Distance between conductors (Inches)')

#%% Characteristic impedance

D = np.linspace(0.1, 2, num = 50)
# Use D from above
char_imp = [CharIPP(1, 3.4, 0.005, x) for x in D]

plt.plot(char_imp, D)
plt.xlabel('Impedance per unit length (ohm/m)')
plt.ylabel('Conductor Width (Inches)')


#%% Stripline Impedance


