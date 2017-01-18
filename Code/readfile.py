import math
import matlab.engine
import sys

# print("start engine")
eng = matlab.engine.start_matlab()


def read_file(file, mode, ks=1):
	file = open(file, 'r')
	lines = [line.rstrip() for line in file]
	#print(lines)
	file.close()
	if mode == 0: # equilibre
		return getGains(lines)
	elif mode == 1: # tracking
		t = []
		g = []
		for l in lines:

			if l == "":
				tu = getGains(t)
				g += [tu]
				t = []
			else:
				t += [l]
		return g
	elif mode == 2: # eequilibre amélioré
		return getGains2(lines, ks)
	else : # tracking amélioré
		t = []
		g = []
		for l in lines:

			if l == "":
				tu = getGains2(t, ks)
				g += [tu]
				t = []
			else:
				t += [l]
		return g


def getGains(lines):
	'''
	je donne des valeurs de 1 au kd.. comme ça je peux evaluer la ligne comme une expression mathématique avec le eval
	'''

	kp = kd = kx = 1

	qd1 = b1 = b2 = b3 = b4 = a = alpha = 0
	lines = list(filter(None, lines))
	if "qd1" in lines[0]:
		ligne0 = lines[0].replace(' ', '')
		ligne0 = ligne0.split('qd1=')
		qd1 = math.radians(float(ligne0[-1]))
		lines = lines[1:]
	for i in range(len(lines[:])):
		lines[i] = lines[i].split(' ')
		for j in range(len(lines[i])):
			lines[i][j] = lines[i][j].replace('^', '**')
			lines[i][j] = lines[i][j].replace('kdd', 'kx')  # on remplace pour eviter les erreur entre kd et kdd
			if lines[i][j] not in '-+' and abs(eval(lines[i][j])) < 0.001:  # si la valeur est trop petite
				lines[i][j] = '0'

	for i in range(len(lines[:])):
		tmp = ''
		for exp in lines[i]:
			tmp = tmp + " " + exp
		tmp += " "
		lines[i] = tmp.replace(' + 0 ', ' ')  # on retire les -0
		lines[i] = lines[i].replace('- 0 ', ' ')  # les +0
		lines[i] = lines[i].replace(' 0 -', ' -')  # on remplace les 0- par -
		lines[i] = lines[i].replace(' 0 +', ' ')  # on remplace les 0- par -
		lines[i] = lines[i].replace(' + - ', ' - ')  # on remplace les 0- par -
		lines[i] = lines[i].replace(' - + ', ' - ')  # on remplace les 0- par -
		lines[i] = lines[i].replace(' - ', ' -')  # on remplace les 0- par -
		lines[i] = lines[i].replace(' + ', ' +')  # on remplace les 0- par -
		lines[i] = lines[i].replace('0  ', ' ')  # on remplace les 0- par -
		lines[i] = lines[i].replace('  ', ' ')  # on remplace les 0- par -
		lines[i] = lines[i].lstrip(' ')
		lines[i] = lines[i].rstrip(' ')
		#print("L^", 3 - i, " ;", lines[i])

	ligne0 = lines[0].split(' ')
	for l in ligne0:
		if 'kx' in l:
			b1 = eval(l)
		elif 'kp' in l:
			b2 = -eval(l)

	ligne0 = lines[1].split(' ')
	for l in ligne0:
		if 'kd' in l:
			b3 = eval(l)
		elif l != '':
			alpha = -eval(l)

	ligne0 = lines[2].split(' ')
	for l in ligne0:
		if 'kp' in l:
			b4 = eval(l)

	ligne0 = lines[3].split(' ')
	for l in ligne0:
		if not 'kd' in l and not 'kx' in l and not 'kp' in l :
			a = eval(l)

	p = a ** (1 / 4)

	kp = (4 * p ** 3) / b4
	kd = (6 * p ** 2 + alpha) / b3
	kx = (4 * p + b2 * kp) / b1


	return kp, kd, kx, qd1


