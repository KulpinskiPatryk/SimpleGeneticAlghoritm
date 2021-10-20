import random

god_Pop = []
used_values = []
val_Pop = 4
iteration = 3


# Mutacja
def mut(r):
	for i in range(8):
		if ((random.randint(0, 9) / 10) <= 0.1):
			if (god_Pop[r][i] > 0):
				god_Pop[r][i] = 0
			else:
				god_Pop[r][i] = 1


# Krzyżowanie
def cross(r1, r2):
	p1 = god_Pop[r1].copy()
	p2 = god_Pop[r2].copy()
	if random.randint(0, 11) <= 7:
		for i in range((random.randint(0, 7))):
			p1[i] = god_Pop[r2][i]
			p2[i] = god_Pop[r1][i]
	god_Pop[r1] = p1.copy()
	god_Pop[r2] = p2.copy()
	mut(r1)
	mut(r2)


# Translacja
def translate(v):
	liczba = ''
	for i in range(8):
		liczba = liczba + str(god_Pop[v][i])
	return int(liczba, 2)


def best():
	winner = 0
	for v in range(val_Pop):
		if (winner < translate(v)):
			winner = translate(v)
	return winner


def check():
	r1 = random.randint(0, val_Pop - 1)
	return r1


for i in range(val_Pop):
	god_Pop.append([])
for i in god_Pop:
	for v in range(8):
		i.append(random.randint(0, 1))
print(god_Pop)
for i in range(iteration):
	for v in range(int(val_Pop)):
		cross(check(), check())
	print(god_Pop)
	print(best())
