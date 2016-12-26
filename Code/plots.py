import matplotlib.pyplot as plt
import numpy as np

'''
bruits_0 = open("./bruit0.txt", "r")
bruits_10 = open("./bruit10.txt", "r")
bruits_25 = open("./bruit25.txt", "r")
bruits_50 = open("./bruit50.txt", "r")

END = 300
X = []
y_bruit0 = []
y_bruit10 = []
y_bruit25 = []
y_bruit50 = []

lines = bruits_0.readlines()
for l in lines[:END]:
	ll = l.split("\t")
	X += [float(ll[0])]
	y_bruit0 += [float(ll[1])]

lines = bruits_10.readlines()
for l in lines[:END]:
	ll = l.split("\t")
	y_bruit10 += [float(ll[1])]

lines = bruits_25.readlines()
for l in lines[:END]:
	ll = l.split("\t")
	y_bruit25 += [float(ll[1])]

lines = bruits_50.readlines()
for l in lines[:END]:
	ll = l.split("\t")
	y_bruit50 += [float(ll[1])]

# plt.suptitle('Bruit sur une population de winner-comparator', fontsize=14, fontweight='bold')
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlabel('temps')
ax.set_ylabel('effort')
ax.plot(X, y_bruit0, 'g-', label="0%")
ax.plot(X, y_bruit10, 'r-', label="10%")
ax.plot(X, y_bruit25, 'b-', label="25%")
ax.plot(X, y_bruit50, 'y-', label="50%")
plt.legend(bbox_to_anchor=(1, 1), loc=2, borderaxespad=0.)

plt.show()
'''

def do_plot(q1, q2, t):
	fig = plt.figure()
	ax = fig.add_subplot(111)
	ax.set_xlabel('Temps')
	ax.set_ylabel('Angle (rad)')
	ax.plot(t, q1, 'g-', label="q1")
	ax.plot(t, q2, 'r-', label="q2")
	plt.legend(bbox_to_anchor=(1, 1), loc=2, borderaxespad=0.)
	plt.show()