import random
god_Pop = []
val_Pop = 2

for i in range(val_Pop):
	god_Pop.append([])
for i in god_Pop:
	for v in range(8):
  		i.append(random.randint(0,1))
print(god_Pop)

#Mutacja
for v in range((1)):
	for i in range(8):
		god_Pop[v][i] = 1
        
for v in range(val_Pop):
	for i in range(8):
		if(god_Pop[v][i] > 0):
			god_Pop[v][i] = 0
		else:
			god_Pop[v][i] = 1            
print(god_Pop)

#Krzyżowanie
r1 = 0
r2 = 1
p1 = god_Pop[r1].copy()
p2 = god_Pop[r2].copy()
print(p1)
print(p2)
for i in range(5):    
	p1[i] = god_Pop[r2][i]
    
for i in range(5):
	p2[i] = god_Pop[r1][i]
print(p1)
print(p2)

#Selekcja
liczba = ''
for i in range(8):
	liczba = liczba + str(p1[i])
print(int(liczba,2))
	




	
main 
GodPopulation

print(god_Pop)



import sys

print('This message will be displayed on the screen.')

original_stdout = sys.stdout 

with open('filename.txt', 'w') as f:
    sys.stdout = f 
    print('This message will be written to a file.')
    sys.stdout = original_stdout 


import sys

print('This message will be displayed on the screen.')

with open('filename.txt', 'w') as f:
    print('This message will be written to a file.', file=f)