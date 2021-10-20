import random
from typing import List, Any

god_pop = []
used_values = []
a = 1
b = 1
c = 1
ile_wyn = 1
lb_pop = 1
ile_os = 2
pr_krzyz = 0.9
pr_mut = 0.1


def calculate():
    x = random.randint(-127, 128)
    goal = (a * (x ** 2)) + (b * x) + c
    return goal


# Tworzenie Populacji Ikea
def Population():
    for i in range(ile_os):
        god_pop.append([])
    for i in god_pop:
        for v in range(8):
            i.append(random.randint(0, 1))
    print(god_pop)


# Mutacja
def mut(r):
    for i in range(8):
        if random.randint(0, 11) <= pr_mut:
            if god_pop[r][i] > 0:
                god_pop[r][i] = 0
            else:
                god_pop[r][i] = 1


# Krzyżowanie
def cross():
    r1 = random.randint(0, ile_os-1)
    r2 = random.randint(0, ile_os - 1)
    while r1 == r2 :
        r2 = random.randint(0, ile_os-1)
    print(r1)
    print(r2)
    p1 = god_pop[r1].copy()
    p2 = god_pop[r2].copy()
    pc = random.randint(0, 7)
    if (random.randint(0, 9) / 10) <= pr_krzyz:
        for i in range(pc):
            p1[i] = god_pop[r2][i]
            p2[i] = god_pop[r1][i]
    god_pop[r1] = p1.copy()
    god_pop[r2] = p2.copy()
    #mut(r1)
   #mut(r2)
    print(p2, end=" ")
    print(p1)


# Translacja
def translate(v):
    liczba = ''
    for i in range(8):
        liczba = liczba + str(god_pop[v][i])
    return int(liczba, 2)


# Selekcja wybierania najlepszego osobnika //Powinno się zapisywać jego numer
def best():
    winner = 0
    pretendet = 0
    for v in range(ile_os):
        if ((goal - winner) >= (goal - translate(v))):
            winner = translate(v)
    return winner


# Losowanie Par poprawienie losawiania losowanie oparte na selekcji




# Główna Funkcja Programu

if(lb_pop * ile_os) <= 150:
    for wyn in range(ile_wyn):
        Population()
        for i in range(lb_pop):
            for v in range(int(ile_os/2)):
                cross()
            print(god_pop)
            print(str(calculate()) + '/')
else:
    print('Błędna ilość lb_pop bądź ile_os')