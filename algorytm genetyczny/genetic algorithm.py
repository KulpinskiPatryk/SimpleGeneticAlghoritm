# import random
from numpy.random import randint
from numpy.random import rand
 
# przerobić na funkcję kwadratową liczącą maksimum
def objective(x):
	return x[0]**2.0 + x[1]**2.0
 
# translacja kodu binarnego na wartość
def decode(bounds, n_bits, bitstring):
	# stworzenie dodatkowej listy do przechowywania wyników clever as fuck
	decoded = list()
	# wartość maksymalna dla ilości bitów u mnie jest to 256
	largest = 2**n_bits
	for i in range(len(bounds)):
		# extract the substring
		start, end = i * n_bits, (i * n_bits)+n_bits
		substring = bitstring[start:end]
		# convert bitstring to a string of chars
		chars = ''.join([str(s) for s in substring])
		# convert string to integer
		integer = int(chars, 2)
		# scale integer to desired range
		value = bounds[i][0] + (integer/largest) * (bounds[i][1] - bounds[i][0])
		# zapisanie wartości ważne !!!!
		decoded.append(value)
	return decoded
 
# selekcja turniejowa 
def selection(pop, scores, k=3):
	# first random selection
	selection_ix = randint(len(pop))
	for ix in randint(0, len(pop), k-1):
		# check if better (e.g. perform a tournament)
		if scores[ix] < scores[selection_ix]:
			selection_ix = ix
	return pop[selection_ix]


	# 	random_number # Between 0.0 and 1.0
	#
	# if random_number < 0.1
	#     select 1
	# else if random_number < 0.3 # 0.3 − 0.1 = 0.2 probability
	#     select 2
	# else if random_number < 0.6 # 0.6 − 0.3 = 0.3 probability
	#     select 3
	# else if random_number < 1.0 # 1.0 − 0.6 = 0.4 probability
	#     select 4
	# end if
 
# crossover two parents to create two children
def crossover(p1, p2, r_cross):
	# children are copies of parents by default
	c1, c2 = p1.copy(), p2.copy()
	# check for recombination
	if rand() < r_cross:
		# select crossover point that is not on the end of the string
		pt = randint(1, len(p1)-2)
		# perform crossover
		c1 = p1[:pt] + p2[pt:]
		c2 = p2[:pt] + p1[pt:]
	return [c1, c2]
 
# mutation operator
def mutation(bitstring, r_mut):
	for i in range(len(bitstring)):
		# check for a mutation
		if rand() < r_mut:
			# flip the bit
			bitstring[i] = 1 - bitstring[i]
 
# genetic algorithm
def genetic_algorithm(objective, bounds, n_bits, n_iter, n_pop, r_cross, r_mut):
	# initial population of random bitstring
	pop = [randint(0, 2, n_bits*len(bounds)).tolist() for _ in range(n_pop)]
	# keep track of best solution
	best, best_eval = 0, objective(decode(bounds, n_bits, pop[0]))
	# enumerate generations
	for gen in range(n_iter):
		# decode population
		decoded = [decode(bounds, n_bits, p) for p in pop]
		# evaluate all candidates in the population
		scores = [objective(d) for d in decoded]
		# check for new best solution
		for i in range(n_pop):
			if scores[i] < best_eval:
				best, best_eval = pop[i], scores[i]
				print(">%d, new best f(%s) = %f" % (gen,  decoded[i], scores[i]))
		# select parents
		selected = [selection(pop, scores) for _ in range(n_pop)]
		# create the next generation
		children = list()
		for i in range(0, n_pop, 2):
			# get selected parents in pairs
			p1, p2 = selected[i], selected[i+1]
			# crossover and mutation
			for c in crossover(p1, p2, r_cross):
				# mutation
				mutation(c, r_mut)
				# store for next generation
				children.append(c)
		# replace population
		pop = children
	return [best, best_eval]
 
# define range for input
bounds = [[-5.0, 5.0], [-5.0, 5.0]]
# define the total iterations
n_iter = 100
# bits per variable
n_bits = 16
# define the population size
n_pop = 100
# crossover rate
r_cross = 0.9
# mutation rate
r_mut = 1.0 / (float(n_bits) * len(bounds))
# perform the genetic algorithm search
best, score = genetic_algorithm(objective, bounds, n_bits, n_iter, n_pop, r_cross, r_mut)
print('Done!')
decoded = decode(bounds, n_bits, best)
print('f(%s) = %f' % (decoded, score))


#AS: Jeżeli masz daną funkcję kwadratową y = a*x2 + b*x + c,
#to ekstrema tej funkcji znajdziesz wzorami (na pewno je znasz} 

#xw = -b/2*a , yw = -delta/4*a

#przy czym 
#gdy a > 0 to zachodzi minimum
#gdy a < 0 to zachodzi maksimum
# # https://stackoverflow.com/questions/41047229/genetic-algorithm-to-solve-a-quadratic-equation
# # https://rocreguant.com/roulette-wheel-selection-python/2019/
#
# def fitness(x):
# 	return a*x**2 + b*x + c
#
#
#
#
# import numpy as np
#
# def roulette_wheel_selection(population):
#
#     # Computes the totallity of the population fitness
#     god_pop_fitness = sum([fitness(pop) for pop in god_pop])
#
#     # Computes for each chromosome the probability
#     pop_probabilities = [chromosome.fitness/population_fitness for chromosome in population]
#
#     # Selects one chromosome based on the computed probabilities
#     return np.random.choice(population,size=len(pop), p=chromosome_probabilities)
#
#
#  'a'int translacja -> int pop_fitness -> array propabilty -> selekcja -> cross(selekcja(pop), selekcja(pop))  /
# -> mutation -> nextgeneration -> pop = nextgeneration.copy -> repeat from a