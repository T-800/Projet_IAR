import math
import matlab.engine

print("start engine")
eng = matlab.engine.start_matlab()


def getGains(file="Data/test2.txt"):
	file = open(file, 'r')
	lines = [line.rstrip() for line in file]
	file.close()
	'''
    je donne des valeurs de 1 au kd.. comme ça je peux evaluer la ligne comme une expression mathématique avec le eval
    '''

	kp = kd = kx = 1

	b1 = b2 = b3 = b4 = a = alpha = 0
	lines = list(filter(None, lines))
	for i in range(1, len(lines[:])):
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
		lines[i] = lines[i].replace(' 0 +', ' ')  # on remplace les 0- par -
		lines[i] = lines[i].replace('- 0 ', ' ')  # les +0
		lines[i] = lines[i].replace(' 0 -', ' -')  # on remplace les 0- par -
		lines[i] = lines[i].replace(' + - ', ' - ')  # on remplace les 0- par -
		lines[i] = lines[i].replace(' - + ', ' - ')  # on remplace les 0- par -
		lines[i] = lines[i].replace(' - ', ' -')  # on remplace les 0- par -
		lines[i] = lines[i].replace(' + ', ' +')  # on remplace les 0- par -
		lines[i] = lines[i].lstrip(' ')
		lines[i] = lines[i].rstrip(' ')
		print(lines[i])


	ligne0 = lines[0].replace(' ', '')
	ligne0 = ligne0.split('qd1=')
	qd1 = math.radians(float(ligne0[-1]))
	print('qd1 : ', qd1)
	ligne0 = lines[1].split(' ')
	for l in ligne0:
		if 'kx' in l:
			b1 = eval(l)
		elif 'kp' in l:
			b2 = -eval(l)
			# print(l)

	ligne0 = lines[2].split(' ')
	for l in ligne0:
		if 'kd' in l:
			b3 = eval(l)
		elif l != '':
			alpha = -eval(l)

	ligne0 = lines[3]
	if 'kp' in ligne0:
		b4 = eval(ligne0)

	ligne0 = lines[4]
	if ligne0 != '':
		a = eval(ligne0)

	p = a ** (1 / 4)

	kp = (4 * p ** 3) / b4
	kd = (6 * p ** 2 + alpha) / b3
	kx = (4 * p + b2 * kp) / b1
	return kp, kd, kx, qd1


def send_val_qd2(qd2):
	fic_vals = open("Data/vals_qd.txt", "w")
	fic_vals.write("qd2 = " + str(math.degrees(qd2)) + '\n')
	fic_vals.close()


def calcul_gains_m():
	print("calcul_gains")
	eng.calcul_gains(nargout=0)
	print("fin")

def calcul_gains_tracking_m():
	print("calcul_gains tracking")
	eng.calcul_gains_tracking(nargout=0)
	print("fin")
