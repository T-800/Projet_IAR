import matplotlib.pyplot as plt

import math

f1 = open("/media/data/Data/git/Projet_IAR/Code/Data/data/equilibre_amelioration_0.txt")
f2 = open("/media/data/Data/git/Projet_IAR/Code/Data/data/equilibre_0.txt")
f3 = open("/media/data/Data/git/Projet_IAR/Code/Data/data/equilibre_amelioration_-90.txt")
f4 = open("/media/data/Data/git/Projet_IAR/Code/Data/data/equilibre_-90.txt")

f5 = open("/media/data/Data/git/Projet_IAR/Code/Data/data/traking_ameliore.txt")
f6 = open("/media/data/Data/git/Projet_IAR/Code/Data/data/traking.txt")


trAcmd = eval(f5.readline())
trAq2 = eval(f5.readline())
trAt = eval(f5.readline())

trcmd = eval(f6.readline())
trq2 = eval(f6.readline())
trt = eval(f6.readline())



q1A0 = eval(f1.readline())
q2A0 = eval(f1.readline())
tA0 = eval(f1.readline())

q10 = eval(f2.readline())
q20 = eval(f2.readline())
t0 = eval(f2.readline())

q1A90 = eval(f3.readline())
q2A90 = eval(f3.readline())
tA90 = eval(f3.readline())

q190 = eval(f4.readline())
q290 = eval(f4.readline())
t90 = eval(f4.readline())


fig2 = plt.figure()
fig2.suptitle('Variation des angles en fonction du temps.', fontsize=14, fontweight='bold')
ax2 = fig2.add_subplot(111, xlim=(0, 2))
#s2 = 'th2 = '+str(int(math.degrees(q2[0])))+' qd2 = '+str(int(math.degrees(qd2)))
#ax2.set_title(s2)
ax2.grid()
ax2.set_xlabel('Temps (sec)')
ax2.set_ylabel('Angle (rad)')
new, = ax2.plot(tA0, q1A0, 'k-', label="new")
old, = ax2.plot(t0, q10, 'c-', label="old")
ax2.plot(tA0, q2A0, 'k-', label="q2")
ax2.plot(t0, q20, 'c-', label="q2")
#ax2.plot(t, q2, 'r-', label="output")
ax2.annotate('q1 - π/2 ', xy=(2, 1), xytext=(0.75, 0.5),)
ax2.annotate('q2', xy=(2, 1), xytext=(0.75, -1.5),)
#ax2.legend(loc="upper right")
plt.legend(handles=[old, new])
plt.savefig('plot0.png', bbox_inches='tight')
plt.close(fig2)
plt.show()


fig2 = plt.figure()
fig2.suptitle('Variation des angles en fonction du temps.', fontsize=14, fontweight='bold')
ax2 = fig2.add_subplot(111, xlim=(0, 4))
#s2 = 'th2 = '+str(int(math.degrees(q2[0])))+' qd2 = '+str(int(math.degrees(qd2)))
#ax2.set_title(s2)
ax2.grid()
ax2.set_xlabel('Temps (sec)')
ax2.set_ylabel('Angle (rad)')
new, = ax2.plot(tA90, q1A90, 'k-', label="new")
old, = ax2.plot(t90, q190, 'c-', label="old")
ax2.plot(tA90, q2A90, 'k-', label="q2")
ax2.plot(t90, q290, 'c-', label="q2")
ax2.annotate('q1 - π/2 ', xy=(2, 1), xytext=(2, 0.5),)
ax2.annotate('q2', xy=(2, 1), xytext=(2, -1.5),)
#ax2.legend(loc="upper right")
plt.legend(handles=[old, new])
plt.savefig('plot90.png', bbox_inches='tight')
plt.close(fig2)
plt.show()

fig2 = plt.figure()
fig2.suptitle('Suivi de trajectoire', fontsize=14, fontweight='bold')
ax2 = fig2.add_subplot(111, xlim=(0, 40))
#s2 = 'th2 = '+str(int(math.degrees(q2[0])))+' qd2 = '+str(int(math.degrees(qd2)))
#ax2.set_title(s2)
ax2.grid()
ax2.set_xlabel('Temps (sec)')
ax2.set_ylabel('q2 (rad)')


ax2.plot(trAt, trAq2, 'r-', label="new")
ax2.plot(trt, trq2, 'c-', label="old")
ax2.plot(trt, trcmd, 'k--', label="cm")
ax2.legend(loc="upper right")
plt.savefig('traking20.png', bbox_inches='tight')
plt.show()
plt.close(fig2)
