import sys
from numpy import sin, cos, pi, array
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import matplotlib.animation as animation
from sympy.solvers import solve
from sympy import Symbol
import sympy as sp
from readfile import *
from plots import *
import math
import os

tab = [[], [], []]

qd2 = -pi/2 # En radian!!
th1 = 90.0
th2 = 0.0

#vals_qd2 = [-pi / 4, -pi / 3, -pi / 2, 0, pi / 2, pi / 3, pi / 4]


_last_time = 0
g = 9.81  # gravite (m/s^2)
l1 = 1.15  # longueur des segments (m)
l2 = 2.25
L = 1.3 * (l1 + l2)
lc1 = l1 / 2.0
lc2 = l2 / 2.0
m1 = 0.4  # masse des segments (kg)
m2 = 0.9
I1 = 1 / 12.0 * m1 * l1 ** 2  # moments d'inertie (kg.m^2)
I2 = 1 / 12.0 * m2 * l2 ** 2

dt = 30e-3
t = np.arange(0.0, 10, dt)

"""t = []
for i in range(len(vals_qd2)):
    t += [np.arange(0.0 + i * 10, 10*(i+1), dt)]
"""

def torque(state, t):
    q1 = state[0]
    dq1 = state[1]
    q2 = state[2]
    dq2 = state[3]

    x1 = lc1 * cos(q1)
    x2 = l1 * cos(q1) + lc2 * cos(q1 + q2)
    dx1 = - dq1 * lc1 * sin(q1)
    dx2 = - dq1 * l1 * sin(q1) - (dq1 + dq2) * lc2 * sin(q1 + q2)

    taud = m2 * lc2 * g * cos(qd1 + qd2)

    Moment = (m1 * lc1 ** 2 + m2 * l1 ** 2 + I1 + m2 * lc2 ** 2 + I2 + 2 * m2 * l1 * lc2 * cos(q2)) * dq1 + (
                                                                                                            m2 * lc2 ** 2 + I2 + m2 * l1 * lc2 * cos(
                                                                                                                q2)) * dq2

    dL = - g * (m1 * x1 + m2 * x2)
    ddL = - g * (m1 * dx1 + m2 * dx2)

    tau = kdd * ddL + kd * dL + kp * Moment + taud
    tq = tau
    return tq


def derivs(state, t):
    global _last_time, tab, dt
    d = np.zeros_like(state)
    q1 = state[0]
    dq1 = state[1]
    q2 = state[2]
    dq2 = state[3]
    if _last_time < t:
        tab[0] += [q1]
        tab[1] += [q2]
        tab[2] += [t]

    d11 = m1 * lc1 ** 2 + m2 * (l1 ** 2 + lc2 ** 2 + 2 * l1 * lc2 * cos(q2)) + I1 + I2
    d22 = m2 * lc2 ** 2 + I2
    d12 = m2 * (lc2 ** 2 + l1 * lc2 * cos(q2)) + I2
    d21 = m2 * (lc2 ** 2 + l1 * lc2 * cos(q2)) + I2

    h1 = -m2 * l1 * lc2 * sin(q2) * dq2 ** 2 - 2 * m2 * l1 * lc2 * sin(q2) * dq2 * dq1
    h2 = m2 * l1 * lc2 * sin(q2) * dq1 ** 2
    phi1 = (m1 * lc1 + m2 * l1) * g * cos(q1) + m2 * lc2 * g * cos(q1 + q2)
    phi2 = m2 * lc2 * g * cos(q1 + q2)

    d[0] = dq1
    d[2] = dq2

    tq = torque(state, t)
    A = np.array([[d11, d12], [d21, d22]])
    B = np.array([-h1 - phi1, tq - h2 - phi2])
    x = np.linalg.solve(A, B)
    d[1] = x[0]
    d[3] = x[1]

    return d


# th1 et th2 sont les angles initiaux (degres)
# dth1 et dth2 sont leurs derivees respectives (les vitesses angulaires, en degres/s)

dth1 = 0.0
dth2 = 0.0

# etat initial (un vecteur de dimension 4)



kp, kd, kdd, qd1 = getGains()

state = np.array([th1, dth1, th2, dth2]) * pi / 180.
y = integrate.odeint(derivs, state, t, mxstep=5000000)


"""
for i in range(len(vals_qd2)):
    qd2 = vals_qd2[i]
    fic_vals = open("Data/vals_qd.txt", "w")
    fic_vals.write("qd2 = "+str(math.degrees(qd2)))
    fic_vals.close()

    os.system("cd C:/Users/Nadjet BOURDACHE/Desktop/Cours/M2 ANDROIDE/Projets/Projet_IAR/Code/Calculs")
    os.system('matlab -nojvm -nodisplay -r "calcul_gains ; exit" ')

    kp, kd, kdd, qd1 = getGains()

    state = np.array([th1, dth1, th2, dth2]) * pi / 180.
    y = integrate.odeint(derivs, state, t[i], mxstep=5000000)

    th1 = qd1
    th2 = qd2
"""

x1 = l1 * cos(y[:, 0])
y1 = l1 * sin(y[:, 0])

x2 = l2 * cos(y[:, 0] + y[:, 2]) + x1
y2 = l2 * sin(y[:, 0] + y[:, 2]) + y1

fig = plt.figure()
ax = fig.add_subplot(111, autoscale_on=False, xlim=(-2, 2), ylim=(-2, 2))
ax.grid()
ax.set_axis_bgcolor('black')

line1, = ax.plot([], [], 'o-', lw=2, c=(0, 1, 0))
line2, = ax.plot([], [], 'o-', lw=2, c=(1, 1.0 * 180.0 / 255.0, 0))
time_template = 'time = %.2fs'
time_text = ax.text(0.05, 0.95, '', color='red', transform=ax.transAxes)


def init():
    line1.set_data([], [])
    time_text.set_text('')
    return line1, time_text


def animate(i):
    thisx = [0, x1[i], x2[i]]
    thisy = [0, y1[i], y2[i]]
    line1.set_data(thisx, thisy)
    time_text.set_text(time_template % (i * dt))
    return line1, time_text


ani = animation.FuncAnimation(fig, animate, frames=len(y),
                              interval=dt * 1e3, init_func=init)

# ani.save('test.mp4', fps=15)
plt.axis('equal')
plt.axis([-L, L, -L, L])
plt.show()
tab[0] = [tab[0][i] - qd1 for i in range(len(tab[1]))]
tab[1] = [tab[1][i] - qd2 for i in range(len(tab[1]))]
do_plot(tab[0], tab[1], tab[2])