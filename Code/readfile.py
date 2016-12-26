
def getGains():
	file = open("./Calculs/test.txt", 'r')
	lines = [line.rstrip('\n') for line in file]
	file.close()
	'''
	je donne des valeurs de 1 au kd.. comme ça je peux evaluer la ligne comme une expression mathématique avec le eval
	'''


	# λ4 + (b1 kdd − b2 kp )λ3 + (b3 kd − α)λ2 + (b4 kp )λ + a = 0

	b1 = b2 = b3 = b4 = a = alpha = 0

	ligne0 = lines[0]
	ligne0 = ligne0.split('-')
	ligne0 =  list(filter(None, ligne0))
	for l in ligne0:
		l = l.replace('^', '**')
		if eval(l) < 0.001:
			continue
		if 'kdd' in l:
			b1 = eval(l)
		elif 'kp' in l:
			b2 = eval(l)

	ligne0 = lines[2]
	ligne0 = ligne0.split('-')
	ligne0 = list(filter(None, ligne0))
	for l in ligne0:
		l = l.replace('^', '**')
		if eval(l) < 0.001:
			continue
		if 'kd' in l:
			b3 = eval(l)
		else :
			alpha = eval(l)


	ligne0 = lines[4]
	ligne0 = ligne0.split('-')
	ligne0 = list(filter(None, ligne0))
	for l in ligne0:
		l = l.replace('^', '**')
		if eval(l) < 0.001:
			continue
		if 'kp' in l:
			b4 = eval(l)

	ligne0 = lines[6]
	ligne0 = ligne0.split('-')
	ligne0 = list(filter(None, ligne0))
	for l in ligne0:
		l = l.replace('^', '**')
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
