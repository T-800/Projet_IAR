import matplotlib.pyplot as plt

import math

def do_plot(q1, q2, t, qd1, qd2):
	fig2 = plt.figure()
	fig2.suptitle('Variation des angles en fonction du temps.', fontsize=14, fontweight='bold')
	ax2 = fig2.add_subplot(111, xlim=(0, 10))
	s2 = 'th2 = '+str(int(math.degrees(q2[0])))+' qd2 = '+str(int(math.degrees(qd2)))
	ax2.set_title(s2)
	ax2.grid()
	ax2.set_xlabel('Temps (sec)')
	ax2.set_ylabel('Angle (rad)')
	ax2.plot(t, q1, 'g-', label="q1 - qd1")
	ax2.plot(t, q2, 'r-', label="q2 - qd2")
	#plt.legend(bbox_to_anchor=(1, 1), loc=2, borderaxespad=0.)
	ax2.legend(loc="upper right")
	plt.savefig('Data/plots/plot_'+str(s2)+'.png', bbox_inches='tight')
	plt.close(fig2)


def do_plot_tracking(cmd, q2, t):
	fig2 = plt.figure()
	fig2.suptitle('Suivi de trajectoire', fontsize=14, fontweight='bold')
	ax2 = fig2.add_subplot(111, xlim=(0, 40))
	#s2 = 'th2 = '+str(int(math.degrees(q2[0])))+' qd2 = '+str(int(math.degrees(qd2)))
	#ax2.set_title(s2)
	ax2.grid()
	ax2.set_xlabel('Temps (sec)')
	ax2.set_ylabel('q2 (rad)')
	ax2.plot(t, cmd, 'k--', label="commande")
	ax2.plot(t, q2, 'k-', label="output")
	plt.legend(bbox_to_anchor=(1, 1), loc=2, borderaxespad=0.)
	plt.savefig('Data/plots/plot_tracking.png', bbox_inches='tight')
	#plt.close(fig2)
	plt.show()