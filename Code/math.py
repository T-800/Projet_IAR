#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from numpy import sin, cos, pi, array
import numpy as np
import scipy.integrate as integrate
from scipy import misc

#q1=state[0]
#dq1=state[1]
#q2=state[2]
#dq2=state[3]

tq = 0

q1 = 90.0
q2 = 0.0
dq1 = 0.0
dq2 = 0.0

g =  9.81 # gravite (m/s^2)
l1 = 1.15 # longueur des segments (m)
l2 = 2.25
L = 1.3*(l1+l2)
lc1 = l1/2.0 
lc2 = l2/2.0
m1 = 0.4 # masse des segments (kg)
m2 = 0.9 
I1 = 1/12.0*m1*l1**2 # moments d'inertie (kg.m^2)
I2 = 1/12.0*m2*l2**2

d11 = m1*lc1**2 + m2*(l1**2 + lc2**2 + 2*l1*lc2*cos(q2)) + I1 + I2
d22 = m2*lc2**2 + I2
d12 = m2*(lc2**2 + l1*lc2*cos(q2)) + I2 
d21 = m2*(lc2**2 + l1*lc2*cos(q2)) + I2

h1 = -m2*l1*lc2*sin(q2)*dq2**2 - 2*m2*l1*lc2*sin(q2)*dq2*dq1
h2 = m2*l1*lc2*sin(q2)*dq1**2
phi1 = (m1*lc1+m2*l1)*g*cos(q1)+m2*lc2*g*cos(q1+q2)
phi2 = m2*lc2*g*cos(q1+q2)

h = [ dq1, dq2, -(h1+phi1)*d22/(d11*d22-d12*d21)-(tq-h2-phi2)*d12/(d11*d22-d12*d21), (h1+phi1)*d21/(d11*d22-d12*d21)+(tq-h2-phi2)*d11/(d11*d22-d12*d21) ]

def fonction(x): 
	return x

#print(misc.derivative(fonction, h[2]))













