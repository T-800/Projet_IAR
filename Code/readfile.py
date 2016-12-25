lines = [line.rstrip('\n') for line in open("./Calculs/test.txt", 'r')]

'''
je donne des valeurs de 1 au kd.. comme ça je peux evaluer la ligne comme une expression mathématique avec le eval
'''
kdd = 1
kd = 1
kp = 1


line0 = lines[0]
line0 = line0.split(' ')
line0 = line0[0]

tab = []
for line in lines:
	ll = line.split(' ')
	t = []
	for l in ll:
		if l and l is not '-':
			l = l.replace('^', '**')  # je remplace la puissance par la puissance en python
			number = eval(l)

			if number < 0.01:  ## si le nombre est trop petit je le prend pas
				number = 0
			else:
				t += [number]
	if t:
		tab += [t]


b1 = tab[0][0]
b2 = 0
if len(tab[0]) > 1:
	b2 = tab[0][-1]


b3 = tab[1][0]
alpha = tab[1][-1]

b4 = tab[2][0]

a =  tab[3][0]

p =  a ** (1 / 4)

kp = (4 * p ** 3) / b4
kd = (6 * p**2 + alpha)/b3
kdd = (4 * p + b2 * kp) / b1

print("kp :", kp)
print("kd :", kd)
print("kkdd :", kdd)