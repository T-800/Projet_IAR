import matplotlib.pyplot as plt

import math

def do_plot(q1, q2, t, qd1, qd2, name):
	fig2 = plt.figure()
	fig2.suptitle('Variation des angles en fonction du temps.', fontsize=14, fontweight='bold')
	ax2 = fig2.add_subplot(111, xlim=(0, 4))
	s2 = 'th2 = '+str(int(math.degrees(q2[0])))+' qd2 = '+str(int(math.degrees(qd2)))
	ax2.set_title(s2)
	ax2.grid()
	ax2.set_xlabel('Temps (sec)')
	ax2.set_ylabel('Angle (rad)')
	ax2.plot(t, q1, 'g-', label="q1 - π/2")
	ax2.plot(t, q2, 'r-', label="q2")
	#plt.legend(bbox_to_anchor=(1, 1), loc=2, borderaxespad=0.)
	fic_vals = open("Data/data/"+name +"_"+ str(int(math.degrees(qd2))) + ".txt", "w")
	fic_vals.write(str(q1) + '\n')
	fic_vals.write(str(q2) + '\n')
	fic_vals.write(str(t))
	fic_vals.close()
	ax2.legend(loc="upper right")

	plt.savefig('Data/plots/'+name+'_'+str(s2)+'.png', bbox_inches='tight')
	plt.close(fig2)


def do_plot_tracking(cmd, q2, t, name):
	fig2 = plt.figure()
	fig2.suptitle('Suivi de trajectoire', fontsize=14, fontweight='bold')
	ax2 = fig2.add_subplot(111, xlim=(0, 40))
	#s2 = 'th2 = '+str(int(math.degrees(q2[0])))+' qd2 = '+str(int(math.degrees(qd2)))
	#ax2.set_title(s2)
	ax2.grid()
	ax2.set_xlabel('Temps (sec)')
	ax2.set_ylabel('q2 (rad)')
	ax2.plot(t, cmd, 'k--', label="commande")
	ax2.plot(t, q2, 'r-', label="output")
	ax2.legend(loc="upper right")
	fic_vals = open("Data/data/" + name + ".txt", "w")
	fic_vals.write(str(cmd) + '\n')
	fic_vals.write(str(q2) + '\n')
	fic_vals.write(str(t))
	fic_vals.close()
	plt.savefig('Data/plots/'+name+'_plot.png', bbox_inches='tight')
	plt.close(fig2)
	plt.show()