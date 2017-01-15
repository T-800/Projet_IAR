import subprocess

import matplotlib.animation as animation
import scipy.integrate as integrate
from numpy import sin, cos, pi
from readfile import *
from plots import *
import numpy as np


from sympy.solvers import solve
from sympy import Symbol
import sympy as sp


tab = [[], [], []]

# it = 0
# vals_qd2 = [-pi / 2, pi / 3, -pi / 6, 0, pi / 2, -pi / 3, pi / 6]

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
t = np.arange(0.0, 40, dt)



def get_qd2(t):
	qd1 = Symbol('qd1', real=True)
	c4 = m1 * lc1 + m2 * l1
	c5 = m2 * lc2

	if t < 5:
		return -1.55, gains[0][0], gains[0][1], gains[0][2], gains[0][3]

	if t < 10:
		return 0, gains[1][0], gains[1][1], gains[1][2], gains[1][3]

	if t < 15:

		x = solve(c4 * sp.cos(qd1) + c5 * sp.cos(qd1 + (-0.25 * t + 2.5)), qd1)
		return -0.25 * t + 2.5, gains[2][0], gains[1][1], gains[2][2], gains[2][3], x[0]

	if t < 20:
        return -1.25, gains[2][0], gains[2][1], gains[2][2], gains[2][3]

	x = solve(c4 * sp.cos(qd1) + c5 * sp.cos(qd1 + ((0.4 * sin(t * 0.7 + 20 )) - 1)), qd1)

	return (0.4 * sin(t * 0.7 + 20 )) - 1, gains[3][0], gains[3][1], gains[3][2], gains[3][3], x[0]

def get_dotqd2(t):
	if t < 10:
		return 0
	if t < 15:
		return -0.25
	if t < 20:
		return 0
	return (0.4 * 0.7 * cos(0.7 * t + 90)) # TODO : Finir sinus

def torque(state, t):
	gain = get_qd2(t)[1:]
	qd2, kp, kd, kdd, qd1 = get_qd2(t)
	q1 = state[0]
	dq1 = state[1]
	q2 = state[2]
	dq2 = state[3]



	x1 = lc1 * cos(q1)
	x2 = l1 * cos(q1) + lc2 * cos(q1 + q2)
	dx1 = - dq1 * lc1 * sin(q1)
	dx2 = - dq1 * l1 * sin(q1) - (dq1 + dq2) * lc2 * sin(q1 + q2)

	taud = m2 * lc2 * g * cos(qd1 + qd2)

	Moment = (m1 * lc1 ** 2 + m2 * l1 ** 2 + I1 + m2 * lc2 ** 2 + I2 + 2 * m2 * l1 * lc2 * cos(q2)) * \
			 dq1 + ( m2 * lc2 ** 2 + I2 + m2 * l1 * lc2 * cos(q2)) * dq2

	c = m1 + m2
	c1 = m1 * lc1 ** 2 + m2 * l1 ** 2 + I1
	c2 = m2 * lc2 ** 2 + I2
	c3 = m2 * l1 * lc2
	c4 = m1 * lc1 + m2 * l1
	c5 = m2 * lc2


	dotqd1 = 0
	dotqd2 = 0
	'''
	dotqd1 = Symbol('dotqd1', real=True)
	dotqd2 = get_dotqd2(t)

	x = solve( - c4 * sin(qd1) * dotqd1 - c5 * sin(qd1+qd2) * dotqd1 , dotqd1)
	print(x)
	dotqd1 = float(x[0])
	'''
	Ld = (c1 + c2 + 2 * c3 * cos(qd2)) * dotqd1 + (c2 + c3 * cos(qd2)) * dotqd2

	dL = - g * (m1 * x1 + m2 * x2)
	ddL = - g * (m1 * dx1 + m2 * dx2)

	tau = kdd * ddL + kd * dL + kp * (Moment - Ld) + taud
	tq = tau

	return tq


def derivs(state, t):
	global _last_time, tab, dt
	d = np.zeros_like(state)
	q1 = state[0]
	dq1 = state[1]
	q2 = state[2]
	dq2 = state[3]
	tab[0] += [get_qd2(t)[0]]
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
th1 = 90.0
th2 = 0.0
dth1 = 0.0
dth2 = 0.0

# etat initial (un vecteur de dimension 4)

calcul_gains_tracking_m()
gains = read_file("Data/polys_tracking.txt", 1)

x = Symbol('x', real=True)
c4 = m1 * lc1 + m2 * l1
c5 = m2 * lc2
v = solve(c4 * sp.cos(x) + c5 * (sp.cos(x)*math.cos(1.55) + sp.sin(x)*math.sin(1.55)), x)
if v[0] > 0:
	v = v[0]
else:
	v = v[1]
print(v)
gains[0][3] = v
v = solve(c4 * sp.cos(x) + c5 * sp.cos(x), x)
if v[0] > 0:
	v = v[0]
else:
	v = v[1]
gains[1][3] = v
v = solve(c4 * sp.cos(x) + c5 * (sp.cos(x)*math.cos(1.25) + sp.sin(x)*math.sin(1.25)), x)
if v[0] > 0:
	v = v[0]
else:
	v = v[1]
gains[2][3] = v


state = np.array([th1, dth1, th2, dth2]) * pi / 180.
y = integrate.odeint(derivs, state, t, mxstep=5000000)


x1 = l1 * cos(y[:, 0])
y1 = l1 * sin(y[:, 0])

x2 = l2 * cos(y[:, 0] + y[:, 2]) + x1
y2 = l2 * sin(y[:, 0] + y[:, 2]) + y1

fig = plt.figure()
ax = fig.add_subplot(111, autoscale_on=False, xlim=(-2, 2), ylim=(-2, 2))
ax.grid()
ax.set_axis_bgcolor('black')

line3, = ax.plot([], [], 'r-', lw=2)
line1, = ax.plot([], [], 'o-', lw=2, c=(0, 1, 0))

#line2, = ax.plot([], [], 'o-', lw=2, c=(1, 1.0 * 180.0 / 255.0, 0))
time_template = 'time = %.2fs'
time_text = ax.text(0.05, 0.95, '', color='red', transform=ax.transAxes)


def init():
	line1.set_data([], [])
	time_text.set_text('')
	return line1, time_text


def animate(i):
	trace = 50
	thisx = [0, x1[i], x2[i]]
	thisy = [0, y1[i], y2[i]]
	line3.set_data(x2[max(0, i-trace):i], y2[max(0, i-trace):i])
	#line3.set_data(x2[:i], y2[:i])
	line1.set_data(thisx, thisy)
	time_text.set_text(time_template % (i * dt))
	return line1, line3, time_text


ani = animation.FuncAnimation(fig, animate, frames=len(y),
							  interval=dt * 1e3, init_func=init)

# ani.save('test.mp4', fps=15)
plt.axis('equal')
plt.axis([-L, L, -L, L])
plt.show()
do_plot_tracking(tab[0], tab[1], tab[2])