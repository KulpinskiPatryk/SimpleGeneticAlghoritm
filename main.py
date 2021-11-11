import numpy.random
from numpy.random import choice as law
from numpy.random import randint as randint
import random
import sys


# Translacja z systemu dwójkowego na system dziesiątkowy
def translate(v):
    number = ''
    for i in range(len(v)):
        number = number + str(v[i])
    return int(number, 2)


# Funkcja Przystosowania czyli funkcja kwadratowa
def fitness(x, a, b, c):
    result = a * x ** 2 + b * x + c
    if result > 0 :
        return result
    elif result < 0:
        result = result - result
        return result


    # Krzyżowanie Kopjujemy wartości by utworzyć pomocnicze tablice dzielimy je i wpisujemy do początkowych tablic
# by utworzyć dzieci
def crossover(r1, r2, cross_point):
    p1 = r1.copy()
    p2 = r2.copy()
    pt = randint(1, len(p1))
    if numpy.random.rand() < cross_point:
        r1 = p1[:pt] + p2[pt:]
        r2 = p2[:pt] + p1[pt:]
    return r1, r2


# Mutacja
def mut(r, mutation_point):
    for i in range(8):
        if numpy.random.rand() < mutation_point:
            if r[i] > 0:
                r[i] = 0
            else:
                r[i] = 1


# Poszukiwanie najlepszego osobnika wyniku
def best_specimen(pop, a, b, c):
    # Utworzenie listy z przystosowaniem
    pop_fitneses = []
    for sub in range(ile_os):
        pop_fitneses.append(fitness(translate(pop[sub]), a, b, c))
    og = translate(pop[0])
    og_val = fitness(og, a, b, c)
    # Znalezienie najlepszego osobnika
    for sub in range(ile_os):
        if pop_fitneses[sub] > og:
            og = translate(pop[sub])
            og_val = pop_fitneses[sub]
    return og, og_val


def genetic_algorithm(iteration, n_pop, cross_point, mutation_point, a, b, c):
    # Utworzenie populacji początkowej
    pop = []
    for i in range(n_pop):
        pop.append([])
    for i in pop:
        for v in range(8):
            i.append(random.randint(0, 1))
    numbered_list = []
    for _ in range(n_pop):
        numbered_list.append(_)
    # Wykożystanie pierwszego osobnika jako najlepszego
    best = translate(pop[0])
    best_val = fitness(best, a, b, c)
    #print('Działanie Programu: ')
    #print('f(' + str(best) + ') = ' + str(best_val))
    # Rozpoczęcie algorytmu
    for gen in range(iteration):
        # Całkowita suma przystosowania
        pop_fitness = 0
        for sub in range(n_pop):
            pop_fitness = pop_fitness + fitness(translate(pop[sub]), a, b, c)
        # Utworzenie listy z poziomem przystosowania
        pop_probabilities = []
        for sub in range(n_pop):
            pop_probabilities.append(fitness(translate(pop[sub]), a, b, c) / pop_fitness)
        # Utworzenie listy z przystosowaniem
        pop_fitneses = []
        for sub in range(n_pop):
            pop_fitneses.append(fitness(translate(pop[sub]), a, b, c))
        # Znalezienie najlepszego osobnika
        for sub in range(n_pop):
            if pop_fitneses[sub] > best_val:
                best = translate(pop[sub])
                best_val = pop_fitneses[sub]
        selected = []
        for sub in range(n_pop):
            selected.append(law(numbered_list, p=pop_probabilities))
        children = []
        for i in range(0, n_pop, 2):
            p1, p2 = pop[selected[i]], pop[selected[i + 1]]
            p1, p2 = crossover(p1, p2, cross_point)
            mut(p1, mutation_point)
            mut(p2, mutation_point)
            children.append(p1)
            children.append(p2)
        pop = children.copy()
    over_best, over_score = best_specimen(pop, a, b, c)
    return over_best, over_score


ile_wyn = 40
ile_os = 10
lb_pop = 10
pr_krzyz = 0.9
pr_mut = 0.2
a = 4
b = 7
c = 2

with open('wyniki.txt', 'w') as f:
    sys.stdout = f
    if lb_pop * ile_os <= 150:
        for i in range(ile_wyn):
            best, score = genetic_algorithm(lb_pop, ile_os, pr_krzyz, pr_mut, a, b, c)
            #print("Wynik : ")
            sys.stdout = f
            print('f(' + str(best) + ') = ' + str(score))
    else:
        print('Nie wlasciwe dane')