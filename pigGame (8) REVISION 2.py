#Erik Rodriguez - TUID: 915255369
#Section 001

import random

mainRun = True
loopRun = True
dice = 0
roll = 0
ply1Tot = 0
ply2Tot = 0


def rollDice():
    dice = random.randrange(1,7)
    print("Roll = ", dice)
    return dice


def turnHmn(playerNum):
    run = True
    turnTot = 0
    choice = ""

    while run == True:
        roll = rollDice()

        if roll == 1:
            print("*** [1] ROLLED ***")
            print("Player",playerNum,"TURN total: 0")
            turnTot = 0
            return turnTot
        else:
            turnTot += roll
            print("TURN Total:", turnTot, end ='')
            choice = input(" | Roll [ENTER] / Hold [ANY KEY]")
            if choice == "":
                continue
            else:
                return turnTot

            
def turnCPU(playerNum):
    run = True
    turnTot = 0
    
    while run == True:
        roll = rollDice()
        
        if roll == 1:
            print("*** [1] ROLLED ***")
            print("Player",playerNum,"TURN total: 0")
            turnTot = 0
            return turnTot
        
        else:
            turnTot += roll

        if playerNum == 1:
            if turnTot + ply1Tot >= 100:
                print("Player",playerNum,"TURN total:", turnTot) 
                return turnTot
        
        elif playerNum == 2:
            if turnTot + ply2Tot >= 100:
                print("Player",playerNum,"TURN total:", turnTot) 
                return turnTot
            
        if turnTot >= 20:
            print("Player",playerNum,"TURN total:", turnTot)     
            return turnTot


def gameWon(player):
    print("Player", player, "W I N S")

while (mainRun == True):
    
    #Player 1
    while loopRun == True:

        print("----------[Turn: PLAYER 1]----------")
        print("------ Player 1 GAME Total:", ply1Tot,"------" )
        ply1Tot += turnHmn(1)
        print("Player 1 GAME Total:", ply1Tot)
        print("")
        print("__________________________________")
        
        if ply1Tot >= 100:
            gameWon(1)
            mainRun = False
            loopRun = False
            break

        print("----------[Turn: PLAYER 2]----------")
        print("------ Player 2 GAME Total:", ply2Tot,"------" )
        ply2Tot += turnCPU(2)
        print("Player 2 GAME Total:", ply2Tot)
        print("")
        print("__________________________________")
        
        if ply2Tot >= 100:
            gameWon(2)
            mainRun = False
            loopRun = False
            break
