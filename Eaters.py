"""
Started on 26. 04. 2012., by Bane. (actually started on 09.05.2012.)

This is a simple Python script which simulates evolution. The "Eaters", or "Flatlanders" move on the screen randomly eating everything green they collide with. The bigger they are, the more things they should be able to eat, ergo average radius of a Flatlander will increase over time due to evolution.
"""

from engine import *

All = [] #An array of everything
startTime = time.time() #Start time

for i in range(nFL):
    r = rand(1, FLR)
    All.append(Flatlander([rand(r, size[0] - r), rand(r, size[1] - r)], {"r": r}, 100))
    
follow = Flatlander([rand(r, size[0] - r), rand(r, size[1] - r)], {"r": r}, 100)


All.append(follow)

for i in range(nFood):
    r = rand(1, foodR)
    All.append(Food((rand(r, size[0] - r), rand(FLR, size[1] - r)), r))

while True: #The main loop
    screen.fill(bgC) #Erase everything

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()        
        
        if event.type == KEYUP and event.key == K_ESCAPE:
            exit()        
    
    
    new = []
    die = []
    
    for ob in All:
        if ob.drawable:
           ob.draw()
       
        if isinstance(ob, Flatlander):
            ob.pos[0] += ob.speed[0]
            ob.pos[1] += ob.speed[1]
            
            ob.speed[0] += rand(-1, 1)*random.random()
            ob.speed[1] += rand(-1, 1)*random.random()
            
            if ob.pos[0] + ob.r >= size[0]:
                ob.pos[0] = size[0] - ob.r
                ob.speed[0] *= -1

            if ob.pos[1] + ob.r >= size[1]:
                ob.pos[1] = size[1] - ob.r
                ob.speed[1] *= -1

            if ob.pos[0] - ob.r <= 0:
                ob.pos[0] = ob.r
                ob.speed[0] *= -1

            if ob.pos[1] - ob.r <= 0:
                ob.pos[1] = ob.r
                ob.speed[1] *= -1

            ob.energy -= 0.2
            offset = 0
            
            if ob.speed[1] > maxSpeed[1]:
                ob.speed[1] = maxSpeed[1]

            if ob.speed[1] < -maxSpeed[1]:
                ob.speed[1] = -maxSpeed[1]

            if ob.speed[0] > maxSpeed[0]:
                ob.speed[0] = maxSpeed[0]

            if ob.speed[0] < -maxSpeed[0]:
                ob.speed[0] = -maxSpeed[0]
            
            for i in range(len(All)):
                i += offset
                
                if collides(ob.pos, ob.r, All[i].pos, All[i].r) and isinstance(All[i], Food) and ob.energy + All[i].r < maxEnergy:
                    ob.energy += All[i].r
                    All.pop(i)
                    offset -= 1
    
            if rand(0, 1000) == 0:
                new_genome = copy.copy(ob.genome)
                
                for gene in new_genome:
                    new_genome[gene] += new_genome[gene]*0.4*rand(-1, 1)
    
                new.append(Flatlander(copy.copy(ob.pos), new_genome, ob.energy/2))
                ob.energy *= 0.5
                
            if (ob.energy < 0):
                die.append(All.index(ob))

    r = rand(1, foodR)
    All.append(Food((rand(r, size[0] - r), rand(FLR, size[1] - r)), r))

    All = remove(All, die)    
        
    for ob in new:
        All.append(ob)

    pygame.display.flip()
    #time.sleep(0.01)
