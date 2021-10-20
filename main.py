from numpy.random import choice as law_of_nature
from numpy.random import randint as randint
import random

god_pop = []
used_values = []
val_Pop = 4
iteration = 3
a = 1
b = 1
c = 1



def best():
    winner = 0
    for v in range(val_Pop):
        if winner < translate(v):
            winner = translate(v)
    return winner


def fitness(x):
    return a * x ** 2 + b * x + c


# Mutacja
def mut(r):
    for i in range(8):
        if ((random.randint(0, 9) / 10) <= 0.1):
            if (god_pop[r][i] > 0):
                god_pop[r][i] = 0
            else:
                god_pop[r][i] = 1


# Krzyżowanie
def crossover(r1, r2):
    p1 = god_pop[r1].copy()
    p2 = god_pop[r2].copy()
    pt = randint(1, len(p1) - 2)
    if random.randint(0, 11) <= 7:
        god_pop[r1] = p1[:pt] + p2[pt:]
        god_pop[r2] = p2[:pt] + p1[pt:]
    mut(r1)
    mut(r2)


# Translacja
def translate(v):
    liczba = ''
    for i in range(len(god_pop[v])):
        liczba = liczba + str(god_pop[v][i])
    return int(liczba, 2)


def selection():
    r1 = random.randint(0, val_Pop - 1)
    return r1


def roulette_wheel_selection():
    # Computes the totallity of the population fitness
    god_pop_fitness = sum([fitness(translate(pop)) for pop in range(len(god_pop))])
    print(god_pop_fitness)
    # Computes for each chromosome the probability
    pop_probabilities = [fitness(translate(pop)) / god_pop_fitness for pop in range(len(god_pop))]
    print(pop_probabilities)
    # Selects one chromosome based on the computed probabilities
    #return law_of_nature(god_pop, p=pop_probabilities)


for i in range(val_Pop):
    god_pop.append([])
for i in god_pop:
    for v in range(8):
        i.append(random.randint(0, 1))
print(god_pop)
print(best())
for i in range(iteration):
    for v in range(int(val_Pop)):
        crossover(selection(), selection())
    print(god_pop)
    print(best())
    roulette_wheel_selection()