def getGains2(lines, kss):
	'''
	je donne des valeurs de 1 au kd.. comme ça je peux evaluer la ligne comme une expression mathématique avec le eval
	'''

	ks = kp = kd = kx = 1


	qd1 = gK = gamma1 = gamma2 = beta = 0
	lines = list(filter(None, lines))
	if "qd1" in lines[0]:
		ligne0 = lines[0].replace(' ', '')
		ligne0 = ligne0.split('qd1=')
		qd1 = math.radians(float(ligne0[-1]))
		lines = lines[1:]
	for i in range(len(lines[:])):
		lines[i] = lines[i].split(' ')
		for j in range(len(lines[i])):
			lines[i][j] = lines[i][j].replace('^', '**')
			lines[i][j] = lines[i][j].replace('kdd', 'kx')  # on remplace pour eviter les erreur entre kd et kdd
			try:
				if lines[i][j] not in '-+' and abs(eval(lines[i][j])) < 0.001:  # si la valeur est trop petite
					lines[i][j] = '0'
			except TypeError:
				print("except", lines[i][j])

	for i in range(len(lines[:])):
		tmp = ''
		for exp in lines[i]:
			tmp = tmp + " " + exp
		tmp += " "
		lines[i] = tmp.replace(' + 0 ', ' ')  # on retire les -0
		lines[i] = lines[i].replace('- 0 ', ' ')  # les +0
		lines[i] = lines[i].replace(' 0 -', ' -')  # on remplace les 0- par -
		lines[i] = lines[i].replace(' 0 +', ' ')  # on remplace les 0- par -
		lines[i] = lines[i].replace(' + - ', ' - ')  # on remplace les 0- par -
		lines[i] = lines[i].replace(' - + ', ' - ')  # on remplace les 0- par -
		lines[i] = lines[i].replace(' - ', ' -')  # on remplace les 0- par -
		lines[i] = lines[i].replace(' + ', ' +')  # on remplace les 0- par -
		lines[i] = lines[i].replace('  ', ' ')  # on remplace les 0- par -
		lines[i] = lines[i].lstrip(' ')
		lines[i] = lines[i].rstrip(' ')
		#print("apres :", lines[i])

	ligne0 = lines[0].split(' ')
	ligne0 = list(filter(None, ligne0))
	for l in ligne0:
		if 'kx' in l:
			gK = eval(l)
		else:
			print("Error in lambda^3")

	ligne0 = lines[1].split(' ')
	ligne0 = list(filter(None, ligne0))
	for l in ligne0:
		if 'kd' in l:
			pass
			t = eval(l)

		elif 'ks' in l:

			gamma1 = eval(l)
		else :
			beta = eval(l)

	ligne0 = lines[2]
	if 'kp' in ligne0:
		t = eval(ligne0)

	ligne0 = lines[3]
	if 'ks' in ligne0:
		s = ligne0.split('*')[0]
		gamma2 = eval(s)


	p4 = (gamma2 * kss)#/a
	#print("p4 : ", p4)
	p = p4 ** (1/4)
	# print("p : ", p)


	kp = (4 * p ** 3) / gK
	kd = (6 * p ** 2 - beta - gamma1 * kss) / gK
	kx = (4 * p) / gK


	return kp, kd, kx, qd1


def send_val_qd2(qd2):
	fic_vals = open("Data/vals_qd.txt", "w")
	fic_vals.write("qd2 = " + str(math.degrees(qd2)) + '\n')
	fic_vals.close()


def calcul_gains_m(bool):
	if bool:
		eng.calcul_gain_equilibre_amelioration(nargout=0)
	else :
		eng.calcul_gains_equilibre(nargout=0)


def calcul_gains_tracking_m():
	eng.calcul_gains_tracking(nargout=0)

def calcul_gains_tracking_amelioration_m():
	eng.calcul_gains_tracking_amelioration(nargout=0)
