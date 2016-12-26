
def getGains():
	file = open("./Calculs/test2.txt", 'r')
	lines = [line.rstrip('\n') for line in file]
	file.close()
	'''
	je donne des valeurs de 1 au kd.. comme ça je peux evaluer la ligne comme une expression mathématique avec le eval
	'''


	# λ4 + (b1 kdd − b2 kp )λ3 + (b3 kd − α)λ2 + (b4 kp )λ + a = 0
	kp = kd =  kdd = 1

	b1 = b2 = b3 = b4 = a = alpha = 0
	for i in range(len(lines)):
		lines[i] = lines[i].rstrip()
		lines[i] = lines[i].split('-')
		lines[i] =  list(filter(None, lines[i]))
		for j in range(len(lines[i])):
			lines[i][j] = lines[i][j].replace('^', '**')

	lines = list(filter(None, lines))


	ligne0 = lines[0]
	for l in ligne0:
		if eval(l) < 0.001:
			continue
		if 'kdd' in l:
			b1 = eval(l)
		elif 'kp' in l:
			b2 = eval(l)

	ligne0 = lines[1]
	for l in ligne0:
		if eval(l) < 0.001:
			continue
		if 'kd' in l:
			b3 = eval(l)
		else :
			alpha = eval(l)


	ligne0 = lines[2]
	for l in ligne0:
		if eval(l) < 0.001:
			continue
		if 'kp' in l:
			b4 = eval(l)

	ligne0 = lines[3]
	for l in ligne0:
		if eval(l) < 0.001:
			continue
		a += eval(l)

	'''
	print("b1 : ", b1)
	print("b2 : ", b2)
	print("b3 : ", b3)
	print("b4 : ", b4)
	print("a : ", a)
	print("alpha : ", alpha)
	'''

	p = a ** (1 / 4)

	kp = (4 * p ** 3) / b4
	kd = (6 * p ** 2 + alpha) / b3
	kdd = (4 * p + b2 * kp) / b1

	return kp, kd, kdd



b1 = b2 = b3 = b4 = a = alpha = 0
getGains()
