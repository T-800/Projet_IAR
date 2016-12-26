import matplotlib.pyplot as plt
import numpy as np



def do_plot(q1, q2):
	fig = plt.figure()
	ax = fig.add_subplot(111)
	ax.set_xlabel('Temps')
	ax.set_ylabel('Angle (rad)')
	t = np.array([i/len(q1)*10 for i in range(len(q1))])
	ax.plot(t, q1, 'g-', label="0%")
	ax.plot(t, q2, 'r-', label="10%")
	#ax.plot(q1[:len(t)], t, 'g-', label="0%")
	plt.show()