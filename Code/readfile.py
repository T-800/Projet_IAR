import re
def getGains():
	file = open("./Calculs/test2.txt", 'r')
	lines = [line.rstrip() for line in file]
	file.close()
	'''
	je donne des valeurs de 1 au kd.. comme ça je peux evaluer la ligne comme une expression mathématique avec le eval
	'''


	# λ4 + (b1 kdd − b2 kp )λ3 + (b3 kd − α)λ2 + (b4 kp )λ + a = 0
	kp = kd =  kx = 1

	b1 = b2 = b3 = b4 = a = alpha = 0
	lines = list(filter(None, lines))
	for i in range(len(lines[:])):
		lines[i] = lines[i].split(' ')
		for j in range(len(lines[i])):
			lines[i][j] = lines[i][j].replace('^', '**')
			lines[i][j] = lines[i][j].replace('kdd', 'kx')
			if lines[i][j] not in '-+' and abs(eval(lines[i][j])) < 0.001:
				lines[i][j] = '0'

	for i in range(len(lines[:])):
		tmp = ''
		for exp in lines[i]:
			tmp = tmp + " "+ exp
		tmp += " "
		lines[i] = tmp.replace(' - 0', ' ')
		lines[i] = lines[i].replace(' + 0 ', ' ')
		lines[i] = lines[i].replace(' 0 - ', ' -')
		delimiters = " - ", " + "
		regexPattern = '|'.join(map(re.escape, delimiters))
		lines[i] = re.split(regexPattern, lines[i])
		print(lines[i])

	ligne0 = lines[0]
	for l in ligne0:
		if 'kx' in l:
			b1 = eval(l)
		elif 'kp' in l:
			b2 = eval(l)

	ligne0 = lines[1]
	for l in ligne0:
		if 'kd' in l:
			b3 = eval(l)
		else:
			alpha = eval(l)

	ligne0 = lines[2]
	for l in ligne0:
		if 'kp' in l:
			b4 = eval(l)

	ligne0 = lines[3]
	for l in ligne0:
		a = eval(l)

	'''
	for i in range(len(lines)):
		lines[i] = lines[i].rstrip()
		#print(lines[i])
		lines[i] = lines[i].split(' - ')
		lines[i] =  list(filter(None, lines[i]))
		for j in range(len(lines[i])):
			if j > 0:
				lines[i][j]  = '-' + lines[i][j]
			lines[i][j] = lines[i][j].replace('^', '**')
			lines[i][j] = lines[i][j].replace('kdd', 'kx')


	lines = list(filter(None, lines))
	#print(lines)

	ligne0 = lines[0]
	for l in ligne0:
		if abs(eval(l)) < 0.001:
			continue
		if 'kx' in l:
			b1 = eval(l)
		elif 'kp' in l:
			b2 = eval(l)

	ligne0 = lines[1]
	for l in ligne0:
		if abs(eval(l)) < 0.001:
			continue
		if 'kd' in l:
			b3 = eval(l)
		else :
			alpha = eval(l)


	ligne0 = lines[2]
	for l in ligne0:
		if abs(eval(l)) < 0.001:
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


	p = a ** (1 / 4)

	kp = (4 * p ** 3) / b4
	kd = (6 * p ** 2 + alpha) / b3
	kx = (4 * p + b2 * kp) / b1

	return kp, kd, kx



#b1 = b2 = b3 = b4 = a = alpha = 0
getGains()
