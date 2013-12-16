import math
import random

car = 2
goat = 1

sims = 1000
wins = 0

for i in range(sims): 
    #assign car and goat to doors
    doors = [0, 1, 2]
    #print doors
    random.shuffle(doors)
    #print doors

    #switch player starts by choosing a door
    firstchoice = random.randrange(0,3)
    #print firstchoice

    #create new doorset
    newdoors=[]
    for i in range(len(doors)):
        if i != firstchoice:
            newdoors.append(doors[i])
    #print newdoors

    #if car is in door then choose one of the other doors else choose the door
    #without the car to show the contestant
    if doors[firstchoice] == car:
        montychoice = random.randrange(0,2)
        #print montychoice
        otherdoor = newdoors[montychoice]
        #print otherdoor
        if 0 == montychoice:
            switchdoor = 1
        else:
            switchdoor = 0
        #print newdoors[switchdoor]
        if newdoors[switchdoor] == 2:
            wins += 1
    else:
        if newdoors[0] == car:
            otherdoor = newdoors[1]
            switchdoor = 0
            #print newdoors[switchdoor]
            if newdoors[switchdoor] == 2:
                wins += 1
        else:
            otherdoor = newdoors[0]
            switchdoor = 1
            #print newdoors[switchdoor]
            if newdoors[switchdoor] == 2:
                wins += 1
winprob = wins/float(sims)*100.
print "With switching wins %: " + str(winprob)

sims = 1000
noswitch_wins = 0

for i in range(sims):
    #assign car and goat to doors
    doors = [0, 1, 2]
    #print doors
    random.shuffle(doors)
    #print doors

    #no switch player starts by choosing a door
    firstchoice = random.randrange(0,3)
    #print firstchoice

    #create new doorset
    newdoors=[]
    for i in range(len(doors)):
        if i != firstchoice:
            newdoors.append(doors[i])
    #print newdoors

    #if car is in door then choose on of the other doors else choose the door
    #without the car to show the contestant
    if doors[firstchoice] == car:
        noswitch_wins += 1
noswitchwinprob = noswitch_wins/float(sims)*100.
print "With no swtiching wins %: " + str(noswitchwinprob)
